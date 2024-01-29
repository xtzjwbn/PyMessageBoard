from src.UserSystem import UserSystem

if __name__ == '__main__':
	UserSystem = UserSystem()
	while True:
		command = input("Enter command: ").split(" ")

		if command[0] == "login":
			if len(command) != 3:
				print("Invalid command")
			else:
				if UserSystem.logIn(command[1], command[2]):
					print("Login successfully")
				else:
					print("Login failed")
		elif command[0] == "logout":
			if len(command) != 1:
				print("Invalid command")
			else:
				UserSystem.logOut()
				print("Logout successfully")
		elif command[0] == "logon":
			if len(command) != 4:
				print("Invalid command")
			else:
				if UserSystem.addUser(command[1], command[2], command[3]):
					print("Logon successfully")
				else:
					print("Logon failed")
		elif command[0] == "printcurrentuser":
			if len(command) != 1:
				print("Invalid command")
			else:
				UserSystem.printCurrentUser()
		elif command[0] == "printuserlist":
			if len(command) != 1:
				print("Invalid command")
			else:
				UserSystem.printUserList()

		else:
			print("Invalid command")

		# TODO : translate command to function call
