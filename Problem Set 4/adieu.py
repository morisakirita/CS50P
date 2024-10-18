import inflect

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            break

        names.append(name)

    adieu = p.join(names)
    print("Adieu, adieu, to", adieu)


if __name__ == "__main__":
    main()
