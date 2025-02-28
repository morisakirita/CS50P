def main():
    twitter = input('Input: ').strip()
    twitter = shorten(twitter)
    print(twitter)


def shorten(word):
    twttr = ('a', 'e', 'i', 'o', 'u')
    for w in word:
        if w.lower() in twttr:
            word = word.replace(w, '')
    return word


if __name__ == "__main__":
    main()
