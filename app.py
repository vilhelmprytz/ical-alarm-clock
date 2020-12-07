#!/usr/bin/env python3

from json import dumps
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from os import environ
from ical_parser import get_alarm_time

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


@app.route("/api/date")
def get_alarm():
    date = get_alarm_time(url=URL, hours=HOURS, minutes=MINUTES)

    if date == False:
        return jsonify({"alarm": False})

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
