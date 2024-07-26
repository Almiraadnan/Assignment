# Write a program that converts a given date time (tz aware) string from one timezone to another.

from datetime import datetime
import pytz


def change_timezone(dt, tz_str):
    tz = pytz.timezone(tz_str)
    return dt.astimezone(tz)

dt = datetime.now()
dt_ny = change_timezone(dt, 'America/New_York')

print("Original datetime:", dt)
print("New York datetime:", dt_ny)




    