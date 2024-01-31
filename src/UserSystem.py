import sqlite3
import uuid
import hashlib
from src.User import User


class UserSystem:
	def __init__(self, sqlite_path="../DataBase/MessageBoardDB.sqlite"):
		# self._user_list = []
		self._connect = sqlite3.connect(sqlite_path)
		self._cs = self._connect.cursor()
		self._current_user = None

	def addUser(self, username, password, nickname):
		# TODO: check valid
		user_uuid = self._getUniqueUUID()
		password = hashlib.md5(password.encode('utf-8')).hexdigest()
		self._cs.execute('''insert into USER values(?,?,?,?);''', (user_uuid, username, password, nickname))
		self._connect.commit()
		user = self._cs.execute('''select * from USER where UUID = ?''', [user_uuid])
		user = self._cs.fetchall()
		return user

	def logIn(self, username, password):
		if self._current_user is not None:
			print("There is user " + self._current_user.username + " logged in!")
			return False
		password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
		self._cs.execute('''select * from USER where NAME = ? and PASSWORD = ?''', (username, password_md5))
		result = self._cs.fetchall()
		if len(result) == 1:
			self._current_user = User(result[0])
			return True
		else:
			return False

	def logOut(self):
		self._current_user = None

	@property
	def current_user(self):
		return self._current_user

	def printCurrentUser(self):
		if self._current_user is None:
			print("No current user")
		else:
			print("Current User:")
			print("---------------------------------------")
			print("Username: " + self._current_user.username)
			print("Nickname: " + self._current_user.nickname)
			print("---------------------------------------")

	def printUserList(self):
		print("User List:")
		self._cs.execute('''select * from USER''')
		user_list = self._cs.fetchall()
		for index, user in enumerate(user_list):
			print("---------------------------------------")
			print("User Number: " + str(index))
			print("User_uuid: " + user[0])
			print("Username: " + user[1])
			print("Nickname: " + user[3])
			# print("---------------------------------------")

	def _getUniqueUUID(self):
		current_uuid_result = self._cs.execute('''select UUID from USER''').fetchall()
		while True:
			user_uuid = uuid.uuid1().hex
			flag = False
			for current_uuid in current_uuid_result:
				if user_uuid == current_uuid[0]:
					flag = True
					break
			if not flag:
				return user_uuid