def main():
    expression = input("Expression: ").strip()
    expression = get_expression(expression)
    x = float(expression[0])
    y = float(expression[-1])
    match expression[1]:
        case "+":
            print(f"{x + y}")
        case "-":
            print(f"{x - y}")
        case "*":
            print(f"{x * y}")
        case "/":
            print(f"{x / y}")


def get_expression(ex):
    return ex.split(" ")


main()
