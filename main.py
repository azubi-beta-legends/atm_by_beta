# Python 3.10.1
# Coding: utf-8
# this is include the entire execution

import jsonHandler
import login
import choice_module
import transaction_module

userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json')
currentUserId = login.user_login()
transaction = choice_module.choose_transaction()
currency = choice_module.choose_currency()



if (transaction==1):
    transaction_module.withdraw(userData, currentUserId, currency)
elif transaction==2:
    transaction_module.deposit(userData, currentUserId, currency)
elif transaction==3:
    transaction_module.transfer(userData, currentUserId, currency)
else:
    exit
