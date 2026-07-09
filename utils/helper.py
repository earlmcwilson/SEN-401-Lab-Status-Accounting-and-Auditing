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