class Bank:
    def __init__(self, account_name, balance= 0.0):
        self.account = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You Successfully Deposit money at amount of {amount} \nNew balance:{self.balance}")

        else:
            print("Invalid Transaction")

    def withdraw(self, amount):
        if 0 < amount <= self.balance :
            self.balance -= amount
            print(f" You Successfully Withdraw amount of {amount} \nNew balance:{self.balance}")

        else:
            print("Invalid Transaction")

    def check_balance(self):
        print(f"Account Name:{self.account} Current balance: {self.balance}")

