# wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv
import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


def main():
    if is_csv(sys.argv[1]):
        students = get_csv()
    else:
        sys.exit("Could not read", sys.argv[2])

    set_csv(students)


def is_csv(file):
    extension = file.split(".")
    return extension[-1] == "csv"


def get_csv():
    students = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file, fieldnames=['name', 'house'])
        for student in reader:
            students.append(student)
    return students


def set_csv(students):
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

        writer.writeheader()
        for student in students[1:]:
            last, first = student["name"].split(",")
            writer.writerow({"first": first.strip(), "last": last.strip(), "house": student["house"]})


if __name__ == "__main__":
    main()
