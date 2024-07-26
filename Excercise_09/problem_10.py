from datetime import datetime

def convert_datetime_format(datetime_str):
    try:
        # Convert input datetime string to datetime object
        dt_obj = datetime.strptime(datetime_str, "%m/%d/%Y %H:%M:%S")
        # Format datetime object to desired format
        formatted_datetime_str = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_datetime_str
    except ValueError:
        return "Invalid datetime format. Please enter datetime in MM/DD/YYYY HH:MM:SS format."

# Example usage:
datetime_str = "12/25/2023 15:30:00"
formatted_datetime = convert_datetime_format(datetime_str)
print(f"The formatted datetime is: {formatted_datetime}")
