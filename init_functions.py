import os
import pyinputplus as pyip
import re
import toml
from configwriter import config_write
from termcolor import colored

paths = {"bottom_video_links": "./text_files/bottom_video_links.txt",
         "top_video_links": "./text_files/top_video_links.txt",
         "config": "./text_files/config.toml",
         "videos_final": "./videos_final",
         "temp_top": "./videos_temp/top",
         "temp_bottom": "./videos_temp/bottom",
         "text_files": "./text_files",
         "videos_temp": "./videos_temp"}


def folder_file_create():
    folders = ["videos_final", "videos_temp", "text_files"]
    sub_folders = ["top", "bottom"]
    files = ["top_video_links.txt", "bottom_video_links.txt", "config.toml"]

    for folder in folders:  # Creates base folders
        path = os.path.join("./", folder)
        try:
            os.makedirs(path)
        except FileExistsError:
            continue

    for sub_folder in sub_folders:  # Creates sub folders
        path = os.path.join(paths["videos_temp"], sub_folder)
        try:
            os.makedirs(path)
        except FileExistsError:
            continue

    for file in files:
        path = os.path.join(paths["text_files"], file)
        try:
            with open(path, "x") as f:
                continue
        except FileExistsError:
            continue

    lines = file_read(paths["config"])
    if len(lines) <= 0:
        config_write(paths["config"])

def config_create():
    config = toml.load(f="text_files/config.toml")
    return config


def start():
    print_avc()
    response = pyip.inputMenu(choices=["Single Video", "Multiple Videos", "Clear Temp Files", "Cancel"],
                              numbered=True)
    clear()

    return response


def clear():  # Clears terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def folder_clear(path):
    files = os.listdir(path)
    temp_files = check_file_ending(files)

    for file in temp_files:
        os.remove(os.path.join(path, file))


def check_folders():
    top_files = os.listdir(paths["temp_top"])
    bottom_files = os.listdir(paths["temp_bottom"])

    if len(top_files) != 0:
        folder_clear(paths["temp_top"])
    if len(bottom_files) != 0:
        folder_clear(paths["temp_bottom"])


def check_file_ending(files: list):
    delete_files = []
    for f in files:
        f = str(f)
        if f.endswith("-temp.mp4"):
            delete_files.append(f)
    return delete_files


def file_read(file):
    with open(file) as f:
        lines = f.readlines()
        return lines


def clean_title(title):
    temp = re.sub(r"\.[a-zA-Z]{,4}$", "", title)  # remove any file ending ex: ".exe"
    temp = re.sub(r"\s", "_", temp)  # replace white spaces with an underscore
    temp = re.sub(r"\W", "", temp)  # remove any slashes

    # removes any emojis
    emoji_regex_pattern = re.compile(pattern="["
                                             u"\U0001F600-\U0001F64F"
                                             u"\U0001F300-\U0001F5FF"
                                             u"\U0001F680-\U0001F6FF"
                                             u"\U0001F1E0-\U0001F1FF"
                                             "]+", flags=re.UNICODE)
    temp = re.sub(emoji_regex_pattern, "", temp)
    return temp


def delete_dup_links(file):
    raw_dup_lines = file_read(file)
    cleaned_dup_lines = []
    for i in raw_dup_lines:
        cleaned_dup_lines.append(i.replace("\n", ""))
    lines = [*set(cleaned_dup_lines)]

    file_write(file, lines)


def file_write(file, links):
    with open(file, "w") as f:
        f.writelines(link + "\n" for link in links)


def video_exists(file_name, path):
    files = os.listdir(path)

    if file_name in files:
        return True
    else:
        return False


def print_avc():
    avc = """
   ▄████████  ▄█    █▄   ▄████████ 
  ███    ███ ███    ███ ███    ███ 
  ███    ███ ███    ███ ███    █▀  
  ███    ███ ███    ███ ███        
▀███████████ ███    ███ ███        
  ███    ███ ███    ███ ███    █▄  
  ███    ███ ███    ███ ███    ███ 
  ███    █▀   ▀██████▀  ████████▀                                
"""
    colored_avc = colored(avc, color="blue")
    print(colored_avc)

