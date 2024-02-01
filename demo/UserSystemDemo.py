from src.UserSystem import UserSystem
from src.MessageBoard import MessageBoard

if __name__ == '__main__':
	UserSystem = UserSystem()
	MessageBoard = MessageBoard()
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
		elif command[0] == "list":
			if len(command) != 1:
				print("Invalid command")
			else:
				MessageBoard.printMessageList()

		elif command[0] == "add_msg":
			if len(command) != 2:
				print("Invalid command")
			else:
				if UserSystem.current_user is None:
					print("Please login first")
				else:
					MessageBoard.addMessage(command[1], UserSystem.current_user)
					print("Message added successfully")
		elif command[0] == "del_msg":
			if len(command) != 2:
				print("Invalid command")
			else:
				if UserSystem.current_user is None:
					print("Please login first")
				else:
					if MessageBoard.removeMessage(command[1], UserSystem.current_user):
						print("Message deleted successfully")
					else:
						print("Message deleted failed")

		else:
			print("Invalid command")

