def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_length_valid(s):
        if starts_with_two_letters(s):
            if numbers_only_end(s):
                if no_special_symbols(s):
                    return True
    return False


def is_length_valid(s):
    if 2 <= len(s) <= 6:
        return True
    return False


def starts_with_two_letters(s):
    for a in s[0:2]:
        if a.isalpha():
            continue
        else:
            return False
    return True



def numbers_only_end(s):
    for index, item in enumerate(s):
        if item.isnumeric():
            if item == '0':
                return False
            else:
                for j in s[index:]:
                    if j.isalpha():
                        return False
                    else:
                        continue
        else:
            continue

    return True


def no_special_symbols(s):
    for a in s:
        if a.isalnum():
            continue
        else:
            return False
    else:
        return True


if __name__ == "__main__":
    main()
