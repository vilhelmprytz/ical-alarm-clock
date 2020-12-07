# ical-alarm-clock

Returns the date and time for which an alarm should be set based on `.ics` file (from URL) and user settings.

## Instructions

Create a file named `config.json` with the following contents.

```json
{
  "url": "https://ical.example.com/foobar.ics",
  "alarm": {
    "hours": 1,
    "minutes": 0
  }
}
```

The endpoint `/api/date` will then return a JSON blob. The day will always be one day forward. If your first event is at `08:30` and your `config.json` is set to 1 hour, it will return the following JSON-blob:

```json
{
  "alarm": true, // only set alarm if this is true
  "year": 2020, // the year tomorrow
  "month": 12, // the month tomorrow
  "day": 8, // the day tomorrow
  "hour": 7,
  "minute": 30
}
```

If you have no events tomorrow and no alarm is required, the API will simply return:

```json
{
  "alarm": false
}
```

## Author

Created by [Vilhelm Prytz](https://github.com/vilhelmprytz).
