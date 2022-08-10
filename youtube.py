"""Module downloads videos from youtube"""
from pathlib import Path
from pytube import YouTube
import pytube
from misc_functions import clean_title, video_exists, paths
from config_funcs import config_create

#config = config_create(paths["config"])

def yt_downloader(urls, folder):
    """Functions takes youtube URL and downloads the video"""
    config = config_create(paths["config"])
    vid_downloaded = 0
    if isinstance(urls, list) is False:
        urls = list(urls.split(" "))

    for url in urls:
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
