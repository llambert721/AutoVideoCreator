"""Module edits all videos into one file"""
import random
from moviepy.editor import VideoFileClip, clips_array, CompositeVideoClip
from misc_functions import video_exists, paths
from config_funcs import config_create

#config = config_create(paths["config"])

def video_edit(top_vid, bottom_vid):
    """Function edits top and bottom video into one final file"""
    config = config_create(paths["config"])

    if isinstance(top_vid, list) is False or isinstance(bottom_vid, list) is False:
        top_vid = list(top_vid.split(" "))
        bottom_vid = list(bottom_vid.split(" "))

    for value in top_vid:
        value = str(value)
        final_name = value.replace("-temp", "")
        if video_exists(final_name + "-PT1.mp4", paths["videos_final"]):
            print(f"Skipped rendering {value} since it already exists!")
            continue
        top_clip = VideoFileClip(f"videos_temp/top/{value}.mp4")
        bottom_clip = VideoFileClip(f"./videos_temp/bottom/{random.choice(bottom_vid)}.mp4")
        bottom_clip_edit = bottom_clip

        if config["mute_bottom_video"]:
            bottom_clip_edit = bottom_clip.without_audio()
        bottom_clip_edit = trim_bottom_to_top(top_clip, bottom_clip_edit)

        combined = clips_array([[top_clip],
                                [bottom_clip_edit]])
        clips = trim_video(combined)

        for i, clip in enumerate(clips):
            clip.write_videofile(f"./videos_final/{final_name}-PT{i + 1}.mp4")
            clip.close()
        print(f"\nExported {len(clips)} video clips!")
        print("Find them in the 'videos_final' folder")
        combined.close()
        bottom_clip.close()
        top_clip.close()
        bottom_clip_edit.close()


def trim_video(video: CompositeVideoClip):
    """Function trims video to fit certain length"""
    config = config_create(paths["config"])
    clips = []
    subclip_start = 0
    end = int(video.duration)

    if end < int(config["max_clip_length"]):
        clips.append(video)
        return clips

    while True:
        end = trim_math(int(video.duration), subclip_start)
        if end == int(video.duration):
            trimed_video = video.subclip(subclip_start, end)
            clips.append(trimed_video)
            break
        trimed_video = video.subclip(subclip_start, end)
        subclip_start = end

        clips.append(trimed_video)
    return clips


def trim_math(duration: int, curr: int):
    """Function does math for trim_video function"""
    config = config_create(paths["config"])
    target = curr + int(config["max_clip_length"])
    difference = duration - target
    if difference <= 0:
        return duration
    duration = duration - difference
    return duration


def trim_bottom_to_top(top_video: CompositeVideoClip, bottom_video: CompositeVideoClip):
    """Function trims bottom video to top videos length"""
    if int(top_video.duration) < int(bottom_video.duration):
        bottom_video = bottom_video.subclip(0, int(top_video.duration))
    return bottom_video
