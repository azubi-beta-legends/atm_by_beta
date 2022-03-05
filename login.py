# Python 3.10.1
# Coding: utf-8
# user login attempts

# import jsonHandler

# userData = jsonHandler.readJsonFile(r'C:\Users\DESMOND\Desktop\Azubi\5.Python\ATM\confidential\userinfo.json')
# print(userData)
 

def user_login(userdata):
	print("**************************")
	print("* *")
	print("* Welcome to BETA ATM SYSTEM *")
	print("* *")
	print("**************************")

	userAccount = input('Enter your account number: ')
	userPin = input('Enter your pin: ')
	# count = 0

	if userAccount not in userdata.keys():
		print('Invalid account or password, try again')
		user_login()

	elif userAccount in userdata.keys() and userPin == userdata[userAccount]['pin']:
		return userAccount

