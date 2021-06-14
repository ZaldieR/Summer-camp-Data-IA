class Budget():
    _transactions = []

    def show_transactions(self):
        for i in self._transactions:
            print(f"You received {i} euros")
        
    def add_transactions(self, transactions):
        self._transactions = self._transactions + transactions


def main():
    transactions = [1, 2, 3]
    wallet = Budget()
    wallet.add_transactions(transactions)
    wallet.show_transactions()


main()