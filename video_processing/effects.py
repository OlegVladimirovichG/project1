from moviepy.editor import VideoFileClip, vfx

def apply_video_effect(video: VideoFileClip, effect_type: str) -> VideoFileClip:
    """Применяет эффекты к видео."""
    if effect_type == 'speed':
        return video.fx(vfx.speedx, 1.5)  # Ускоряем видео
    elif effect_type == 'color-grading':
        return video.fx(vfx.colorx, 1.2)  # Цветокоррекция
    else:
        return video
