#Code to take a .csv file and put it into a more readable table

import sys #Import sys to use sys.argv and take system arguments
import csv #Import csv module to work with our csv files
from tabulate import tabulate #Import tabulate to format data

csv_data = [] #Set a list to store our data
#Check that sys.argv[1] exists
if len(sys.argv) == 2: #If file is valid, set name variable to file name
    name = sys.argv[1] #set our file name to file user inputted
elif len(sys.argv) == 1: #If sys.argv[1] doesn't exist, quit with too few arguments
    sys.exit("Too few command-line arguments")
else: #If there are more than 1 argument, quit with too many arguments
    sys.exit("Too many command-line arguments")

#Make sure the file is actually a .py file, otherwise quit
if not name.endswith(".csv"):
    sys.exit("Not a CSV file")

#If all those checks passed, try and access the csv file
try:
    with open(name) as file: 
        reader = csv.reader(file) #use csv reader to cleanly access the csv file
        print(tabulate(reader, headers="firstrow", tablefmt="grid")) #Use tabulate to print out a nice table
except FileNotFoundError: #If file cannot be found, then quit
    sys.exit("File does not exist")
