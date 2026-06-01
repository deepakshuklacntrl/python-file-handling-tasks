# Append New Sales

# append data
new_sales = [500, 2500, 1700]
with open("sales_data.txt", "a") as file:
    for s in new_sales:
        file.write(str(s) + "\n")

# read updated file
with open("sales_data.txt", "r") as file:
    data = file.readlines()
    print("updated file content:")
    print("".join(data))
    print("total lines:", len(data))        
