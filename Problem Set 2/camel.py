def main():
    camel_case = input("camelCase: ")
    snake_case_converter(camel_case)


def snake_case_converter(c):
    for letter in c:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")
    print()


if __name__ == "__main__":
    main()
