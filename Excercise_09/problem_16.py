#create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/

from datetime import datetime

date_string = "08-26-2023 08:10:00 PM"
datetime_object = datetime.strptime(date_string, "%m-%d-%Y %H:%M:%S %p")


print(datetime_object)