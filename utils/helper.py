Item = dict[str, str | int | float]
def print_inventory(inventory: list[Item]) -> None:
    print(f"{'Item Name':<25}{'Quantity':>10}{'Price':>12}{'Value':>14}")
    print("-" * 61)
    if not inventory:
        print("(no items in inventory)")
    else:
        for item in inventory:
            value = item["quantity"] * item["price"]
            print(
                f"{item['item_name']:<25}{item['quantity']:>10}"
                f"{item['price']:>12.2f}{value:>14.2f}"
            )
    print("-" * 61)
    
def highest_stock_item(stock: list[dict]):
    if not stock:
        return None
    return max(stock, key=lambda item: item["quantity"])

def lowest_stock_item(stock: list[dict]):
    if not stock: 
        return None
    return min(stock, key=lambda item: item["quantity"])

def total_stock_value(stock: list[dict]):
    return sum(item["quantity"] * item["price"] for item in stock)

def add_stock(inventory: list[Item]) -> Item:
    name = input("Enter the name of the item to add: ").strip()
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a whole number for quantity.")
    while True:
        try:
            price = float(input("Enter the price: "))
            if price < 0:
                print("Price cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for price.")
    for item in inventory:
        if item["item_name"].lower() == name.lower():
            item["quantity"] += quantity
            item["price"] = price 
            print(f"Updated '{item['item_name']}': now {item['quantity']} units.")
            return item
    new_record: Item = {"item_name": name, "quantity": quantity, "price": price}
    inventory.append(new_record)
    print(f"Added '{name}': {quantity} units at ${price:.2f} each.")
    return new_record