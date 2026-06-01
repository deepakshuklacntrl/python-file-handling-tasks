# read file safely(error handling inside file handling only)
# safe file reading

import os
filename = input("enter filename to open:")

# check if file exists
if os.path.exists(filename):
    with open(filename, "r") as file:
        print("\nfile content:\n")
        print(file.read())
else:
    print("file not found. please check the filename.")