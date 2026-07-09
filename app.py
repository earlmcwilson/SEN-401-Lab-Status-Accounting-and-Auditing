from inventory import items
from utils.helper import highest_stock_item, lowest_stock_item, total_stock_value

def main():
    total_value = total_stock_value(items)
    print(f"\nTotal Stock Value: ${total_value:,.2f}")
 
    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)

 
    print(f"\nHighest Stock Item: {highest['item_name']} ({highest['quantity']} units)")
    print(f"Lowest Stock Item:  {lowest['item_name']} ({lowest['quantity']} units)")
 
 
if __name__ == "__main__":
    main()
 

