#!/usr/bin/env python3

from json import dumps
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
from os import environ
from datetime import datetime
from ical_parser import get_alarm_time, get_context_events

__author__ = "Vilhelm Prytz"
__email__ = "vilhelm@prytznet.se"


URL = environ["URL"]
HOURS = int(environ["HOURS"])
MINUTES = int(environ["MINUTES"])

app = Flask(__name__)


def check_int(x: int):
    try:
        int(x)
    except Exception:
        return False
    return True


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()

    response.data = dumps(
        {"code": e.code, "name": e.name, "description": e.description}
    )

    response.content_type = "application/json"
    return response, e.code


@app.route("/api/alarm", methods=["POST", "GET"])
def get_alarm():
    def _verify_valid_context(context: dict):
        for i in ("year", "month", "day", "hour", "minute"):
            if i not in context:
                return False
            if not check_int(context[i]):
                return False
        return True

    def _datetime_jsonify(i: datetime):
        return {
            "year": i.year,
            "month": i.month,
            "day": i.day,
            "hour": i.hour,
            "minute": i.minute,
        }

    hours = HOURS
    minutes = MINUTES

    curr = datetime.now()
    context = curr

    if request.method == "POST":
        blob = request.json

        hours = (
            int(blob["hours"])
            if "hours" in blob and check_int(blob["hours"])
            else HOURS
        )
        minutes = (
            int(blob["minutes"])
            if "minutes" in blob and check_int(blob["minutes"])
            else MINUTES
        )
        context = (
            datetime(
                int(blob["context"]["year"]),
                int(blob["context"]["month"]),
                int(blob["context"]["day"]),
                int(blob["context"]["hour"]),
                int(blob["context"]["minute"]),
            )
            if "context" in blob and _verify_valid_context(blob["context"])
            else curr
        )

    events = get_context_events(url=URL, context=context)

    # format to return
    curr_time = _datetime_jsonify(curr)
    context_time = _datetime_jsonify(context)

    if len(events) == 0:
        return jsonify(
            {"alarm": False, "curr_time": curr_time, "context_time": context_time}
        )

    date = get_alarm_time(events=events, hours=hours, minutes=minutes)

    return jsonify(
        {
            "alarm": True,
            "year": date.year,
            "month": date.month,
            "day": date.day,
            "hour": date.hour,
            "minute": date.minute,
            "curr_time": curr_time,
            "context_time": context_time,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
