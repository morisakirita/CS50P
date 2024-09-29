def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if starts_with_two_letters(s):
        if is_length_valid(s):
            if is_number_in_middle(s):
                if not_allowed(s):
                    return True
    else:
        return False


def starts_with_two_letters(s):
    return s[0:1].isalpha()


def is_length_valid(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def is_number_in_middle(s):
    plate_len = len(s)
    middle_plate = int(plate_len / 2)
    if s[-1].isalpha():
        if s[middle_plate-1].startswith("0"):
            return False
        else:
            for i in s[middle_plate:-1]:
                if i.isnumeric():
                    return False
                else:
                    return True
    else:
        if s[middle_plate].startswith("0"):
            return False
        else:
            return True


def not_allowed(s):
    return s.isalnum()


main()
