#!/usr/bin/env python3

import pychromecast
from datetime import datetime
from json import load
from lib import read_config


def play_sound(url: str, friendly_name: str):
    services, browser = pychromecast.discovery.discover_chromecasts()
    pychromecast.discovery.stop_discovery(browser)
    chromecasts, browser = pychromecast.get_listed_chromecasts(
        friendly_names=[friendly_name]
    )
    cast = chromecasts[0]
    cast.wait()
    mc = cast.media_controller
    mc.play_media(url, "audio/mpeg")
    mc.block_until_active()


def read_alarm():
    with open("alarm.json") as f:
        alarm = load(f)
    return alarm


if __name__ == "__main__":
    config = read_config()
    alarm = read_alarm()
    now = datetime.now()

    if not alarm["alarm"]:
        exit(0)

    if (
        now.year == alarm["year"]
        and now.month == alarm["month"]
        and now.day == alarm["day"]
        and now.hour == alarm["hour"]
        and now.minute == alarm["minute"]
    ):
        print("Running alarm!")
        play_sound(config["url"], config["friendly_name"])
