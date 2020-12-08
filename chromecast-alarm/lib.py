from json import load


def read_config():
    with open("config.json") as f:
        config = load(f)
    return config
