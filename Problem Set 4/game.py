import sys
import random

def main():
    while True:
        level = get_level()
        if level < 1:
            continue
        random_num = get_random_number(level)
        guess = get_user_input()

        if guess < random_num:
            print("Too small!")
        elif guess > random_num:
            print("Too large!")
        else:
            sys.exit("Just right!")


def get_user_input():
    try:
        return int(input("Guess: "))
    except ValueError:
        get_user_input()


def get_level():
    try:
        return int(input("Level: "))
    except ValueError:
        get_level()


def get_random_number(level):
    return random.randint(1, level)


if __name__ == "__main__":
    main()
