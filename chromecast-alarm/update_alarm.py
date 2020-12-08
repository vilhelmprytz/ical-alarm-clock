#!/usr/bin/env python3

import requests
from json import dump
from lib import read_config


def get_alarm_time(config: dict):
    r = requests.get(config["endpoint_url"])
    return r.json()


def write_file(config: dict):
    with open("alarm.json", "w") as f:
        dump(get_alarm_time(config), f)


def main():
    config = read_config()
    write_file(config)


if __name__ == "__main__":
    main()
