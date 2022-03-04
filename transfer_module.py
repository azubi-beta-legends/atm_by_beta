# Python 3.10.1
# Coding: utf-8
# transfer money

import json # to write data onto the json file > update
import jsonHandler # reads the data
import login 

currentUser = login.user_login()
userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\confidential\userinfo.json')

def transferFunds():
    while True:
        transaction = input("Select: 1 to Withdraw...2 to Deposit...3 to Transfer\n")

        if transaction == '3':
            print("You can transfer up to {:.2f}".format(1000/3))
            transferTo = input("Enter account number to transfer to:\n")

            if transferTo in userData.keys():
                transferAmount = int(input('Enter transfer amount:\n'))
                k = (userData[currentUser]['balance']['KSH'])

                if 0 < transferAmount < k and (userData[currentUser]['balance']['KSH']) > 100:
                    userData[currentUser]['balance']['KSH'] -= transferAmount
                    userData[transferTo]['balance']['KSH'] += transferAmount
                    print(f"Ksh.{transferAmount} sent to {userData[transferTo]['username']}. New balance is Ksh.",userData[currentUser]['balance']['KSH'])
                    with open(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\confidential\userinfo.json', 'w') as json_file2:
                        json.dump(userData, json_file2)
                    continue
                else:
                    print('You have insufficient funds to complete the transaction!')
                    transferFunds()
                    
            else:
                print('Invalid account. Try again')
                transferFunds()

        else:
            print('Would you like to deposit or withdraw? ')
            transferFunds()
    

transferFunds()