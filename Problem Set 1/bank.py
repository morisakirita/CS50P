def main():
    greeting = input("Greeting: ").strip().lower()
    is_greeting(greeting)


def is_greeting(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
