from PyQt6.QtWidgets import (QMainWindow, QTextEdit, QLineEdit, QPushButton,
                             QApplication)
import openai
import sys
import os


class ChatBot:
    def __init__(self, user_input):
        my_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = my_key
        self.user_input = user_input
    
    def get_responce(self):
        responce = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=self.user_input,
            max_tokens=4080,
            temperature=0.5
        ).choices[0].text
        return responce


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
        self.ok_button.clicked.connect(self.send_message)
        self.show()
    
    def send_message(self):
        user_input = self.input_box.text().strip()
        self.chat_area.append(
            f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_box.clear()
        chatbot = ChatBot(user_input)
        responce = chatbot.get_responce()
        self.chat_area.append(
            f"<p style='color:#333333; background-\
            color:#E9E9E9'>Bot: {responce}</p>")


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
