def main():
    get_tacos("Item: ")


def get_tacos(prompt):
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    order = 0
    while True:
        try:
            item = input(prompt).title().strip()
            try:
                order = order + menu.get(item)
            except TypeError:
                continue
            print(f"Total: ${order:.2f}")
        except EOFError:
            break
    print()


if __name__ == "__main__":
    main()
