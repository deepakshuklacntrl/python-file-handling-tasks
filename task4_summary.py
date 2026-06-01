# summary report from file

# read file
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

# convert to int
sales = []
for line in lines:
    sales.append(int(line.strip()))

# calculations
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

# print results
print("total sales:", total_sales)
print("highest sal:", highest_sale)
print("lowest sale:", lowest_sale)
print("average sale:", average_sale)