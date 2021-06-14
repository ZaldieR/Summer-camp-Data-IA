import json

class Budget():
    _transactions = []

    def __init__(self, path=""):
        self.path = path
        self.data = {}

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
        if (self.path == ""):
            return
        with open(self.path, 'r') as f:
            self.data = json.load(f)
        for i in self.data['transactions']:
            res.append(i['category'])
        return res