def main():
    deep = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    deep = deep.lower().replace("-", " ").strip()
    answer = ["forty two", "42"]

    if deep in answer:
        print("Yes")
    else:
        print("No")


main()

