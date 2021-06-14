import json

class Budget():
    _transactions = []

    def __init__(self, path=""):
        self.path = path
        self.data = {}
        if self.path != "":
            with open(self.path, 'r') as f:
                self.data = json.load(f)

    def show_transactions(self, name):
        for i in self.data['transactions']:
            if name == i['category']:
                if i['value'] > 0:
                    print(f"You received {i['value']} euros")
                else:
                    print(f"You spend {i['value'] * -1} euros")
        
    def add_transactions(self, transactions):
        self._transactions = self._transactions + transactions

    def get_category(self):
        res = []
        for i in self.data['transactions']:
            res.append(i['category'])
        return res
    
    def consult_my_balance(self):
        res = 0
        for i in self.data['transactions']:
            res += i['value']
        print(f"Your balance is equal to {res} euros")
    
    def transactions_history(self):
        for i in self.data['transactions']:
            print(i['category'])
            if i['value'] > 0:
                print(f"You received {i['value']} euros")
            else:
                print(f"You spend {i['value'] * -1} euros")

    def add_new_transaction(self):
        print("Enter category name: ", end='')
        category = input()
        print("Enter value: ", end='')
        value = input()
        try:
            value = int(value)
        except:
            print("Bad value")
            return
        self.data['transactions'].append({'category':category, 'value':value})
        print(f"Transaction with Category:{category} and value:{value} added")
    
    def quit(self):
        with open('test.json', 'w') as f:
            json.dump(self.data, f)
        exit(0)

def main():
    wallet = Budget("test.json")
    while(1):
        print("Choose between :\n" +
        "1 - consult my balance\n" +
        "2 - add a new transaction\n" +
        "3 - consult your transactions history\n" +
        "4 - quit")
        ch = input()
        try:
            ch = int(ch)
        except:
            exit(84)
        if not ch > 0 and not ch < 5 :
            exit(0)
        if ch == 1:
            wallet.consult_my_balance()
        if ch == 2:
            wallet.add_new_transaction()
        if ch == 3:
            wallet.transactions_history()
        if ch == 4:
            wallet.quit()
        print('\n')
        
main()