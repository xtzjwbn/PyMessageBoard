from src.User import User

class UserSystem:
	def __init__(self):
		self._user_list = []
		self._current_user = None

	def addUser(self, username, password, nickname):
		user = User(username, password, nickname)
		self._user_list.append(user)
		return user

	def logIn(self, username, password):
		if self._current_user is not None:
			print("There is user " + self._current_user.username + " logged in!")
			return False
		for user in self._user_list:
			if user.username == username and user.password == password:
				self._current_user = user
				return True
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
		for index,user in enumerate(self._user_list):
			print("---------------------------------------")
			print("User Number: " + str(index))
			print("Userid: " + user.id)
			print("Username: " + user.username)
			print("Nickname: " + user.nickname)
			# print("---------------------------------------")