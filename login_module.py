# Python 3.10.1
# Coding: utf-8
# user login attempts


from tkinter import W
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
		# count = 0

		if userAccount not in userData.keys():
			print('Invalid account or password, try again')
			user_login()

		elif userAccount in userData.keys() and userPin == userData[userAccount]['pin']:
			print(f'\nHello, {userData[userAccount]["username"]}')
			if userAccount != None:
				return userAccount
			else:
				user_login()
		else:
			print('Wrong credentials! Try again.')
			exit
	except EOFError or userAccount == 0:
		sys.exit()
