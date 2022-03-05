# Python 3.10.1
# Coding: utf-8
# this is include the entire execution

import ATM_transaction
import login
import jsonHandler

userData = jsonHandler.readJsonFile(r'C:\Users\Pascal Habineza\Desktop\AWS Azubi\azubiCodes\ATM_BETA\userinfo.json')

userId = login.user_login(userData)
print("select a number corresponding to the currency you would like to use:\n(1) KSH\n(2) USD")
currencyChoice=int(input())
currency=''

if currencyChoice == 1:
    currency = 'KSH'
elif currencyChoice==2:
    currency = 'USD'
else:
    print("Error1, Illegal input currency")

ATM_transaction.choose_transaction(userData, userId, currency)