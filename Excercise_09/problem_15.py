# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00" 
# hint: https://strftime.org/

from datetime import datetime

date_string = "26-08-2023 15:18:33.983780-07:00"
datetime_object = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S.%f%z")


print(datetime_object)

