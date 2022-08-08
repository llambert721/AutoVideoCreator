import toml

config_default_string = """
max_clip_length = 180 # How long each clip should be when rendering video. default 3 mins (counted in seconds).
mute_bottom_video = true # mutes bottom video. (should only be true or false).
save_bottom_video = false # saves temp bottom videos. default false (should only be true or false).
"""
config_parsed = toml.loads(config_default_string)
#config = toml.load(f="text_files/config.toml")


def config_write(file):
    with open(file, "w") as f:
        toml.dump(config_parsed, f)
