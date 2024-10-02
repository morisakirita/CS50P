def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()
        except EOFError:
            print()
            break

        if "/" in date:
            date = date.split("/")
            try:
                month = int(date[0])
            except ValueError:
                pass
        elif "," in date:
            date = date.replace(",", "").split(" ")
            try:
                month = months.index(date[0]) + 1
            except ValueError:
                pass

        try:
            if month < 13:
                day = int(date[1])
                if day < 32:
                    year = int(date[2])
                    print(f"{year}-{month:02d}-{day:02d}")
                    break
        except UnboundLocalError:
            pass


if __name__ == "__main__":
    main()
