#Code to take a time, and figure out if it is breakfast, lunch, dinner, or none 

def main():
    time = input("What time is it? ").lower().strip() #Prompt the user for input and convert it to lowercase and remove whitespace

    if time.endswith("am") or time.endswith("pm"): #Code to run if the time is in AM or PM format, convert to 24h format
        converted_time = convert12h(time)
    else: #Code to run if the time is in 24h format   
        converted_time = convert24h(time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
    else:
        print("")

def convert24h(x):
    #Convert the time to a float
    hours, minutes = x.split(":")
    minutes = float(minutes)* (5/3) #Convert the minutes to a decimal value
    return float(hours) + minutes

def convert12h(x):
    #Convert the time to a float
    hours, minutes = x[:-2].split(":")
    minutes = float(minutes)* (5/3) #Convert the minutes to a decimal value
    if x[-2:] == "pm" and hours != "12": #If the time is in PM and not 12, add 12 to the hours
        hours = str(int(hours) + 12)
    elif x[-2:] == "am" and hours == "12": #If the time is in AM and is 12, set the hours to 0
        hours = "0"
    return float(hours) + minutes
main()