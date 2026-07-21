#Code that takes a date, and calculates the time in minutes since that date, printing it out in words

import datetime #Import the datetime module
import inflect #Use to convert number into words

def main():
    print(calculate(input("Date: ")))

def calculate(date):
    if date.count("-") == 2:
        year, month, day = date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        datetime.date(year,month,day)
    else:
        return("Invalid date")
    


...


if __name__ == "__main__": #Only run main if file ran directly
    main()