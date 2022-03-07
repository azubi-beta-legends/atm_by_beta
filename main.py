# Python 3.10.1
# Coding: utf-8
# this is include the entire execution


import jsonHandler          # this is used to read user data from json file
import login_module         # this prompts the user for the username and password
import choice_module        # this prompts the user to select the currency type and transaction type
import transaction_module   # this executes the transactions: such as deposit, withdraw or transfer
import sys                  # the exit method from this module is used to exit the program


def atm_execution(userData, currentUserId, transaction, currency):
    while transaction != 1 or 2 or 3 or 0:
        transaction = choice_module.choose_transaction()
        if (transaction==1):
            transaction_module.withdraw(userData, currentUserId, currency)
            break
        elif transaction==2:
            transaction_module.deposit(userData, currentUserId, currency)
            break
        elif transaction==3:
            transaction_module.transfer(userData, currentUserId, currency)
            break
        elif transaction==0:
            sys.exit()
        else:
            transaction = choice_module.choose_transaction()
        # except ValueError:
        #     atm_execution(userData, currentUserId, transaction, currency)

    # userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json')
    # transaction = choice_module.choose_transaction()
    # # currency = choice_module.choose_currency()
    # atm_execution(userData, currentUserId, transaction, currency)


userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json')
currentUserId = login_module.user_login()

while True:
    if currentUserId != None:
        transaction = choice_module.choose_transaction()
        break
    else:
        currentUserId = login_module.user_login()

currency = choice_module.choose_currency()

atm_execution(userData, currentUserId, transaction, currency)