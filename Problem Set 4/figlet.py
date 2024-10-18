import sys
import pyfiglet

def main():
    figlet = pyfiglet.Figlet()

    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid usage")

    if len(sys.argv) > 1:
        if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        else:
            figlet.setFont(font=sys.argv[2])

    s = input("Input: ")
    print(figlet.renderText(s))



if __name__ == "__main__":
    main()
