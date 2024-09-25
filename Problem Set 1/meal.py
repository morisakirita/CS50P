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
    hour = float(time[0])
    time = time[-1].split(" ")
    converted_time = hour + float(time[0])/60
    if "a.m." in time[-1]:
        return converted_time
    elif "p.m." in time[-1]:
        return converted_time + 12
    else:
        return converted_time


if __name__ == "__main__":
    main()
