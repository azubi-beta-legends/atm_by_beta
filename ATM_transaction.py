#Python 3.10.2
#Azubi 1st project assignment. mimic ATM operations
#transactions


import datetime
import json


date = datetime.datetime.now()

#choose deposit, transfer, withdraw or quit
def choose_transaction(userData, currentUserId, currency):
    choice=-1
    while (choice != 1 and choice !=2 and choice !=3 and choice !=0):
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
        print("Enter amount of money you would like to withdraw (the money should be less than your balance): ")
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
        updateCurrency(userData, currentUserId, currency, currentBalance)
        updateData(r'C:\Users\Pascal Habineza\Desktop\AWS Azubi\azubiCodes\ATM_BETA\userinfo.json', userData)
        
        #receipt 
        printReceipt(currentBalance, moneyToWithdraw, 'Withdrawn', currency)
        #choose again
        choose_transaction(userData, currentUserId, currency)
        

#depositing
def deposit(userData, currentUserId, currency):
    
    #store the current balance of the current user
    currentBalance = userData[currentUserId]['balance'][currency]
    
    print("Depositing initiated...")
    print(f"Your current balance is {currentBalance}{currency}")
    moneyToDeposit = float(input("Enter the amount of money you would like to deposit: "))
    
    currentBalance = currentBalance + moneyToDeposit
    userData[currentUserId]['balance'][currency] = currentBalance
    updateCurrency(userData, currentUserId, currency, currentBalance)
    updateData(r'C:\Users\Pascal Habineza\Desktop\AWS Azubi\azubiCodes\ATM_BETA\userinfo.json', userData)
    #receipt 
    printReceipt(currentBalance, moneyToDeposit, 'Deposited', currency)
    #choose again
    choose_transaction(userData, currentUserId, currency)
 
        
#transfering
def transfer(userData, currentUserId, currency):
    #TODO
    currentBalance = userData[currentUserId]['balance'][currency]

#updating the user data in the json file
def updateData(dataFileJson, userData ):
    with open(dataFileJson, 'w') as json_file2:
        json.dump(userData, json_file2)
 
        
#update another(unused) currency
def updateCurrency(userData, currentUserId, currency, currentBalance):
    if currency=='KSH':
        userData[currentUserId]['balance']['USD'] = currentBalance/113
    elif currency=='USD':
        userData[currentUserId]['balance']['KSH'] = currentBalance * 113
    else:
        print("Unknown Currency:: ERROR!")
        
        
#print a receipt
def printReceipt(currentBalance, moneyToTransact, transaction, currency):
    print("Would you like a receipt? (Y/N): ")
    answer = input()
    answer = answer.upper()
    if answer=='Y':
        print(f"\n\nThe transaction was successful!\n\
Thank you for using BETA ATM\n*****************************\n\
\nDate: {date}\n{transaction} Money:{moneyToTransact}{currency}\n\
Balance: {currentBalance}{currency}")     
        print()   
    else:
        print(f"{transaction} money in {currency} successfully! Thank you for using BETA ATM.")
        print()




