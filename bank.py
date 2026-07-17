#Code to output $0 when user inputs a string starting with "hello", $20 when user inputs anything else starting with "h", and $100 otherwise

def main():
    bank = input("Enter greeting: ").lower().strip() #prompt user for input, put in lowercase and remove whitespace
    amount = value(bank)
    print(f"${amount}")

#ifelse statement to check if the input starts with "hello", anything else starting with "h", and print "$0", "$20", or "$100" accordingly
def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__": #Only run main if file ran directly
    main()