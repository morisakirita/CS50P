def main():
    coins_allowed = [25, 10, 5]
    amount = 0
    amount_due = 50
    while True:
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: ").strip())
        if coin in coins_allowed:
            amount = amount + coin
            amount_due = amount_due - coin
        else:
            continue
        if amount >= 50:
            amount = amount - 50
            print("Change Owed:", amount)
            break


if __name__ == "__main__":
    main()
