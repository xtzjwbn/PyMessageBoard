class MessageBoard:
    def __init__(self, max_list_showing=10):
        self._max_list_showing = max_list_showing

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
