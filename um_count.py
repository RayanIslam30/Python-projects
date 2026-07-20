#Code to count the amount of times 'um' shows up in a string

import re

def main(): 
    print(count(input("Text: ")))

def count(str):
    matches = re.findall(r"\bum\b", str, re.IGNORECASE) #Finds only the word 'um' in the string, not as part of another word
    return len(matches)

if __name__ == "__main__":
    main()