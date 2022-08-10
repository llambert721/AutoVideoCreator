"""Main program loop"""
import sys
from misc_functions import start, clear, folder_file_create, paths
from choices import single_vid, clear_temp_files, multiple_vids
from config_funcs import config_create

folder_file_create()  # Creates folders / files for videos (skips if they already exist)
config_create(paths["config"])
while True:
    startResp = start()

    if startResp == "Single Video":
        single_vid()
        clear_temp_files()
        clear()
    elif startResp == "Multiple Videos":
        multiple_vids()
        clear_temp_files()
        clear()
    elif startResp == "Clear Temp Files":
        clear_temp_files()
    elif startResp == "Cancel":
        sys.exit()
    else:
        sys.exit()
