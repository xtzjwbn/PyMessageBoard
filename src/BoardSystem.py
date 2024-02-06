import sqlite3
import src.FuncLib as FuncLib

class BoardSystem:
    def __init__(self, sqlite_path="./DataBase/MessageBoardDB.sqlite"):
        # self._message_list = []
        self._connect = sqlite3.connect(sqlite_path)
        self._cs = self._connect.cursor()

    def __del__(self):
        self._connect.close()

    def addMessage(self, msg, user):
        msg_uuid = FuncLib.getUniqueUUID(self._cs, "MESSAGES")
        self._cs.execute(
            '''
            insert into MESSAGES values(?,?,?,?,?,?);
            ''', (msg_uuid, msg, user.uuid, user.nickname, 0, True))
        self._connect.commit()
        message = self._cs.execute(
            '''
            select * from MESSAGES where UUID = ? and ACTIVE=true
            ''', (msg_uuid,)).fetchall()
        return message

    def indexToUUID(self, index):
        message_list = self.getMessageList()
        if index > len(message_list):
            print("Warning: index out of range")
            return None
        return message_list[index-1][0]

    def removeMessageByUUID(self, message_uuid, user):
        real_user = self._cs.execute(
            '''
            select user_uuid from MESSAGES where uuid = ? and active=true
            ''', (message_uuid,)).fetchone()
        if real_user[0] == user.uuid:
            self._cs.execute(
                '''
                update MESSAGES set active=false where uuid = ?
                ''', (message_uuid,))
            self._connect.commit()
            return True
        return False

    def removeMessageByIndex(self, index, user):
        message_list = self.getMessageList()
        message_uuid = self.indexToUUID(index)
        return self.removeMessageByUUID(message_uuid,user)

    def getMessageList(self):
        self._cs.execute('''
        select * from MESSAGES
        where ACTIVE=true
        order by LIKE DESC''')
        message_list = self._cs.fetchall()
        return message_list

    # def printNthMessageList(self, page_n):
    #     message_list = self.getMessageList()
    #     self._message_board.printNthMessageList(message_list, page_n)
    #
    # def printMessageList(self):
    #     message_list = self.getMessageList()
    #     self._message_board.printMessageList(message_list)
    #
    # def downloadMessageList(self, textpath):
    #     message_list = self.getMessageList()
    #     self._message_board.downloadMessageList(message_list, textpath)
