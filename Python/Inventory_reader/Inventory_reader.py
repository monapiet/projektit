import json
# Open the JSON file
with open('warehouse.JSON', 'r', encoding="utf-8") as f:
    inventory = json.load(f)

# Variable for the products
products = inventory["products"]

# Print headline
print(f"==============INVENTORY REPORT==============")
print(f"Low stock items (less than 5 units):")
# Loop the products and check if quantity under 5
for product in products:
    quantity = int(product["quantity"])
    id = product["product_id"]
    name = product["name"]
    if quantity < 5:
        print(f"{id} - {name} - {quantity}")

# Print emptyline
print("")

# Variable for the total value
total_value = 0
# Loop the products and count the total inventory value
for product in products:
    id = product["product_id"]
    name = product["name"]
    quantity = int(product["quantity"])
    price = product["unit_price"]
    # count the inventory value
    value_per_product = price * quantity
    total_value += value_per_product
    round_value = round(total_value, 2)
# Print the total value of the inventory
print(f"TOTAL INVENTORY VALUE:\n{round_value} €")
print("")

# Hedline for out of stock items
print(f"OUT OF STOCK ITEMS:")
# Loop products and find products out of stock (quantity = 0)
for product in products:
    id = product["product_id"]
    name = product["name"]
    quantity = int(product["quantity"])
    if quantity == 0:
        print(f"{id} - {name} - {quantity}")


# Function that counts the products in given category and the value of the products in given category
def count_total_quantity_and_value(products, target_category ):

    total_quantity = 0
    total_value = 0

    # Loop the products
    for product in products:
        category = product["category"]
        quantity = int(product["quantity"])
        price = float(product["unit_price"])

        if category == target_category:
            total_quantity += quantity
            total_value += quantity * price
    return total_quantity,  total_value

# List of categories to help me keep track of what categories exist in the dataset.
# This makes the code easier to read and understand while calling the function
category_list = []
for product in products:
    if product["category"] not in category_list:
        category_list.append(product["category"])

print("")
# Product quantities and values in different categories
# Print headline
print(f"QUANTITIES AND VALUES IN DIFFERENT CATEGORIES")
# Electronics
electronics_quantity, electronics_value = count_total_quantity_and_value(products, "Elektroniikka")
print(f"Electronics quantity: {electronics_quantity} pcs, Electronics value: {round(electronics_value, 2)} €")
# Food
food_quantity, food_value = count_total_quantity_and_value(products, "Ruoka")
print(f"Food quantity: {food_quantity} pcs, Food value: {round(food_value, 2)} €")
# Tools
tools_quantity, tools_value = count_total_quantity_and_value(products, "Työkalut")
print(f"Tools quantity: {tools_quantity} pcs, Tools value: {round(tools_value, 2)} €")
# Furniture
furniture_quantity, furniture_value = count_total_quantity_and_value(products, "Kalusteet")
print(f"Furniture quantity: {furniture_quantity} pcs, Furniture value: {round(furniture_value, 2)} €")
# Office
office_quantity, office_value = count_total_quantity_and_value(products, "Toimisto")
print(f"Office quantity: {office_quantity} pcs, Office value: {round(office_value, 2)} €")
# Hygiene
hygiene_quantity, hygiene_value = count_total_quantity_and_value(products, "Hygienia")
print(f"Hygiene quantity: {hygiene_quantity} pcs, Hygiene value: {round(hygiene_value, 2)} €")
# Outdoor_activities
outdoor_quantity, outdoor_value = count_total_quantity_and_value(products, "Ulkoilu")
print(f"Outdoor quantity: {outdoor_quantity} pcs, Outdoor value: {round(outdoor_value, 2)} €")






