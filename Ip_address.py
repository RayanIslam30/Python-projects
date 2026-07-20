# Code that checks if a IP address is valid or invalid

import re  # Import re to check for validity


def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))


def validate(ip):
    if re.search(
        r"^\d+\.\d+\.\d+\.\d+$", ip
    ):  # Checks that ip address is formatted right, and numbers are where we expect
        parts = ip.split(".")  # Split our string into number parts
        for part in parts:
            number = int(part)
            if not (0 <= number <= 255):  # Check that each number is valid
                return "Invalid"  # Not valid numbers, invalid
        return "Valid"  # If ip address is valid format and numbers, valid
    else:  # If ip address formatted wrong, invalid
        return "Invalid"


if __name__ == "__main__":  # Only run file if called directly, so that we can run tests
    main()
