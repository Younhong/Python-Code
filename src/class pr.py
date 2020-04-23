class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def deposit(self, balance):
        self.balance += balance
    def __add__(self, amount):
        self.deposit(amount)
    def withdraw(self, balance):
        self.balance -= balance
    def __sub__(self, amount):
        self.withdraw(amount)
    def __str__(self):
        return "%s has balance %d"%(self.name, self.balance)
myAccount = BankAccount("Smith")
myAccount + 10000
print(myAccount)
myAccount - 3000
print(myAccount)