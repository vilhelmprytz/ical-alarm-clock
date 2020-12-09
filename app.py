#!/usr/bin/env python3

from json import dumps
from flask import Flask, jsonify
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


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()

    response.data = dumps(
        {"code": e.code, "name": e.name, "description": e.description}
    )

    response.content_type = "application/json"
    return response, e.code


@app.route("/api/alarm")
def get_alarm():
    # this might be the worst way ever to avoid running
    # datetime.now() multiple times and avoiding
    # variable declarations... utterly stupid but it work's
    curr_time = [
        {
            "year": x.year,
            "month": x.month,
            "day": x.day,
            "hour": x.hour,
            "minute": x.minute,
        }
        for x in [datetime.now()]
    ][0]

    events = get_context_events(url=URL)

    if len(events) == 0:
        return jsonify({"alarm": False, "curr_time": curr_time})

    date = get_alarm_time(events=events, hours=HOURS, minutes=MINUTES)

    return jsonify(
        {
            "alarm": True,
            "year": date.year,
            "month": date.month,
            "day": date.day,
            "hour": date.hour,
            "minute": date.minute,
            "curr_time": curr_time,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
