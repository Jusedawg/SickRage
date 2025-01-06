from sickchill.views.api.authentication import KeyHandler
from sickchill.views.api.webapi import (
    ApiCall,
    ApiError,
    ApiHandler,
    CMDBacklog,
    CMDComingEpisodes,
    CMDDailySearch,
    CMDEpisode,
    CMDEpisodeSearch,
    CMDEpisodeSetStatus,
    CMDExceptions,
    CMDFailed,
    CMDFullSubtitleSearch,
    CMDHelp,
    CMDHistory,
    CMDHistoryClear,
    CMDHistoryTrim,
    CMDLogs,
    CMDLogsClear,
    CMDPostProcess,
    CMDProperSearch,
    CMDShow,
    CMDShowAddExisting,
    CMDShowAddNew,
    CMDShowCache,
    CMDShowDelete,
    CMDShowGetBanner,
    CMDShowGetFanArt,
    CMDShowGetNetworkLogo,
    CMDShowGetPoster,
    CMDShowGetQuality,
    CMDShowPause,
    CMDShowRefresh,
    CMDShows,
    CMDShowSeasonList,
    CMDShowSeasons,
    CMDShowSetQuality,
    CMDShowsStats,
    CMDShowStats,
    CMDShowUpdate,
    CMDSickChill,
    CMDSickChillAddRootDir,
    CMDSickChillCheckScheduler,
    CMDSickChillCheckVersion,
    CMDSickChillDeleteRootDir,
    CMDSickChillGetDefaults,
    CMDSickChillGetMessages,
    CMDSickChillGetRootDirs,
    CMDSickChillPauseBacklog,
    CMDSickChillPing,
    CMDSickChillRestart,
    CMDSickChillSearchIndexers,
    CMDSickChillSearchTVDB,
    CMDSickChillSearchTVRAGE,
    CMDSickChillSetDefaults,
    CMDSickChillShutdown,
    CMDSickChillUpdate,
    CMDSubtitleSearch,
    function_mapper,
    TVDBShorthandWrapper,
)