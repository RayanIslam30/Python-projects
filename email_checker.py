# Code that uses a premade validator to check if an email is valid

from validator_collection import is_email  # From the validator_collection module, import a checker for valid email

def main():
    print(email(input("What's your email address? ")))

#Use is_email to check for a valid email format (not necessarily real email, but right formatting)
def email(email):
    if is_email(email): #If true, valid
        return "Valid" 
    else: #If false, invalid
        return "Invalid"

if __name__ == "__main__":
    main()
