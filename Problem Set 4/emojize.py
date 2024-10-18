import emoji

def main():
    uemoji = input("Input: ")
    uemoji = emoji.emojize(uemoji, language="alias")
    print("Output: " + uemoji)


if __name__ == "__main__":
    main()
