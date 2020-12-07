#!/usr/bin/env python3

from ics import Calendar
from datetime import datetime, date, timedelta
import requests

__author__ = "Vilhelm Prytz"
__email__ = "vilhelm@prytznet.se"


def get_alarm_time(url: str, hours: int, minutes: int):
    cal = Calendar(requests.get(url).text)

    today = date.today()
    tomorrow = today + timedelta(days=1)
    alarm_diff = timedelta(hours=hours, minutes=minutes)

    tomorrow_events = []

    for event in list(cal.timeline):
        begin_datetime_obj = datetime.strptime(
            str(event.begin)[:19], "%Y-%m-%dT%H:%M:%S"
        )

        if (
            begin_datetime_obj.year == tomorrow.year
            and begin_datetime_obj.month == tomorrow.month
            and begin_datetime_obj.day == tomorrow.day
        ):
            tomorrow_events.append(begin_datetime_obj)

    # no events tomorrow; no alarm clock
    if len(tomorrow_events) == 0:
        return False

    first_event = min(tomorrow_events)
    return first_event - alarm_diff
