#Code to take date in month-day-year order, and converts to year-month-day order

#A list of all months, a dictionary that converts the name of the month to the number
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    
}

def main(): 
    date = input("Input date: ").strip().lower() #Take user input, remove whitespace and put into lowercase
    converted_date = convert(date)


#Function to convert from MM/DD/YYYY to YYYY-MM-DD, OR 'Month', 
def convert():

    month, day, year =
