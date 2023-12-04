class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder
        self._balance = balance

    def get_balance(self):
        return self._balance


    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposit: ${amount}. New Balance: {self._balance}")
        else:
            print("Invalid Deposit Amount. Please deposit a positive amount")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdraw: ${amount}. New Balance: ${self._balance}")
        else:
            print("Invalid Withdrawal amount or insufficient funds")

if __name__ == "__main__":
    account1 = BankAccount("John Doe", 1000)
    account2 = BankAccount("Jane Doe")

print(f"{account1._account_holder}'s balace: ${account1.get_balance()}")
print(f"{account2._account_holder}'s balace: ${account2.get_balance()}")

account1.deposit(500)
account2.withdraw(200)

print(f"{account1._account_holder}'s final balace: ${account1.get_balance()}")
print(f"{account2._account_holder}'s final balace: ${account2.get_balance()}")