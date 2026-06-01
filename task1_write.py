# TASK 1: Write Sales Data
# Write Sales Records

sales = [1200, 450, 980, 1500, 3000]

# write data to file
with open("sales_data.txt","w") as file:
 for s in sales:
  file.write(str(s) + "\n")

# reopen and print
with open("sales_data.txt", "r") as file:
 print("file content:")
 print(file.read())