import sys


def choose_transaction():
    transactionChoice=-1
    while (transactionChoice != '1' or transactionChoice !='2' or transactionChoice !='3' or transactionChoice !='0'):
        print("Choose a number corresponding to an action you want to perform:")
        print("(1) Withdraw\n(2) Deposit\n(3) Transfer\n(0) Log Out\n(q) Quit")
        choice = input()
        return choice


def choose_currency():
    currencyChoice = ''
    while (currencyChoice != '1' or currencyChoice != '2' or currencyChoice != '0'):
        currencyChoice = input('Choose 1 for KSH and 2 for USD. (q to quit, 1 to log out from previous step): ')
    
        if currencyChoice.lower() == 'q':
            sys.exit()
        elif currencyChoice == '1':
            return 'KSH'
        elif currencyChoice == '2':
            return 'USD'
            