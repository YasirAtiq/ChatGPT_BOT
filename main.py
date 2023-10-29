from PyQt6.QtWidgets import (QMainWindow, QTextEdit, QLineEdit, QPushButton,
                             QApplication)
import sys


class ChatBot:
    pass


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Bot")
        self.setMinimumSize(700, 500)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        self.input_box = QLineEdit(self)
        self.input_box.setGeometry(10, 340, 480, 40)


        self.ok_button = QPushButton("Send", self)
        self.ok_button.setGeometry(500, 340, 100, 40)

        self.show()


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
