def main():
    grocery()


def grocery():
    grocery = {}
    quantity = 0

    while True:
        try:
            item = input().upper().strip()
            quantity = grocery[item] + 1
            grocery.update({item: quantity})
        except KeyError:
            grocery.update({item: 1})
        except EOFError:
            break

    grocery_order = sorted(grocery)
    for item in grocery_order:
        print(grocery[item], item)


if __name__ == "__main__":
    main()
