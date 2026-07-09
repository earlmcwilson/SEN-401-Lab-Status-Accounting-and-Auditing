
def highest_stock_item(stock: list[dict]):
    return max(stock, key=lambda item: item["quantity"])

def lowest_stock_item(stock: list[dict]):
    return min(stock, key=lambda item: item["quantity"])

def total_stock_value(stock: list[dict]):
    return sum(item["quantity"] * item["price"] for item in stock)

