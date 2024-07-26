
# Create a function that takes a datetime object and a number of hours as input, then returns a new datetime object with the added hours.

from datetime import datetime, timedelta

def add_hours(datetime_obj, hours):
    return datetime_obj + timedelta(hours=hours)

current_datetime = datetime.now()
added_hours = 3
new_datetime = add_hours(current_datetime, added_hours)
print(new_datetime)  # Output: 2023-03-15 16:25:16.786571