#Code that takes a date, and calculates the time in minutes since that date, printing it out in words

import datetime #Import the datetime module
import inflect #Use to convert number into words

def main():
    print(calculate(input("Date: ")))

def calculate(date):
    if date.count("-") == 2: #Check if format is at least close to what we want
        year, month, day = date.split("-") #Split into year, month, day by splitting at '-'
        year = int(year)
        month = int(month)
        day = int(day)
        try:
            datetime.date(year,month,day) #Check if we have a valid date
        except(ValueError):
            return("Invalid date")
    else: #If not, invalid
        return("Invalid date")
    


if __name__ == "__main__": #Only run main if file ran directly
    main()