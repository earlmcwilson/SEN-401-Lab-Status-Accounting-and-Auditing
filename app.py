from inventory import items
from utils.helper import highest_stock_item, lowest_stock_item, total_stock_value, print_inventory, add_stock

def main() -> None:
    menu = (
        "\n=== Inventory Menu ===\n"
        "1. View Inventory\n"
        "2. Add Stock\n"
        "3. View Highest Stock Item\n"
        "4. View Lowest Stock Item\n"
        "5. Total stock value\n"
        "6. Exit\n"
    )
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            print()
            print_inventory(items)
        elif choice == "2":
            print()
            add_stock(items)
        elif choice == "3":
            print()
            if not items:
                print("Inventory is empty — nothing to compare.")
            else:
                highest = highest_stock_item(items)
                print(f"Highest Stock Item: {highest['item_name']} ({highest['quantity']} units)")
        elif choice == "4":
            print()
            if not items:
                print("Inventory is empty — nothing to compare.")
            else:
                lowest = lowest_stock_item(items)
                print(f"Lowest Stock Item: {lowest['item_name']} ({lowest['quantity']} units)")
        elif choice == "5":
            print()
            total = total_stock_value(items)
            print(f"Total Stock value is ${total}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, 5 or 6.")
 
 
if __name__ == "__main__":
    main()
 

