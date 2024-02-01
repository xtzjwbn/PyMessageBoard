from src.UserSystem import UserSystem
from src.MessageBoard import MessageBoard
from src.LikeSystem import LikeSystem

if __name__ == '__main__':
	UserSystem = UserSystem()
	MessageBoard = MessageBoard()
	LikeSystem = LikeSystem()
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
		elif command[0] == "logoff":
			if len(command) != 1:
				print("Invalid command")
			else:
				UserSystem.logOff()
				print("logoff successfully")
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

		elif command[0] == "like_msg":
			if len(command) != 2:
				print("Invalid command")
			else:
				if UserSystem.current_user is None:
					print("Please login first")
				else:
					if LikeSystem.likeMessage(command[1], UserSystem.current_user):
						print("Message liked successfully")
					else:
						print("Message liked failed")

		elif command[0] == "unlike_msg":
			if len(command) != 2:
				print("Invalid command")
			else:
				if UserSystem.current_user is None:
					print("Please login first")
				else:
					if LikeSystem.dislikeMessage(command[1], UserSystem.current_user):
						print("Message unliked successfully")
					else:
						print("Message unliked failed")
		elif command[0] == "exit":
			print("EXIT!")
			break

		else:
			print("Invalid command")

