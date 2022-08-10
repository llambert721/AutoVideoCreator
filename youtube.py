from pytube import YouTube
import pytube
from misc_functions import *
from pathlib import Path

config = config_create()

def yt_downloader(url, folder):
    vid_downloaded = 0
    if type(url) != list:
        url = list(url.split(" "))

    for url in url:
        try:
            vid = YouTube(url).streams.get_highest_resolution()
        except pytube.exceptions.RegexMatchError:
            continue
        vid_title = clean_title(vid.title)

        if video_exists(vid_title + "-perm.mp4", paths["temp_bottom"]):
            print(f"Skipped downloading {vid_title} since it already exists!")
            vid_downloaded = 0
            continue
        if video_exists(vid_title + "-perm.mp4", paths["temp_top"]):
            print(f"Skipped downloading {vid_title} since it already exists!")
            vid_downloaded = 0
            continue

        if config["save_bottom_video"] and folder == "bottom":
            vid_title += "-perm"
        else:
            vid_title += "-temp"

        print("Downloading video...")
        vid.download(output_path=Path(paths["videos_temp"], folder), filename=f"{vid_title}.mp4")
        vid_downloaded = 1

    return (vid_downloaded, vid_title)
