#Code that takes a period of time in 12 hour AM/PM, and converts it to that time period in 24 hour

import re

def main():
    print(convert(input("Hours: ")))


def convert(time):
    if time := re.search(r"^(\d{1,2}|\d{1,2}:\d{2}) (AM|PM) to (\d{1,2}|\d{1,2}:\d{2}) (AM|PM)$", time, re.IGNORECASE): #Check that user inputted what should be a valid time
        return "works"

...


if __name__ == "__main__":
    main()