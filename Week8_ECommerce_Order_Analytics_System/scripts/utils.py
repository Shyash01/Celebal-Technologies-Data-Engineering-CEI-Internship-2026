from datetime import datetime


# Convert string to datetime object

def convert_to_date(date_string):

    return datetime.strptime(
        date_string,
        "%Y-%m-%d"
    )


# Check if start date comes before end date

def validate_date_range(start_date, end_date):

    start = convert_to_date(start_date)
    end = convert_to_date(end_date)

    return start <= end


# Format currency for reporting

def format_currency(amount):

    if amount is None:
        amount = 0

    return f"₹{amount:,.2f}"


# Print section heading

def print_heading(title):

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)