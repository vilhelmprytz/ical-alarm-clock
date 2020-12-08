#!/usr/bin/env python3

from json import dumps
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from os import environ
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
    events = get_context_events(url=URL)

    if len(events) == 0:
        return jsonify({"alarm": False})

    date = get_alarm_time(events=events, hours=HOURS, minutes=MINUTES)

    return jsonify(
        {
            "alarm": True,
            "year": date.year,
            "month": date.month,
            "day": date.day,
            "hour": date.hour,
            "minute": date.minute,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
