import sqlite3
import uuid
# from src.User import User
# from src.Message import Message


class MessageBoard:
    def __init__(self, max_list_showing=10, sqlite_path="../DataBase/MessageBoardDB.sqlite"):
        # self._message_list = []
        self._connect = sqlite3.connect(sqlite_path)
        self._cs = self._connect.cursor()
        self._max_list_showing = max_list_showing

    def __del__(self):
        self._connect.close()

    def addMessage(self, msg, user):
        msg_uuid = self._getUniqueUUID()
        self._cs.execute('''insert into MESSAGES values(?,?,?,?,?,?);''', (msg_uuid, msg, user.uuid, user.nickname, 0, True))
        self._connect.commit()
        message = self._cs.execute('''select * from MESSAGES where UUID = ? and ACTIVE=true''', (msg_uuid,)).fetchall()
        return message

    def removeMessage(self, message_uuid, user):
        real_user = self._cs.execute('''select user_uuid from MESSAGES where uuid = ? and active=true''', (message_uuid,)).fetchone()
        if real_user[0] == user.uuid:
            self._cs.execute('''update MESSAGES set active=false where uuid = ?''', (message_uuid,))
            self._connect.commit()
            return True
        return False

    def getMessageList(self):
        self._cs.execute('''
        select * from MESSAGES
        where ACTIVE=true''')
        message_list = self._cs.fetchall()
        return message_list

    def printMessageList(self):
        message_list = self.getMessageList()
        for index, message in enumerate(message_list):
            print("---------------------------------------")
            print("Message Number: " + str(index))
            print("UUID: " + message[0])
            print("Message: " + message[1])
            print("Create User: " + message[3])
            print("Like Num: " + str(message[4]))
            # print("---------------------------------------")

    # def likeMessage(self, msg_id, user):
    #     for message in self._message_list:
    #         if message.uuid == msg_id:
    #             message.addLikeUser(user)
    #             return True
    #     return False

    def _getUniqueUUID(self):
        current_uuid_result = self._cs.execute('''select UUID from MESSAGES''').fetchall()
        while True:
            user_uuid = uuid.uuid1().hex
            flag = False
            for current_uuid in current_uuid_result:
                if user_uuid == current_uuid[0]:
                    flag = True
                    break
            if not flag:
                return user_uuid
