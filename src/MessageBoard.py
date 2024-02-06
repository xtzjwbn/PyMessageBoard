from src.UserSystem import UserSystem
from src.BoardSystem import BoardSystem
from src.LikeSystem import LikeSystem

class MessageBoard:
    def __init__(self, database_path="./DataBase/MessageBoardDB.sqlite", max_list_showing=10):
        self._max_list_showing = max_list_showing
        self._UserSystem = UserSystem(database_path)
        self._BoardSystem = BoardSystem(database_path)
        self._LikeSystem = LikeSystem(database_path)


    def InputLine(self, line_str):
        command = line_str.split(" ")

        # UserSystem
        if command[0] == "login":
            if len(command) != 3:
                print("Invalid command")
            else:
                if self._UserSystem.logIn(command[1], command[2]):
                    print("Login successfully")
                else:
                    print("Login failed")
        elif command[0] == "logoff":
            if len(command) != 1:
                print("Invalid command")
            else:
                self._UserSystem.logOff()
                print("logoff successfully")
        elif command[0] == "logon":
            if len(command) != 4:
                print("Invalid command")
            else:
                if self._UserSystem.addUser(command[1], command[2], command[3]):
                    print("Logon successfully")
                else:
                    print("Logon failed")
        # elif command[0] == "printcurrentuser":
        # 	if len(command) != 1:
        # 		print("Invalid command")
        # 	else:
        # 		self._UserSystem.printCurrentUser()
        # elif command[0] == "printuserlist":
        # 	if len(command) != 1:
        # 		print("Invalid command")
        # 	else:
        # 		self._UserSystem.printUserList()

        # BoardSystem
        elif command[0] == "list":
            if len(command) == 1:
                message_list = self._BoardSystem.getMessageList()
                self.printMessageList(message_list)
            else:
                if len(command) != 2:
                    print("Invalid command")
                else:
                    message_list = self._BoardSystem.getMessageList()
                    self.printNthMessageList(message_list, int(command[1]))
        elif command[0] == "add_msg":
            if self._UserSystem.current_user is None:
                print("Please login first")
            else:
                msg = line_str[len(command[0]) + 1:]
                self._BoardSystem.addMessage(msg, self._UserSystem.current_user)
                print("Message added successfully")
        elif command[0] == "del_msg":
            if len(command) != 2:
                print("Invalid command")
            else:
                if self._UserSystem.current_user is None:
                    print("Please login first")
                else:
                    # if self._BoardSystem.removeMessageByIndex(int(command[1]), self._UserSystem.current_user):
                    if self._BoardSystem.removeMessageByUUID(command[1], self._UserSystem.current_user):
                        print("Message deleted successfully")
                    else:
                        print("Message deleted failed")


        # LikeSystem
        elif command[0] == "like_msg":
            if len(command) != 2:
                print("Invalid command")
            else:
                if self._UserSystem.current_user is None:
                    print("Please login first")
                else:
                    # if self._LikeSystem.likeMessage(self._BoardSystem.indexToUUID(int(command[1])), self._UserSystem.current_user):
                    if self._LikeSystem.likeMessage(command[1], self._UserSystem.current_user):
                        print("Message liked successfully")
                    else:
                        print("Message liked failed")

        elif command[0] == "unlike_msg":
            if len(command) != 2:
                print("Invalid command")
            else:
                if self._UserSystem.current_user is None:
                    print("Please login first")
                else:
                    # if self._LikeSystem.dislikeMessage(self._BoardSystem.indexToUUID(int(command[1])), self._UserSystem.current_user):
                    if self._LikeSystem.dislikeMessage(command[1], self._UserSystem.current_user):
                        print("Message unliked successfully")
                    else:
                        print("Message unliked failed")
        elif command[0] == "exit":
            print("EXIT!")
            return

        else:
            print("Invalid command")

    def printNthMessageList(self, message_list, page_n):
        # page_n -= 1
        if page_n > len(message_list) // self._max_list_showing+1:
            print("Invalid page number")
            return
        for index, message in enumerate(message_list):
            if (page_n - 1) * self._max_list_showing <= index < page_n * self._max_list_showing:
                print("-------------------------------------------------")
                print("----- LIKE RANKING: " + str(index + 1))
                print("----- UUID: " + message[0])
                print("----- Message: " + message[1])
                print("----- Create User: " + message[3])
                print("----- Like Num: " + str(message[4]))
        print("-------------------------------------------------")

    def printMessageList(self, message_list):
        for index, message in enumerate(message_list):
            print("-------------------------------------------------")
            print("----- LIKE RANKING: " + str(index + 1))
            print("----- UUID: " + message[0])
            print("----- Message: " + message[1])
            print("----- Create User: " + message[3])
            print("----- Like Num: " + str(message[4]))
        print("-------------------------------------------------")

    def downloadMessageList(self, message_list, text_path):
        download_text = []
        for index, message in enumerate(message_list):
            download_text.append("-------------------------------------------------")
            download_text.append("----- LIKE RANKING: " + str(index + 1))
            download_text.append("----- UUID: " + message[0])
            download_text.append("----- Message: " + message[1])
            download_text.append("----- Create User: " + message[3])
            download_text.append("----- Like Num: " + str(message[4]))
        download_text.append("-------------------------------------------------")

        # download to txt
        with open(text_path, 'w') as f:
            for item in download_text:
                f.write("%s\n" % item)
        print("Downloaded to " + text_path)
