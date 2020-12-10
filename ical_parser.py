#!/usr/bin/env python3

from ics import Calendar
from datetime import datetime, timedelta
import requests

__author__ = "Vilhelm Prytz"
__email__ = "vilhelm@prytznet.se"


def get_context_events(url: str, context: datetime):
    cal = Calendar(requests.get(url).text)

    events = []

    for event in list(cal.timeline):
        begin_datetime_obj = datetime.strptime(
            str(event.begin)[:19], "%Y-%m-%dT%H:%M:%S"
        )

        if (
            begin_datetime_obj.year == context.year
            and begin_datetime_obj.month == context.month
            and begin_datetime_obj.day == context.day
        ):
            events.append(begin_datetime_obj)

    return events


def get_alarm_time(events: list, hours: int, minutes: int):
    alarm_diff = timedelta(hours=hours, minutes=minutes)

    first_event = min(events)
    return first_event - alarm_diff
