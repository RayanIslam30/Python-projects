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
            birthdate = datetime.date(year,month,day) #Check if we have a valid date
            today = datetime.date.today() #Get todays date
        except(ValueError):
            return("Invalid date")
    else: #If not, invalid
        return("Invalid date")
    time = today - birthdate #Get the difference between the dates
    minutes = time.days * 24 * 60 #Convert difference to minutes
    p = inflect.engine() #Run inflect to convert number to words
    minutes_since = p.number_to_words(minutes, andword="") 
    return minutes_since.capitalize() + " minutes" #Return the output in proper format
    
if __name__ == "__main__": #Only run main if file ran directly
    main()