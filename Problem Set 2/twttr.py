def main():
    twitter = input("Input: ").strip()
    twttr(twitter)


def twttr(twitter):
    vowels = ["a", "e", "i", "o", "u"]
    for t in twitter:
        if not t.lower() in vowels:
            print(t, end="")
    print()


if __name__ == "__main__":
    main()
