"""Module handles config and config writing"""
from pathlib import Path
import toml

CONFIG_DEFAULT_STRING = """
max_clip_length = 180 # How long each clip should be when rendering video. default 3 mins (counted in seconds).
mute_bottom_video = true # mutes bottom video. (should only be true or false).
save_bottom_video = false # saves temp bottom videos. default false (should only be true or false).
"""
config_parsed = toml.loads(CONFIG_DEFAULT_STRING)
#config = toml.load(f="text_files/config.toml")

def config_write(file):
    """Function writes config"""
    with open(file, "w", encoding="utf-8") as open_file:
        toml.dump(config_parsed, open_file)

def config_create(path: Path):
    """Function checks and creates the config file"""
    if path.is_file() is False:
        config_write(path)
    config = toml.load(Path("text_files", "config.toml"))
    return config
