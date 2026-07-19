# Code to take a 24 or 12 hour time, and figure out if it is breakfast, lunch, dinner, or none
# Time must be inputted (X:XXam/pm or XX:XX) and will be converted to a float for comparison


def main():
    time = (
        input("What time is it? ").lower().strip()
    )  # Prompt the user for input and convert it to lowercase and remove whitespace
    if time.endswith("am") or time.endswith(
        "pm"
    ):  # Code to run if the time is in AM or PM format, convert to 24h format
        converted_time = convert12h(time)
    else:  # Code to run if the time is in 24h format, considered default
        converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
    else:
        pass  # If the time is not in any of the above ranges, do nothing


def convert(x):
    # Convert the time to a float
    hours, minutes = x.split(":")
    minutes = float(minutes) / 60  # Convert the minutes to a decimal value
    return float(hours) + minutes


def convert12h(x):
    # Convert the time to a float
    hours, minutes = x[:-2].split(":")
    minutes = float(minutes) / 60  # Convert the minutes to a decimal value
    if (
        x[-2:] == "pm" and hours != "12"
    ):  # If the time is in PM and not 12, add 12 to the hours
        hours = str(int(hours) + 12)
    elif (
        x[-2:] == "am" and hours == "12"
    ):  # If the time is in AM and is 12, set the hours to 0
        hours = "0"
    return float(hours) + minutes


if __name__ == "__main__":  # If the script is run directly, call the main function
    main()
