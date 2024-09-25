def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    time = time.split(":")
    converted_time = float(time[0]) + float(time[-1])/60
    return converted_time


if __name__ == "__main__":
    main()
