# create Product Info File (user input)

# Take input
products = []

for i in range(3):
    name = input("Enter product name: ")
    price = input("Enter price: ")
    products.append((name, price))

# Write to file
with open("products.txt", "w") as file:
    for name, price in products:
        file.write(name + " | " + price + "\n")

# Read and print formatted output
print("\nProduct List:")

with open("products.txt", "r") as file:
    for line in file:
        parts = line.strip().split("|")
        name = parts[0].strip()
        price = parts[1].strip()

        print(f"Product: {name}  ->  Price: ₹{price}")