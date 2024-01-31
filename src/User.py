import uuid
import hashlib


class User:
    def __init__(self, user_data):
        self._uuid = user_data[0]
        self._username = user_data[1]
        self._password = user_data[2]
        self._nickname = user_data[3]

    @property
    def uuid(self):
        return self._uuid

    @property
    def username(self):
        return self._username

    def setUsername(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    # TODO: maybe should not provide this method
    def setPassword(self, password):
        self._password = password

    @property
    def nickname(self):
        return self._nickname

    def setNickname(self, nickname):
        self._nickname = nickname
