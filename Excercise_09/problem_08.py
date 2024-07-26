# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.


from datetime import datetime, timedelta

def calculate_future_date():
    try:
       
        start_date_str = input("Enter a starting date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        num_days = int(input("Enter number of days: "))
        future_date = start_date + timedelta(days=num_days)
        future_date_str = future_date.strftime('%Y-%m-%d')
        
        print(f"The date {num_days} days after {start_date_str} is {future_date_str}")
        
    except ValueError:
        print("Invalid input. Please enter date in YYYY-MM-DD format and a valid integer for number of days.")

calculate_future_date()
