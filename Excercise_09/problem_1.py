# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".

from datetime import datetime

def get_current_date():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    return formatted_date

current_date = get_current_date()

print("Current date:", current_date)

# Output: Current date: 2022-11-13


