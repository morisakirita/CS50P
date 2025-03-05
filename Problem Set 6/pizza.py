"""
Regular Pizza,Small,Large
Cheese,$13.50,$18.95
1 topping,$14.75,$20.95
2 toppings,$15.95,$22.95
3 toppings,$16.95,$24.95
Special,$18.50,$26.95
"""

import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")


def main():
    if is_csv(sys.argv[1]):
        menu = get_menu(sys.argv[1])
    else:
        sys.exit("Not a CSV file")

    print(tabulate_menu(menu))


def is_csv(file):
    extension = file.split(".")
    return extension[-1] == "csv"


def get_menu(f):
    items = []
    try:
        with open(f) as file:
            menu = csv.reader(file)
            for row in menu:
                items.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    return items


def tabulate_menu(menu):
    return tabulate(menu[1:], headers=menu[0], tablefmt="grid")


if __name__ == "__main__":
    main()
