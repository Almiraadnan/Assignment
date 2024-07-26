 #Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

import datetime as datetime 

def main():
    date_str = input("Enter a date in the format MM/DD/YYYY: ")
    converted_date = convert_date(date_str)  
def convert_date(date_str):
    month, day, year = map(int, date_str.split('/'))
    new_date = datetime.date(year, month, day)
    converted_date = new_date.strftime('%Y-%m-%d')
    
    return converted_date
date_str = "07/24/2024"
converted_date = convert_date(date_str)
print(converted_date)  # Output: 2024-07-24

