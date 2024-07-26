# Write a Python program that uses the datetime module to print the current date and time.

from datetime import datetime

def get_current_datetime():
    current_datetime = datetime.now()
    return current_datetime

current_datetime = get_current_datetime()

print("Current date and time:", current_datetime)