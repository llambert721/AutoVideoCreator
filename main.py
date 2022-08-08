from init_functions import *
folder_file_create()  # Creates folders / files for videos (skips if they already exist)
from choices import *

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
        exit()
    else:
        exit()
