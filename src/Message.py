from src.User import User


class Message:
    def __init__(self, msg, user):
        # TODO: id
        self._uuid = 0
        self._msg = msg
        self._create_user = user
        self._like_user_list = []
        self._active = True

    @property
    def uuid(self):
        return self._uuid

    @property
    def msg(self):
        return self._msg

    def setMsg(self, msg):
        # TODO: check if msg is valid
        self._msg = msg

    @property
    def create_user(self):
        return self._create_user

    @property
    def like_user_list(self):
        return self._like_user_list

    @property
    def active(self):
        return self._active

    def addLikeUser(self, user):
        if user in self._like_user_list:
            print("You already liked this message")
            return False
        else:
            self._like_user_list.append(user)

    def removeLikeUser(self, user):
        if user in self._like_user_list:
            self._like_user_list.remove(user)
            return True
        else:
            print("You have not like this message")
            return False
