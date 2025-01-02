import datetime
import threading
import time

import sickchill
from sickchill import logger, settings
from sickchill.helper.exceptions import CantRefreshShowException, CantUpdateShowException
from sickchill.oldbeard import db, network_timezones, ui
from sickchill.show.Show import Show


class ShowUpdater(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.amActive = False

        self.seven_days = 7 * 24 * 60 * 60

    def run(self, force=False):
        if self.amActive:
            return

        self.amActive = True
        try:
            logger.info("ShowUpdater for tvdb Api V3 starting")

            cache_db_con = db.DBConnection("cache.db")
            for index, provider in sickchill.indexer:
                database_result = cache_db_con.select("SELECT `time` FROM lastUpdate WHERE provider = ?", [provider.name])
                last_update = int(database_result[0][0]) if database_result else 0
                network_timezones.update_network_dict()
                update_timestamp = int(time.time())
                updated_shows = []

                if last_update:
                    logger.info("Last update: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last_update))))

                    current_check = update_timestamp
                    while current_check >= last_update:
                        try:
                            TvdbData = sickchill.indexer[1].updates(fromTime=current_check - self.seven_days, toTime=current_check)
                            TvdbData.series()
                            updated_shows.extend([d["id"] for d in TvdbData.series])
                        except Exception as error:
                            logger.info(error)

                        current_check -= self.seven_days - 1
                else:
                    logger.info(_("No last update time from the cache, so we do a full update for all shows"))

                pi_list = []
                for cur_show in settings.show_list:
                    if settings.stopping or settings.restarting:
                        break
                    try:
                        cur_show.next_episode()

                        skip_update = False
                        # Skip ended or paused shows until interval is met
                        if (cur_show.status == "Ended" or cur_show.paused) and settings.ENDED_SHOWS_UPDATE_INTERVAL != 0:  # 0 is always
                            if settings.ENDED_SHOWS_UPDATE_INTERVAL == -1:  # Never
                                skip_update = True
                            if (
                                datetime.datetime.today() - datetime.datetime.fromordinal(cur_show.last_update_indexer or 1)
                            ).days < settings.ENDED_SHOWS_UPDATE_INTERVAL:
                                skip_update = True

                        # When last_update is not set from the cache or the show was in the tvdb updated list we update the show
                        if not last_update or (cur_show.indexerid in updated_shows and not skip_update):
                            pi_list.append(Show.update(cur_show, force))
                        elif not skip_update:
                            # TODO: do we really need to refresh every show every day if it is not updated?
                            # Temporarily use the same duration for paused as ended
                            pi_list.append(Show.refresh(cur_show, force))
                    except (CantUpdateShowException, CantRefreshShowException) as error:
                        logger.info(_("Automatic update failed: {error}").format(error=error))

                ui.ProgressIndicators.setIndicator("dailyUpdate", ui.QueueProgressIndicator("Daily Update", pi_list))

                if database_result:
                    cache_db_con.action("UPDATE lastUpdate SET `time` = ? WHERE provider = ?", [str(update_timestamp), provider.name])
                else:
                    cache_db_con.action("INSERT INTO lastUpdate (time, provider) VALUES (?, ?)", [str(update_timestamp), provider.name])
        except Exception as error:
            logger.exception(error)

        self.amActive = False

    @staticmethod
    def request_hook(response, **kwargs):
        logger.info(f"{response.request.method} URL: {response.request.url} [Status: {response.status_code}]")

    def __del__(self):
        pass
