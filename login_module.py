# Python 3.10.1
# Coding: utf-8
# user login attempts


# from tkinter import W
import jsonHandler
import getpass
import stdiomask
import sys


userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\confidential\userinfo.json')
# print(userData)
# countAttempts = 0


def user_login():
	print("\n" + "*" * 30)
	print("**" + " " * 26 + "**")
	print("* Welcome to BETA ATM SYSTEM *")
	print("**" + " " * 26 + "**")
	print("*" * 30)
	try:
		userAccount = input('\nEnter your account number: ')
		userPin = stdiomask.getpass('Enter your pin: ')
		count = 0
		while (userAccount not in userData.keys() or userPin != userData[userAccount]['pin']) and count < 3:
			userAccount = input('\nEnter your account number: ')
			userPin = stdiomask.getpass('Enter your pin: ')
			if userAccount not in userData.keys():
				print('Wrong account number!')
			elif userPin != userData[userAccount]['pin']:
				print('Wrong pin')
			print(f'{2-count} attempts remaining!!')
			count += 1
			
		
		if userAccount not in userData.keys() or userPin != userData[userAccount]['pin']:
			print('Three failed attempts!!\nContact the customer desk to retrieve your credentials. \nGOODBYE!!')
			sys.exit()
		else:
			print(f'\nHello, {userData[userAccount]["username"]}')
			return userAccount


	except EOFError or userAccount == 0:
		sys.exit()
