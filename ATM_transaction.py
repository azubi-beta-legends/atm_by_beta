#Python 3.10.2
#Azubi 1st project assignment. mimic ATM operations
#transactions


import datetime
import json


date = datetime.datetime.now()

#choose deposit, transfer, withdraw or quit
def choose_transaction(userData, currentUserId, currency):
    choice=-1
    while (choice != 1 or choice !=2 or choice !=3 or choice !=0):
        print("Choose a number corresponding to an action you want to perform:")
        print("(1) Withdraw\n (2) Deposit\n (3) Transfer\n (0) Quit")
        choice=int(input())
    if (choice==1):
        withdraw(userData, currentUserId, currency)
    elif choice==2:
        deposit(userData, currentUserId, currency)
    elif choice==3:
        transfer(userData, currentUserId, currency)
    else:
        exit

#Withdrawing
def withdraw(userData, currentUserId, currency):
    
    #store the current balance of the current user
    currentBalance = userData[currentUserId]['balance'][currency]
    
    print("Withdrawing intiated...")
    print(f"Your balance: {currentBalance}")
    
    moneyToWithdraw = currentBalance + 1
    count = 0
    
    while (moneyToWithdraw >= currentBalance):
        print("Enter amount of money you would like to withdraw (the money should be\
            less than your balance): ")
        moneyToWithdraw = float(input())
        
        count += 1 #count number of attempts
        if count==3 and moneyToWithdraw >= currentBalance:
            break
     
     #if 3 attemps failed, go backto choose transaction   
    if count == 3 and moneyToWithdraw >= currentBalance:
        choose_transaction(userData, currentUserId, currency)
        
    else: #updating the balance
        currentBalance = currentBalance - moneyToWithdraw
        userData[currentUserId]['balance'][currency] = currentBalance
        updateData('userinfo.json', userData)
        
        #receipt 
        print("Would you like a receipt? (Y/N): ")
        answer = input()
        answer = answer.upper()
        if answer=='Y':
            print(f"Withdrawing transaction was successful!\n\
                Thank you for using ATM BETA\n*****************************\n\
                \nDate: {date}\nWithdrawn Money:{moneyToWithdraw}\n\
                    Balance: {currentBalance}")
            choose_transaction(userData, currentUserId, currency)
            
        else:
            print("Withdrawing transaction was successful! Thank you for using ATM BETA.")
            choose_transaction(userData, currentUserId, currency)

#depositing
def deposit(userData, currentUserId, currency):
    
    #store the current balance of the current user
    currentBalance = userData[currentUserId]['balance'][currency]
    
    print("Depositing initiated...")
    print(f"Your current balance is {currentBalance}")
    moneyToDeposit = float(input("Enter the amount of money you would like to deposit: "))
    currentBalance = currentBalance + moneyToDeposit
    userData[currentUserId]['balance'][currency] = currentBalance
    updateData('userinfo.json', userData)
    
    #receipt
    print("Would you like a receipt? (Y/N): ")
    answer = input()
    answer = answer.upper()
    if answer=='Y':
        print(f"Depositing transaction was successful!\n\
            Thank you for using ATM BETA\n*****************************\n\
                \nDate: {date}\nDeposited Money:{moneyToDeposit}\n\
                    Balance: {currentBalance}")
        choose_transaction(userData, currentUserId, currency)
    else:
        print("Depositing transaction was successful! Thank you for using ATM BETA.")
        choose_transaction(userData, currentUserId, currency)
        
#transfering
def transfer(userData, currentUserId, currency):
    #TODO
    currentBalance = userData[currentUserId]['balance'][currency]

#updating the user data in the json file
def updateData(dataFileJson, userData ):
    with open(dataFileJson, 'w') as json_file2:
        json.dump(userData, json_file2)
    





