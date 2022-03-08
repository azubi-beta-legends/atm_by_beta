# Python 3.10.1
# Coding: utf-8
# this includes the main execution


import jsonHandler          # this is used to read user data from json file
import login_module         # this prompts the user for the username and password
import choice_module        # this prompts the user to select the currency type and transaction type
import transaction_module   # this executes the transactions: such as deposit, withdraw or transfer
import sys                  # the exit method from this module is used to exit the program


# userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json')
# currentUserId = login_module.user_login()


def atm_execution(data, user):
    while True:
            transaction = choice_module.choose_transaction()

            currency = choice_module.choose_currency()

            if (transaction=='1'):
                try:
                    transaction_module.withdraw(data, user, currency)
                except ValueError:
                    print('Enter a number')
                    transaction_module.withdraw(data, user, currency)
                    # break
            elif transaction=='2':
                try:
                    transaction_module.deposit(data, user, currency)
                    # break
                except ValueError:
                    print('Enter a number')
                    transaction_module.deposit(data, user, currency)
            elif transaction=='3':
                try:
                    transaction_module.transfer(data, user, currency)
                except ValueError:
                    print('Enter a number')
                    transaction_module.transfer()
                    # break
            elif transaction=='0':
                entire_execution()
            elif transaction == 'q':
                sys.exit()


def entire_execution():
    userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json')
    currentUserId = login_module.user_login()
    while True:
        try:
            atm_execution(userData, currentUserId)
        except ValueError and TypeError:
            atm_execution(userData, currentUserId)

entire_execution()