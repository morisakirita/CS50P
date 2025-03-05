import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not is_python_file(sys.argv[1]):
        sys.exit("Not a Python file")

    lines = read_lines(sys.argv[1])
    print(lines)


def is_python_file(file):
    extension = file.split(".")
    try:
        return extension[1].startswith("py")
    except:
        return False


def read_lines(f):
    count_lines = 0
    try:
        with open(f) as file:
            for line in file:
                if not is_comment(line.strip()):
                    count_lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return count_lines


def is_comment(line):
    if line.startswith("#"):
        return True
    elif len(line) == 0:
        return True

    return False


if __name__ == "__main__":
    main()
