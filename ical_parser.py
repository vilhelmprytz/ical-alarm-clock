#!/usr/bin/env python3

from ics import Calendar
from datetime import datetime, timedelta
import requests

__author__ = "Vilhelm Prytz"
__email__ = "vilhelm@prytznet.se"


def _ical_arrow_to_datetime(x):
    return datetime.strptime(str(x)[:19], "%Y-%m-%dT%H:%M:%S")


def get_context_events(url: str, context: datetime):
    cal = Calendar(requests.get(url).text)

    events = []

    for event in list(cal.timeline):
        begin = _ical_arrow_to_datetime(event.begin)

        if (
            begin.year == context.year
            and begin.month == context.month
            and begin.day == context.day
        ):

            # "all day" events should be ignored
            if begin + timedelta(hours=24) == _ical_arrow_to_datetime(event.end):
                continue

            events.append(begin)

    return events


def get_alarm_time(events: list, hours: int, minutes: int):
    alarm_diff = timedelta(hours=hours, minutes=minutes)

    first_event = min(events)
    return first_event - alarm_diff
