# SEN-401-Lab-Status-Accounting-and-Auditing

A simple Python application for tracking inventory items and reporting key stock metrics — total stock value, highest-stock item, and lowest-stock item.

## Features

-  Maintain an inventory of items with name, quantity, and price
-  Calculate total stock value across all items
-  Identify the item with the highest stock quantity
-  Identify the item with the lowest stock quantity

## Project Structure

```
.
├── app.py              # Entry point — runs the stock report
├── inventory.py         # Inventory data (item name, quantity, price)
└── utils/
    └── helper.py         # Helper functions for stock calculations
```

## Usage

Run the application from the project root:

```bash
python app.py
```

### Sample Output

```
Total Stock Value: $310.00

Highest Stock Item: Cotton_wool (30 units)
Lowest Stock Item:  Wipes (10 units)
```

## How It Works

1. **`inventory.py`** defines a list of items, each represented as a dictionary with:
   - `item_name` — the name of the item
   - `quantity` — units currently in stock
   - `price` — price per unit

2. **`utils/helper.py`** provides three core functions:
   | Function | Description |
   |---|---|
   | `total_stock_value(stock)` | Returns the total value of all stock (`quantity × price`, summed) |
   | `highest_stock_item(stock)` | Returns the item dict with the highest `quantity` |
   | `lowest_stock_item(stock)` | Returns the item dict with the lowest `quantity` |

3. **`app.py`** imports the inventory and helper functions, computes the metrics, and prints a formatted report.

## Extending This Project

Some ideas for building on this foundation:
- Add functions for low-stock alerts (e.g., items below a reorder threshold)
- Load/save inventory data from a CSV or JSON file instead of a hardcoded list
- Add a `restock_item()` or `sell_item()` function to update quantities
- Write unit tests for the helper functions using `pytest`
- Add command-line arguments (e.g., `--sort-by price`) using `argparse`

## License

This project is free to use and modify for personal or educational purposes.