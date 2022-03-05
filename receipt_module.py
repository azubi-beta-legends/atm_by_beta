 #receipt

 def print_receipt():
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
        