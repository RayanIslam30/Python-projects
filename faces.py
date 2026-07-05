#Code to take user input and convert :) and :( into emojis

#Main function to prompt user for input and call convert function
def main():
    # Prompt the user for input
    user_input = input("Please enter a string: ")
    
    # Call convert function to convert 
    converted_input = convert(user_input)
    print(converted_input)

# Convert :) and :( to their corresponding emojis
def convert(input): 
    converted_input = input.replace(":)", "🙂")
    converted_input = converted_input.replace(":(", "🙁")
    return converted_input

main()
