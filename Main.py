from src.MessageBoard import MessageBoard

if __name__ == '__main__':
    message_board = MessageBoard()
    while True:
        input_command = input("Enter command: ")
        if input_command == "exit":
            break
        message_board.InputLine(input_command)