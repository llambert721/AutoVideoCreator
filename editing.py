from moviepy.editor import *
import random
from misc_functions import *

config = config_create()

def video_edit(top_vid, bottom_vid):
    if type(top_vid) != list or type(bottom_vid) != list:
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


def trim_math(duration: int, curr):
    target = curr + int(config["max_clip_length"])
    x = duration - target
    if x <= 0:
        return duration
    duration = duration - x
    return duration


def trim_bottom_to_top(top_video: CompositeVideoClip, bottom_video: CompositeVideoClip):
    if int(top_video.duration) < int(bottom_video.duration):
        bottom_video = bottom_video.subclip(0, int(top_video.duration))
    return bottom_video
