# ical-alarm-clock

Returns the date and time for which an alarm should be set based on `.ics` file (from URL) and user settings.

## Instructions

Create a file named `.env` with the following contents.

```bash
URL="https://ical.example.com/foobar.ics"
HOURS="1"
MINUTES="0"
```

You can also run a Docker container. `--env-file` can be replaced with `--env URL="" --env HOURS=1 --env MINUTES=1` if you do not want to create a `.env` file.

```bash
docker run --env-file .env --restart unless-stopped --name ical-alarm-clock -d -p 5000:5000 prytz/ical-alarm-clock:latest
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
