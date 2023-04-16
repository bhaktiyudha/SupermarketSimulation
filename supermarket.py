all_items = [{"item": "susu", "harga": 50000},
             {"item": "daging", "harga": 20000},
             {"item": "lampu", "harga": 15000},
             {"item": "masker", "harga": 25000},
             {"item": "apel", "harga": 30000}]

promotional_items = [{"item": "susu", "harga": 50000},
                     {"item": "masker", "harga": 25000}]

# Display greetings and promotional items
print("Welcome to our supermarket!")
print("We have some promotional items:")
for item in promotional_items:
    print("- {} (Rp.{})".format(item["item"], item["harga"]))

# Take user input
print("\nWhat would you like to see?")
print("1. Promotional items only")
print("2. All items")
choice = input("Enter your choice (1 or 2): ")

# Show items according to user request
if choice == "1":
    items = promotional_items
else:
    items = all_items

print("\nHere are the items we have:")
for item in items:
    print("- {} (Rp.{})".format(item["item"], item["harga"]))

# Take user input for buying items
print("\nWhat would you like to buy?")
items_to_buy = input("Enter the items you want to buy, separated by commas: ")
items_to_buy = [item.strip() for item in items_to_buy.split(",")]

# Initialize dictionary for keeping track of item quantity
item_qty = {}
for item in items_to_buy:
    item_qty[item] = 0

# Take user input for quantity of each item
for item in item_qty:
    qty = int(input("How many {} do you want to buy? ".format(item)))
    item_qty[item] = qty

# Calculate total price and display details
total_price = 0
print("\nHere are the details of your purchase:")
for item in items_to_buy:
    for product in items:
        if product["item"] == item:
            qty = item_qty[item]
            price = product["harga"]
            item_price = qty * price
            total_price += item_price
            print("- {} (Rp.{}) x {} = Rp.{}".format(item, price, qty, item_price))
            break

print("\nTotal harga: Rp.{}".format(total_price))
