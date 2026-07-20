# Code that uses a premade validator to check if an email is valid

from validator_collection import is_email  # From the validator_collection module, import a checker for valid email

def main():
    print(email(input("What's your email address? ")))

def email(email):
    if is_email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
