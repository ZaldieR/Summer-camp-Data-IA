def show_transactions(transactions):
    for i in transactions:
        print(f"You received {i} euros")

def main():
    transactions = [1, 2, 3]
    show_transactions(transactions)


main()