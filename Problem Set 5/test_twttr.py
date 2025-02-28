'''
In the twttr.py file

def main():
    twitter = input("Input: ").strip()
    twitter = shorten(twitter)
    print(twitter)


def shorten(word):
    twttr = ("a", "e", "i", "o", "u")
    for w in word:
        if w.lower() in twttr:
            word = word.replace(w, "")
    return word


if __name__ == "__main__":
    main()
'''

from twttr import shorten


def test_lower():
    assert shorten('twitter') == 'twttr'


def test_upper():
    assert shorten('TWITTER') == 'TWTTR'


def test_blank():
    assert shorten('') == ''


def test_punctuation():
    assert shorten('TWi.tter!w') == 'TW.ttr!w'


def test_number():
    assert shorten('1') == '1'
