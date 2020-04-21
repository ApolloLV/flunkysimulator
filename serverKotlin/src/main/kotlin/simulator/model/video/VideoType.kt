package simulator.model.video

import de.flunkyteam.endpoints.projects.simulator.EnumVideoType

enum class VideoType {
    Setup, Hit, CloseMiss, Miss, Stop
}

fun VideoType.toGrpc(): EnumVideoType = when (this){
    VideoType.Setup -> EnumVideoType.SETUP_VIDEOTYPE
    VideoType.Hit -> EnumVideoType.HIT_VIDEOTYPE
    VideoType.CloseMiss -> EnumVideoType.NEAR_MISS_VIDEOTYPE
    VideoType.Miss -> EnumVideoType.MISS_VIDEOTYPE
    VideoType.Stop -> EnumVideoType.STOP_VIDEOTYPE
}