import sqlite3
import hashlib
from src.User import User
import src.FuncLib as FuncLib


class UserSystem:
    def __init__(self, sqlite_path="./DataBase/MessageBoardDB.sqlite"):
        # self._user_list = []
        self._connect = sqlite3.connect(sqlite_path)
        self._cs = self._connect.cursor()
        self._current_user = None

    def __del__(self):
        self._connect.close()

    def addUser(self, username, password, nickname):
        unique_username_list = self._cs.execute('''select * from USERS where NAME = ?''', (username,)).fetchall()
        if len(unique_username_list) != 0:
            print("Username has been used!")
            return False
        unique_nickname_list = self._cs.execute('''select * from USERS where NICKNAME = ?''', (nickname,)).fetchall()
        if len(unique_nickname_list) != 0:
            print("Nickname has been used!")
            return False
        user_uuid = FuncLib.getUniqueUUID(self._cs, "USERS")
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        self._cs.execute('''insert into USERS values(?,?,?,?);''', (user_uuid, username, password, nickname))
        self._connect.commit()

        user = self._cs.execute('''select * from USERS where UUID = ?''', (user_uuid,)).fetchall()
        return user

    def logIn(self, username, password):
        if self._current_user is not None:
            print("There is user " + self._current_user.username + " logged in!")
            return False
        password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
        self._cs.execute('''select * from USERS where NAME = ? and PASSWORD = ?''', (username, password_md5))
        result = self._cs.fetchall()
        if len(result) == 1:
            self._current_user = User(result[0])
            return True
        else:
            return False

    def logOff(self):
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
        self._cs.execute('''select * from USERS''')
        user_list = self._cs.fetchall()
        for index, user in enumerate(user_list):
            print("---------------------------------------")
            print("User Number: " + str(index))
            print("User_uuid: " + user[0])
            print("Username: " + user[1])
            print("Nickname: " + user[3])
    # print("---------------------------------------")
