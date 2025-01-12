from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))  # Format and display

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add)  # Calculate future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))  # Format and display

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
