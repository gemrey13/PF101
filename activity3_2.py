from activity3_1 import *

account_1 = Bank('Sanji')
account_2 = Bank('Zoro')


account_1.deposit(200)
account_2.deposit(250)

account_1.withdraw(200)
account_2.withdraw(200)

account_1.check_balance()
account_2.check_balance()