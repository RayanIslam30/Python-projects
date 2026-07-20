#Code that takes a period of time in 12 hour AM/PM, and converts it to that time period in 24 hour

import re

def main():
    print(convert(input("Hours: ")))


def convert(time):
    #Set up baseline values for output at the end, in case they don't get overwritten
    minute = int(0)
    minute2 = int(0)
    if time := re.search(r"^(\d{1,2}|\d{1,2}:\d{2}) (AM|PM) to (\d{1,2}|\d{1,2}:\d{2}) (AM|PM)$", time, re.IGNORECASE): #Check that user inputted what should be a valid time
        #Define variables
        start_time = time.group(1)
        start_ampm = time.group(2)
        end_time = time.group(3)
        end_ampm = time.group(4)
        if ":" in start_time: #If we got hours and minutes for first time
            hour, minute = start_time.split(":")
            hour = int(hour)
            minute = int(minute)
            if hour not in range(1,13): #If hour isn't valid hour, raise value error
                raise ValueError("Invalid hour")
            if minute not in range(0,60): #If minute isn't valid minute, raise value error
                raise ValueError("Invalid minute")
            if start_ampm == "PM" or start_ampm == "pm":
                hour+=12
        else: #We just got hour for first time
            hour = int(start_time)
            if hour not in range(1,13): #If hour isn't valid hour, raise value error
                raise ValueError("Invalid hour") 
            if start_ampm == "PM" or start_ampm == "pm":
                hour+=12

        if ":" in end_time: #If we got hours and minutes for second time
            hour2, minute2 = end_time.split(":")
            hour2 = int(hour2)
            minute2 = int(minute2)
            if hour2 not in range(1,13): #If hour isn't valid hour, raise value error
                raise ValueError("Invalid hour")
            if minute2 not in range(0,60): #If minute isn't valid minute, raise value error
                raise ValueError("Invalid minute")
            if end_ampm == "PM" or end_ampm == "pm":
                hour2+=12
        else: #We just got hour for first time
            hour2 = int(end_time)
            if hour2 not in range(1,13): #If hour isn't valid hour, raise value error
                raise ValueError("Invalid hour") 
            if end_ampm == "PM" or end_ampm == "pm":
                hour2+=12
    else: #If input isn't valid, raise value error
        raise ValueError("Invalid input")
        
    #Print out our converted time
    return(f"{hour:02}:{minute:02} to {hour2:02}:{minute2:02}")


if __name__ == "__main__":
    main()