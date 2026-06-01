# mini project - export discounte prices

prices = {"mouse": 500, "keyboard": 800, "monitor": 7000,"pendrive": 400, "camera": 5000}

# take discount input
discount = float(input("enter discount percentage:"))

# write to file
with open("discount_report.txt", "w") as file:
    file.write("product | original price | discounted price\n")
    total_discounted = 0
    count = 0
    for product, price in prices.items():
        discounted_price = price - (price * discount / 100)
        file.write(f"{product} | {price} | {discounted_price}\n")
        total_discounted += discounted_price
        count += 1
        
# extra summary
    average = total_discounted / count
    file.write("\nsummary:\n")
    file.write(f"total items: {count}\n")
    file.write(f"average discounted price: {average}\n")

# read and print file 
print("\ndiscount report:\n")
with open("discount_report.txt", "r") as file:
    print(file.read())        