import os

from sickchill.providers.metadata import generic


class PS3Metadata(generic.GenericMetadata):
    """
    Metadata generation class for Sony PS3.

    The following file structure is used:

    show_root/cover.jpg                         (poster)
    show_root/Season ##/filename.ext            (*)
    show_root/Season ##/filename.ext.cover.jpg  (episode thumb)
    """

    def __init__(
        self,
        show_metadata=False,
        episode_metadata=False,
        fanart=False,
        poster=False,
        banner=False,
        episode_thumbnails=False,
        season_posters=False,
        season_banners=False,
        season_all_poster=False,
        season_all_banner=False,
    ):
        super().__init__(
            show_metadata, episode_metadata, fanart, poster, banner, episode_thumbnails, season_posters, season_banners, season_all_poster, season_all_banner
        )

        self.name = "Sony PS3"

        self.poster_name = "cover.jpg"

        # web-ui metadata template
        self.eg_show_metadata = "<i>not supported</i>"
        self.eg_episode_metadata = "<i>not supported</i>"
        self.eg_fanart = "<i>not supported</i>"
        self.eg_poster = "cover.jpg"
        self.eg_banner = "<i>not supported</i>"
        self.eg_episode_thumbnails = "Season##\\<i>filename</i>.ext.cover.jpg"
        self.eg_season_posters = "<i>not supported</i>"
        self.eg_season_banners = "<i>not supported</i>"
        self.eg_season_all_poster = "<i>not supported</i>"
        self.eg_season_all_banner = "<i>not supported</i>"

    # Override with empty methods for unsupported features
    def retrieveShowMetadata(self, folder):
        # no show metadata generated, we abort this lookup function
        return None, None, None

    def create_show_metadata(self, show_obj):
        pass

    def update_show_indexer_metadata(self, show_obj):
        pass

    def get_show_file_path(self, show_obj):
        pass

    def create_episode_metadata(self, episode_object):
        pass

    def create_fanart(self, show_obj):
        pass

    def create_banner(self, show_obj):
        pass

    def create_season_posters(self, show_obj):
        pass

    def create_season_banners(self, episode_object):
        pass

    def create_season_all_poster(self, show_obj):
        pass

    def create_season_all_banner(self, show_obj):
        pass

    @staticmethod
    def get_episode_thumb_path(episode_object):
        """
        Returns the path where the episode thumbnail should be stored. Defaults to
        the same path as the episode file but with a .cover.jpg extension.

        episode_object: a TVEpisode instance for which to create the thumbnail
        """
        if os.path.isfile(episode_object.location):
            tbn_filename = episode_object.location + ".cover.jpg"
        else:
            return None

        return tbn_filename


# present a standard "interface" from the module
metadata_class = PS3Metadata
