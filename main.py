# Python 3.10.1
# Coding: utf-8
# this is include the entire execution


from msilib.schema import Error
import jsonHandler
import login_module
import choice_module
import transaction_module
import sys


def atm_execution(userData, currentUserId, transaction, currency):
    while True:
        try:
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
        except ValueError:
            sys.exit()
    userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json')
    transaction = choice_module.choose_transaction()
    currency = choice_module.choose_currency()
    atm_execution(userData, currentUserId, transaction, currency)


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