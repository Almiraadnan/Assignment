from datetime import datetime
import pytz

def localize_datetime(dt, tz_str):
    """
    Localizes a naive datetime object to the specified timezone.
    
    Parameters:
    - dt: datetime object (naive)
    - tz_str: timezone string (e.g., 'America/New_York')
    
    Returns:
    - Localized datetime object in the specified timezone.
    """
    tz = pytz.timezone(tz_str)
    localized_dt = tz.localize(dt)
    return localized_dt

# Prompt the user for input
tz_str = input("Enter the timezone (e.g., 'America/New_York'): ").strip()

# Create a naive datetime object from user input (assuming format yyyy-mm-dd hh:mm:ss)
dt_str = input("Enter the datetime (yyyy-mm-dd hh:mm:ss): ").strip()
dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

# Localize the datetime to the specified timezone
localized_dt = localize_datetime(dt, tz_str)

# Print the localized datetime
print(f"Localized datetime in {tz_str}: {localized_dt}")
