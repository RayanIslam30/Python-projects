# Code to take a date in month-day-year order and convert it to year-month-day order.

# A list of all months, a dictionary that converts the name of the month to the number
months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def main():
    while True:
        date = input("Date: ").strip().lower()

        try:
            converted_date = convert(date)
            print(converted_date)
            break
        except ValueError:
            pass


# Function to convert from MM/DD/YYYY to YYYY-MM-DD, OR 'Month' 'Day', 'Year'
def convert(date):
    parts = (
        date.split()
    )  # saves our split string, splits where there is whitespace, used if they input actual month name
    if "/" in date:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if (
            month < 1 or month > 12 or day < 1 or day > 31
        ):  # If day or month not valid, raise exception
            raise ValueError
    elif (
        len(parts) == 3 and parts[0] in months and parts[1].endswith(",")
    ):  # Case to convert if user inputted actual month name, check if that is in our months dictionary and that input has valid formatting
        month_name = parts[0]  # month
        day = parts[1].rstrip(",")
        year = parts[2]
        month = months[month_name]
        day = int(day)
        year = int(year)
        if day < 1 or day > 31:  # Check for invalid day
            raise ValueError
    else:  # If date is invalid, ask for date again, raise exception
        raise ValueError

    return f"{year}-{month:02d}-{day:02d}"  # Return YYYY-MM-DD


if __name__ == "__main__":  # Only run main if file ran directly
    main()
