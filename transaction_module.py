# Python 3.10.1
# Coding: utf-8
# transactions


import json
import datetime
import jsonHandler


date = datetime.datetime.now()
# userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\atm_by_beta-babyRwanda-patch-Transactions1\userinfo.json')
newBalance = 0
exchangeRate = 113.00


#Withdrawing
def withdraw(userData, currentUserId, currency):
    #store the current balance of the current user
    currentBalance = userData[currentUserId]['balance'][currency]
    print(f"Your balance: {currentBalance}")
    moneyToWithdraw = int(input('Enter withdrwal amount (must be less than balance): '))
    count = 0
    #if 3 attemps failed, go backto choose transaction

    if moneyToWithdraw >= currentBalance:
        print("Enter withdrwal amount (must be less than balance): ")
        moneyToWithdraw = float(input())
        count += 1      #count number of attempts
    elif 0<moneyToWithdraw<currentBalance:
        print("Withdrawal intiated",".",".",".","Withdrawal complete")
        newBalance = currentBalance - moneyToWithdraw
        userData[currentUserId]['balance'][currency] = newBalance
     
        jsonHandler.updateData('userinfo.json', userData)
                
        #receipt 
        print("Would you like a receipt? (Y/N): ")
        answer = input()
        answer = answer.upper()

        if answer=='Y':
            print(f"\nWithdral Successful!\nThank you for choosing BETA BANK\n\
********************************\n\nDate: {date}\nAmount Withdrawn: {currency}. {moneyToWithdraw}\nBalance: {newBalance}\n\
********************************")                    
        else:
            print("Withdrawal Successful! Thank you for choosing BETA BANK!")


#depositing
def deposit(userData, currentUserId, currency): 
    #store the current balance of the current user
    currentBalance = userData[currentUserId]['balance'][currency]
    
    print(f"Your current balance is {currentBalance}")
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
            print(f"Deposit was successful!\n\
                Thank you for choosing BETA BANK\n*****************************\n\
                    \nDate: {date}\nDeposited Money:{moneyToDeposit}\n\
                        Balance: {newBalance}")
        else:
            print("Deposit Successful! Thank you for choosing BETA BANK.")
    
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
                    print(f"Transfer Successful!\nThank you for choosing BETA BANK\n*****************************\n\n\
                        Date: {date}\nTransferred {transferAmount} to {userData[transferTo]['username']}\n\
                        Balance: {userData[currentUserId]['balance']['KSH']}\n")
                else:
                    print("Transfer Successful! Thank you for choosing BETA BANK.")
                
            else:
                print('You have insufficient funds to complete the transaction!')
                transfer()

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
                    print(f"Transfer Successful!\n\
                            Thank you for choosing BETA BANK\n*****************************\n\
                            \nDate: {date}\nTransferred {transferAmount} to {userData[transferTo]['username']}\n\
                            Balance: {userData[currentUserId]['balance']['USD']}")
                else:
                    print("Transfer Successful! Thank you for choosing BETA BANK.")

            else:
                print('You have insufficient funds to complete the transaction!')
                        
        else:
            print('Invalid account. Try again')
    except IOError:
        print('Kindly input the correct information!')
