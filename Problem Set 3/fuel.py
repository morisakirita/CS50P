def main():
    fuel = get_fuel("Fraction: ")
    fuel = fuel * 100
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel:.0f}%")


def get_fuel(prompt):
    while True:
        fuel = input(prompt)
        fuel = fuel.split("/")
        try:
            x = int(fuel[0])
            y = int(fuel[1])
            if x > y:
                continue
            else:
                return x / y
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
