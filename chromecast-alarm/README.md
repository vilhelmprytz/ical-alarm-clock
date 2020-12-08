# ical-alarm-clock/chromecast-alarm

Two simple scripts for triggering a Chromecast sound when the alarm is due.

- `update_alarm.py` updates the `alarm.json` with information about when to ring the alarm. Create a cronjob to run this every hour or something
- `run.py` will trigger the Chromecast. Create a cronjob to run this every minute.
