# Simple Warehouse Management System


from wms_module import *

# Main menu loop
def main():
    while True:
        print("\nWarehouse Management System")
        print("1. Add Inventory")
        print("2. Update Inventory")
        print("3. Create Order")
        print("4. Purchase Inventory")
        print("5. Reports")
        print("6. Exit")

        choice = input("Enter your choice: ")

        
        if choice == "1":
            add_inventory()
        elif choice == "2":
            update_inventory()
        elif choice == "3":
            create_order()
        elif choice == "4":
            buy_item()
        elif choice == "5":
            a= int ( input("What report are you requesting? \n0. View Inventory \n1. View Orders \n2. View Purchases \n3. Total Sales of Product \n4. Total Purchases of Product \n5. Check for Low Stock \nEnter your choice: "))
            if a==0 : 
                view_inventory()
            elif a==1 : 
                view_orders()
            elif a ==2 :
                view_buys()
            elif a==3 : 
                how_many_sold()
            elif a==4 :
                how_many_bought()
            elif a==5 : 
                low_stock()
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()

