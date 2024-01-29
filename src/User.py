class User:
	def __init__(self, username, password, nickname):
		# TODO: id
		self._id = 0
		self._username = username
		self._password = password
		self._nickname = nickname

	@property
	def id(self):
		return self._id

	@property
	def username(self):
		return self._username
	def setUsername(self, username):
		# TODO: check if username is valid
		self._username = username

	@property
	def password(self):
		return self._password
	def setPassword(self, password):
		# TODO: check if password is valid
		self._password = password

	@property
	def nickname(self):
		return self._nickname
	def setNickname(self, nickname):
		self._nickname = nickname