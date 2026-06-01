# Read File in Different Ways

# read full file
with open("sales_data.txt", "r") as file:
    print("using read():")
    print(file.read())

# read first line
with open("sales_data.txt", "r") as file:
    print("using readline():")
    print(file.readline())

# read all lines and convert to list of int
with open("sales_data.txt", "r") as file:
    lines = file.readlines()   
   # convert to int
    sales_list = []
for line in lines:
    sales_list.append(int(line.strip()))
    print("converted list:", sales_list)