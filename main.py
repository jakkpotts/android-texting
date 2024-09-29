import sys
from modules import googlemessages
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QTextEdit, QPushButton

class MessagesClone(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Messages App Clone')

        # Layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # List of conversations
        self.conversations_list = QListWidget()
        self.conversations_list.addItem("John Doe")
        self.conversations_list.addItem("Jane Smith")
        main_layout.addWidget(self.conversations_list)

        # Text area for conversation
        self.conversation_text = QTextEdit()
        self.conversation_text.setReadOnly(True)
        main_layout.addWidget(self.conversation_text)

        # Text input area
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Type a message...")
        main_layout.addWidget(self.message_input)

        # Send button
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_message)
        main_layout.addWidget(send_button)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def send_message(self):
        message = self.message_input.toPlainText()
        self.conversation_text.append(f"You: {message}")
        self.message_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MessagesClone()
    main_window.show()
    sys.exit(app.exec_())