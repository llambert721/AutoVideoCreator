"""Module handles user choice"""
import pyinputplus as pyip
from youtube import yt_downloader
from misc_functions import clear, folder_clear, delete_dup_links, file_read, paths
import editing


def single_vid():
    """Function handles single video flow"""
    url = pyip.inputURL(prompt="Enter top video URL: ")
    downloads, top_video = yt_downloader(url, "top")
    print(f"Downloaded {downloads} top video!")

    url = pyip.inputURL(prompt="Enter bottom video URL: ")
    downloads, bottom_video = yt_downloader(url, "bottom")
    print(f"Downloaded {downloads} bottom video!")
    clear()

    editing.video_edit(top_video, bottom_video)


def clear_temp_files():
    """Function clears all -temp video files"""
    folder_clear(paths["temp_bottom"])
    folder_clear(paths["temp_top"])
    print("Cleared all temp files!")


def multiple_vids():
    """Function handles multiple video flow"""
    delete_dup_links(paths["top_video_links"])
    delete_dup_links(paths["bottom_video_links"])

    top_video_links = file_read(paths["top_video_links"])
    bottom_video_links = file_read(paths["bottom_video_links"])

    top_file_list = []
    bottom_file_list = []

    input("Enter YT links into .txt files\nRemember 1 link per line!\nPress enter to continue")
    clear()

    for top_link in top_video_links:
        downloads, top_video = yt_downloader(top_link, "top")
        print(f"Downloaded {downloads} top videos!")
        top_file_list.append(top_video)
    for bottom_link in bottom_video_links:
        downloads, bottom_video = yt_downloader(bottom_link, "bottom")
        print(f"Downloaded {downloads} bottom videos!")
        bottom_file_list.append(bottom_video)
    clear()
    editing.video_edit(top_file_list, bottom_file_list)
