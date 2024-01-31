from src.User import User
from src.Message import Message


class MessageBoard:
    def __init__(self, max_list_showing=10):
        self._message_list = []
        self._max_list_showing = max_list_showing

    def addMessage(self, msg, user):
        message = Message(msg, user)
        self._message_list.append(message)
        return message

    def removeMessage(self, message):
        # TODO
        pass

    def likeMessage(self, msg_id, user):
        for message in self._message_list:
            if message.uuid == msg_id:
                message.addLikeUser(user)
                return True
        return False
