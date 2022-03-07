# Python 3.10.1
# Coding: utf-8
# this includes the main execution


import jsonHandler          # this is used to read user data from json file
import login_module         # this prompts the user for the username and password
import choice_module        # this prompts the user to select the currency type and transaction type
import transaction_module   # this executes the transactions: such as deposit, withdraw or transfer
import sys                  # the exit method from this module is used to exit the program


userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json')
currentUserId = login_module.user_login()


def atm_execution():
    while True:
        try:
            transaction = choice_module.choose_transaction()

            currency = choice_module.choose_currency()

            if (transaction=='1'):
                try:
                    transaction_module.withdraw(userData, currentUserId, currency)
                except ValueError:
                    print('Enter a number')
                    transaction_module.withdraw(userData, currentUserId, currency)
                    # break
            elif transaction=='2':
                try:
                    transaction_module.deposit(userData, currentUserId, currency)
                    # break
                except ValueError:
                    print('Enter a number')
                    transaction_module.deposit(userData, currentUserId, currency)
            elif transaction=='3':
                try:
                    transaction_module.transfer(userData, currentUserId, currency)
                except ValueError:
                    print('Enter a number')
                    transaction_module.transfer(userData, currentUserId, currency)
                    # break
            elif transaction=='0':
                atm_execution()
            else:
                transaction = choice_module.choose_transaction()
        except ValueError and TypeError:
            atm_execution()



while True:
    try:
        atm_execution()
    except ValueError and TypeError:
        atm_execution()