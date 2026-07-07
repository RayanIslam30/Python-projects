#Code to output $0 when user inputs "hello", $20 when user inputs anything else starting with "h", and $100 otherwise

bank = input("Enter greeting: ") #prompt user for input

clean_bank = bank.lower().strip() #put the string in lowercase and remove any whitespace
#ifelse statement to check if the input is "hello", anything else starting with "h", and print "$0", "$20", or "$100" accordingly
if clean_bank == "hello":
    print("$0")
elif clean_bank.startswith("h"):
    print("$20")
else:
    print("$100")