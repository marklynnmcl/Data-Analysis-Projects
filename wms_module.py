# Inventory and Orders as lists with dictionaries
inventory = []
orders = []
buys= []

# Add inventory item
def add_inventory():
    item_id = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    quantity = int(input("Enter Quantity: "))
    location = input("Enter Storage Location: ")
    inventory.append({"item_id": item_id, "name": name, "quantity": quantity, "location": location})
    print(f"Item '{name}' added successfully.")

# View inventory
def view_inventory():
    if inventory:
        print("\nCurrent Inventory:")
        for item in inventory:
            print(f"ID: {item['item_id']}, Name: {item['name']}, Quantity: {item['quantity']}, Location: {item['location']}")
    else:
        print("\nInventory is empty.")

# Update inventory
def update_inventory():
    item_id = input("Enter Item ID to update: ")
    for item in inventory:
        if item["item_id"] == item_id:
            new_quantity = int(input(f"Enter new quantity for '{item['name']}': "))
            item["quantity"] = new_quantity
            print("Inventory updated successfully.")
            return
    print("Item not found.")

# Create order
def create_order():
    item_id = input("Enter Item ID for the order: ")
    for item in inventory:
        if item["item_id"] == item_id:
            order_quantity = int(input("Enter order quantity: "))
            if order_quantity <= item["quantity"]:
                orders.append({"item_id": item_id, "quantity": order_quantity})
                item["quantity"] -= order_quantity
                print("Order created successfully.")
            else:
                print("Insufficient stock.")
            return
    print("Item not found in inventory.")

# View orders
def view_orders():
    if orders:
        print("\nCurrent Orders:")
        for order in orders:
            print(f"Item ID: {order['item_id']}, Quantity: {order['quantity']}")
    else:
        print("\nNo orders found.")

# Purchase an item from supplier
def buy_item():
    item_id = input("Enter Item ID to add: ")
    for item in inventory:
        if item["item_id"] == item_id:
            additional_quantity = int(input(f"Enter quantity to add to '{item['name']}': "))
            buys.append({"item_id": item_id, "quantity": additional_quantity})
            item["quantity"] += additional_quantity
            print(f"Successfully added {additional_quantity} units to '{item['name']}'. New quantity: {item['quantity']}.")
            return
    print("Item not found in inventory.")


def view_buys():
    if buys:
        print("\nCurrent purchase orders:")
        for buy  in  buys:
            print(f"Item ID: {buy['item_id']}, Quantity: {buy['quantity']}")
    else:
        print("\nNo purchase orders found.")

def how_many_sold():
    item_id = input("Enter the Item ID to check total sales quantity: ")
    total_sold = 0  

    for order in orders:
        if order["item_id"] == item_id:  
            total_sold += order["quantity"]  
    print(total_sold)

def how_many_bought():
    item_id = input("Enter the Item ID to check total purchase quantity: ")
    total_buy = 0  

    for buy in buys:
        if buy["item_id"] == item_id:  
            total_buy += buy["quantity"]  
    print(total_buy)

def low_stock():
    threshold = int(input("Enter the threshold for low stock: "))
    for item in inventory:
        if item["quantity"] < threshold:
            print(f"ID: {item['item_id']}, Name: {item['name']}, Quantity: {item['quantity']} is less than the threshold")
        else:
            print("No items with low stock")

    
