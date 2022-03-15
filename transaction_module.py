# Python 3.10.1
# Coding: utf-8
# transactions


import json
import datetime
import jsonHandler
import check_type_module


date = datetime.datetime.now()
newBalance = 0
exchangeRate = 113.00


#Withdrawing
def withdraw(userData, currentUserId, currency):
    #store the current balance of the current user
    currentBalance = userData[currentUserId]['balance'][currency]
    print("Your current balance is {}.{:.2f}".format(currency,currentBalance))
    moneyToWithdraw = currentBalance + 1
    # moneyToWithdraw = float(input('Enter withdrwal amount (must be less than balance): '))
    count = 0
    #if 3 attemps failed, go backto choose transaction

    while moneyToWithdraw >= currentBalance and count < 3:
        moneyToWithdraw = float(input('Enter withdrwal amount (must be less than balance): '))
        count += 1      #count number of attempts
    if 0<moneyToWithdraw<currentBalance:
        print("Withdrawal intiated",".",".",".","Withdrawal complete")
        newBalance = currentBalance - moneyToWithdraw
        userData[currentUserId]['balance'][currency] = newBalance
     
        jsonHandler.updateData('userinfo.json', userData)
                
        #receipt 
        print("Would you like a receipt? (Y/N): ")
        answer = input()
        answer = answer.upper()

        if answer=='Y':
            print("\nWithdral Successful!\nThank you for choosing BETA BANK\n\
********************************\n\nDate: {}\nAmount Withdrawn: {}. {}\nBalance: {}. {:.2f}\n\
********************************".format(date, currency.lower(), moneyToWithdraw, currency.lower(), newBalance))                    
        else:
            print("Withdrawal Successful! Thank you for choosing BETA BANK!")
        jsonHandler.loguserData(currentUserId, date, 'Withdrawal', moneyToWithdraw, 'N/A', currentBalance, newBalance)
        jsonHandler.logallData('Transaction_logs.csv', currentUserId, date, 'Withdrawal', moneyToWithdraw, 'N/A', currentBalance, newBalance)


#depositing
def deposit(userData, currentUserId, currency): 
    #store the current balance of the current user
    currentBalance = userData[currentUserId]['balance'][currency]
    
    print("Your current balance is {}.{:.2f}".format(currency,currentBalance))
    moneyToDeposit = float(input("Enter the amount of money you would like to deposit: "))
    if moneyToDeposit > 0:
        print("Deposit intiated...")
        newBalance = currentBalance + moneyToDeposit
        userData[currentUserId]['balance'][currency] = newBalance
        jsonHandler.updateData('userinfo.json', userData)

        #receipt
        print("Would you like a receipt? (Y/N): ")
        answer = input()
        answer = answer.upper()
        if answer=='Y':
            print("\nDeposit Successful!\nThank you for choosing BETA BANK\n\
********************************\n\nDate: {}\nAmount Deposited: {}. {:.2f}\nBalance: {}. {:.2f}\n\
********************************".format(date, currency.lower(), moneyToDeposit, currency.lower(), newBalance)) 
        else:
            print("Deposit Successful! Thank you for choosing BETA BANK.")
        jsonHandler.loguserData(currentUserId, date, 'Withdrawal', moneyToDeposit, 'N/A', currentBalance, newBalance)
        jsonHandler.logallData('Transaction_logs.csv', currentUserId, date, 'Withdrawal', moneyToDeposit, 'N/A', currentBalance, newBalance)
    
    else:
        print('Try again!')
    
    
def transfer(userData, currentUserId, currency):
    try:
        transferTo = input("Enter account number to transfer to: ")
        k = (userData[currentUserId]['balance']['KSH'])
        d = (userData[currentUserId]['balance']['USD'])

        if transferTo in userData.keys() and currency == 'KSH':
            transferAmount = float(input('Enter transfer amount: '))
                
            if 0 < transferAmount < k and k > 100:
                userData[currentUserId]['balance']['KSH'] -= transferAmount
                userData[transferTo]['balance']['KSH'] += transferAmount
                userData[currentUserId]['balance']['USD'] -= transferAmount/exchangeRate
                userData[transferTo]['balance']['USD'] += transferAmount/exchangeRate

                with open(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json', 'w') as json_file2:
                    json.dump(userData, json_file2)

                print("Would you like a receipt? (Y/N): ")
                answer = input()
                answer = answer.upper()

                if answer=='Y':
                    print("\nTransfer Successful!\nThank you for choosing BETA BANK\n\
********************************\n\nDate: {}\nTransferred Ksh. {:.2f} to {}\n\
Balance: Ksh. {:.2f}\n".format(date, transferAmount, userData[transferTo]['username'], userData[currentUserId]['balance']['KSH']))
                else:
                    print("Transfer Successful! Thank you for choosing BETA BANK.")
                jsonHandler.loguserData(currentUserId, date, 'Transfer', transferAmount, 'N/A', userData[currentUserId]['balance']['KSH'], newBalance)
                jsonHandler.logallData('Transaction_logs.csv', currentUserId, date, 'Transfer', transferAmount, transferTo, userData[currentUserId]['balance']['KSH'], newBalance)
                
            else:
                print('You have insufficient funds to complete the transaction!')
                transfer(userData, currentUserId, currency)

        elif transferTo in userData.keys() and currency == 'USD':
            transferAmount = float(input('Enter transfer amount: '))

            if 0 < transferAmount < d and d > 1 :
                userData[currentUserId]['balance']['USD'] -= transferAmount
                userData[transferTo]['balance']['USD'] += transferAmount
                userData[currentUserId]['balance']['KSH'] -= transferAmount * exchangeRate
                userData[transferTo]['balance']['KSH'] += transferAmount * exchangeRate
                    
                with open(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json', 'w') as json_file2:
                    json.dump(userData, json_file2)
                print("Would you like a receipt? (Y/N): ")
                answer = input()
                answer = answer.upper()
                if answer=='Y':
                    print("\nTransfer Successful!\nThank you for choosing BETA BANK\n\
********************************\n\nDate: {}\nTransferred ${:.2f} to {}\n\
Balance: ${:.2f}\n".format(date, transferAmount, userData[transferTo]['username'], userData[currentUserId]['balance']['USD']))
                else:
                    print("Transfer Successful! Thank you for choosing BETA BANK.")
                jsonHandler.loguserData(currentUserId, date, 'Transfer', transferAmount, 'N/A', userData[currentUserId]['balance']['USD'], newBalance)
                jsonHandler.logallData('Transaction_logs.csv', currentUserId, date, 'Transfer', transferAmount, transferTo, userData[currentUserId]['balance']['USD'], newBalance)

            else:
                print('You have insufficient funds to complete the transaction!')
                        
        else:
            print('Invalid account. Try again')
    except IOError:
        print('Kindly input the correct information!')
