# Code to determine if user input a string that ends with a common file extension, and print the corresponding file type
file_input = input("Enter a file name: ")  # prompt user for input
clean_file_input = (
    file_input.lower().strip()
)  # put the string in lowercase and remove any whitespace
# ifelse statement to check if the input ends with a common file extension, and print the corresponding file type accordingly
if clean_file_input.endswith(".txt"):
    print("text/plain")
elif clean_file_input.endswith(".jpg") or clean_file_input.endswith(".jpeg"):
    print("image/jpeg")
elif clean_file_input.endswith(".png"):
    print("image/png")
elif clean_file_input.endswith(".gif"):
    print("image/gif")
elif clean_file_input.endswith(".pdf"):
    print("application/pdf")
elif clean_file_input.endswith(".doc") or clean_file_input.endswith(".docx"):
    print("application/msword")
elif clean_file_input.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
