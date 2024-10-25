import random


def main():
    x = []
    y = []
    level = get_level()
    for i in range(10):
        x.append(generate_integer(level))
        y.append(generate_integer(level))

    wrong = 0
    right = 0
    for i in range(10):
        while True:
            print(x[i], "+", y[i], "= ", end="")
            answer = int(input())
            if answer != x[i]+y[i] and wrong < 2:
                print("EEE")
                wrong += 1
            elif answer == x[i]+y[i]:
                right += 1
                break
            else:
                print(x[i]+y[i])
                break
    print("Score:", right)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            get_level()

        if level not in [1, 2, 3]:
            get_level()
        else:
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
