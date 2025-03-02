'''
# plates.py
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
                break
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
'''

import pytest
import plates


def test_expected_plate():
    assert plates.is_valid('AAA202') == True


def test_starts_with_two_letters():
    assert plates.is_valid('a1') == False


def test_minimum_maximum_characters():
    assert plates.is_valid('a') == False
    assert plates.is_valid('aaaaaaaaaaaaaaaaaa') == False


def test_no_middle_numbers():
    assert plates.is_valid('aa1a') == False


def test_no_start_with_zero():
    assert plates.is_valid('aa01') == False


def test_no_special_characters():
    assert plates.is_valid('aa.a') == False


def test_pass_number():
    with pytest.raises(TypeError):
        plates.is_valid(1)
