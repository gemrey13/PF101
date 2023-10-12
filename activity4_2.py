from activity4_1 import *

account_1 = BankAccount('Goku')
account_2 = BankAccount('Naruto')
account_3 = BankAccount('Baki')
account_4 = BankAccount('Inuyasha')
account_5 = BankAccount('Vegeta')
account_6 = BankAccount('Luffy')
account_7 = BankAccount('Zoro')
account_8 = BankAccount('Sanji')
account_9 = BankAccount('Brook')

account = [account_1, account_2, account_3, account_4, account_5, account_6, account_7, account_8, account_9]

run = True
login = False

while run:
    if login == False:
        print("""
            [1] Login
            [2] Create a BankAccount Account
            [3] Exit
        """)
        choice = input("> ")
        if choice == '1':
            print("""
                Please Login....
                Enter account name
            """)
            account_name = str(input("> ")).title()
            for i in account:
                if account_name == i.account:
                    print(i.account , i)
                    print("Login Successfully")
                    current_account = i
                    login = True
                    continue
        elif choice == '2':
            print("""
                Please enter a account name.
            """)
            account_name = str(input("> ")).title()
            new_account = BankAccount(account_name)
            account.append(new_account)
            print(f"""
                Created Succesfully for {account_name}.
            """)
            continue
        elif choice == '3':
            print("""
                Exiting Program....
            """)
            run = False
        else:
            print("Invalid Choice")
            continue

    elif login == True:      
        print("""
            [1] Withdraw
            [2] Deposit
            [3] Check Balance
            [4] Logout
        """)
        choice = input('> ')
        if choice == '1':
            print("""
                Please enter a amount.
            """)
            amount = float(input("> "))
            current_account.withdraw(amount)
            continue
        elif choice == '2':
            print("""
                Please enter a amount.
            """)
            amount = float(input("> "))
            current_account.deposit(amount)
        elif choice == '3':
            current_account.check_balance()
        elif choice == '4':
            login = False
            print("Logging out...")
            continue
        else:
            print("Invalid Choice")
            continue
