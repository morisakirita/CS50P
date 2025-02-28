'''
bank.py
def main():
    greeting = input('Greeting: ').strip().lower()
    money = value(greeting)
    print(f'${money}')


def value(greeting):
    if greeting.lower().startswith('hello'):
        return 0
    elif greeting.lower().startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
'''
from bank import value


def test_starts_with_hello():
    assert value('hello') == 0


def test_starts_with_only_h():
    assert value('hi') == 20


def test_starts_with_hello_sensitive():
    assert value('HELLO') == 0


def test_starts_with_only_h_sensitive():
    assert value('HIIII') == 20


def test_number():
    assert value('1') == 100


def test_symbol():
    assert value('#') == 100
