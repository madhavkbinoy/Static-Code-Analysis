

import json
from datetime import datetime


"""Inventory system for managing stock data with validation and file I/O."""

stock_data = {}


def add_item(item_name, quantity):
    """Add the given quantity of an item to the stock."""
    if not isinstance(item_name, str):
        print("Invalid item name type: int. Expected string.")
        return
    if not isinstance(quantity, int):
        print("Invalid quantity type. Expected integer.")
        return

    stock_data[item_name] = stock_data.get(item_name, 0) + quantity


def remove_item(item_name, quantity):
    """Remove the given quantity of an item from the stock."""
    if not isinstance(item_name, str):
        print("Invalid item name type: int. Expected string.")
        return
    if not isinstance(quantity, int):
        print("Invalid quantity type. Expected integer.")
        return

    if item_name not in stock_data:
        print(f"Item '{item_name}' not found in stock data.")
        return
    stock_data[item_name] -= quantity


def get_qty(item_name):
    """Return the quantity of a given item."""
    return stock_data.get(item_name, 0)


def load_data():
    """Load stock data from file."""
    data = {}
    try:
        with open("stock_data.txt", "r", encoding="utf-8") as file:
            for line in file:
                item, qty = line.strip().split(",")
                data[item] = int(qty)
    except FileNotFoundError:
        data = {}
    return data


def save_data(data):
    """Save stock data to file."""
    with open("stock_data.txt", "w", encoding="utf-8") as file:
        for item, qty in data.items():
            file.write(f"{item},{qty}\n")


def print_data():
    """Print all items in stock."""
    print("\nItems Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items():
    """Print items with quantity below 5."""
    low_items = [item for item, qty in stock_data.items() if qty < 5]
    print(f"Low items: {low_items}")


if __name__ == "__main__":
    stock_data = load_data()
    add_item("apple", 10)
    add_item("banana", 3)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 5)
    print(f"Apple stock: {get_qty('apple')}")
    check_low_items()
    print_data()
    save_data(stock_data)
    print("eval used")
