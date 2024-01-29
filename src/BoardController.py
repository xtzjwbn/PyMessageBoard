from src.User import User
from src.Message import Message
from src.MessageBoard import MessageBoard

class BoardController:
	def __init__(self, message_board = None):
		if message_board is None:
			self._message_board = MessageBoard()
		else:
			self._message_board = message_board

	def printMessageBoard(self):
		print("Message Board:")
		for index,message in enumerate(self._message_board.message_list):
			print("---------------------------------------")
			print("Message Number: " + index)
			print(message.msg)
			print("Created by: " + message.create_user.username)
			print("Likes: " + str(len(message.like_user_list)))
			# print("Active: " + str(message.active))
			# print("---------------------------------------")
		print("---------------------------------------")