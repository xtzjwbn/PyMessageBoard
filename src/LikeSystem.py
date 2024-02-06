import sqlite3
import src.FuncLib as FuncLib

class LikeSystem:
    def __init__(self, sqlite_path="./DataBase/MessageBoardDB.sqlite"):
        self._connect = sqlite3.connect(sqlite_path)
        self._cs = self._connect.cursor()

    def __del__(self):
        self._connect.close()

    def likeMessage(self, message_uuid, user):
        like_uuid = FuncLib.getUniqueUUID(self._cs, "LIKES")

        self._cs.execute(
            '''
            select * from LIKES
            where MESSAGE_UUID = ? and USER_UUID = ?
        ''', (message_uuid, user.uuid))
        result = self._cs.fetchall()

        if len(result) != 0:
            # print("You already liked this message")
            return False

        self._cs.execute(
            '''
            insert into LIKES values(?,?,?);
            ''', (like_uuid, message_uuid, user.uuid))
        self._connect.commit()
        self._cs.execute(
            '''
                update MESSAGES set LIKE = LIKE + 1
                where UUID = ?
            ''', (message_uuid,))
        self._connect.commit()
        return True

    def dislikeMessage(self, message_uuid, user):
        self._cs.execute('''
            select * from LIKES
            where MESSAGE_UUID = ? and USER_UUID = ?
        ''', (message_uuid, user.uuid))
        result = self._cs.fetchall()

        if len(result) == 0:
            # print("You have not liked this message")
            return False

        self._cs.execute(
            '''
            delete from LIKES
            where MESSAGE_UUID = ? and USER_UUID = ?
            ''', (message_uuid, user.uuid))
        self._connect.commit()
        self._cs.execute(
            '''
            update MESSAGES set LIKE = LIKE - 1
            where UUID = ?
            ''', (message_uuid,))
        self._connect.commit()

        return True
