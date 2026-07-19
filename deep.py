# Code to say "Yes" when user inputs 42 or forty two, and "No" otherwise

deep = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)  # prompt user for input

clean_deep = (
    deep.lower().strip().replace("-", "").replace(" ", "")
)  # put the string in lowercase and remove any whitespace, and remove any dashes
# ifelse statement to check if the input is 42 or forty two, and print "Yes" or "No" accordingly
if clean_deep == "42" or clean_deep == "fortytwo" or clean_deep == "fourtytwo":
    print("Yes")
else:
    print("No")
