import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import socket
import threading

class Client(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.initUI()
        self.connectServer()

    def initUI(self):
        # Set window properties
        self.setWindowTitle('Chat Client')
        self.setGeometry(100, 100, 400, 600)

        # Create layout for text area
        layout = QVBoxLayout()
        self.textArea = QTextEdit()
        self.textArea.setReadOnly(True)
        self.textArea.setStyleSheet("background-color: white;")
        self.textArea.setFont(QFont("Arial", 12))
        layout.addWidget(self.textArea)

        # Create input area for typing messages
        self.inputArea = QTextEdit()
        self.inputArea.setStyleSheet("background-color: white;")
        self.inputArea.setFont(QFont("Arial", 12))
        layout.addWidget(self.inputArea)

        # Create button for sending messages
        buttonLayout = QHBoxLayout()
        sendButton = QPushButton("Send")
        sendButton.clicked.connect(self.sendMessage)
        buttonLayout.addWidget(sendButton)

        # Add layouts to main layout
        self.setLayout(layout)
        layout.addLayout(buttonLayout)

        # Show the window
        self.show()

    def connectServer(self):
        # Create a new socket and connect to the server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('localhost', 55555))

        # Send the username to the server
        self.socket.send(self.username.encode())

        # Start a new thread to receive messages from the server
        thread = threading.Thread(target=self.receiveMessage)
        thread.start()

    def receiveMessage(self):
        # Continuously receive messages from the server and append them to the text area
        while True:
            try:
                message = self.socket.recv(1024).decode()
                self.textArea.append(message)
            except:
                # If an error occurs, close the socket and break out of the loop
                self.socket.close()
                break

    def sendMessage(self):
        # Get the message from the input area and send it to the server
        message = f"{self.username}: {self.inputArea.toPlainText()}"
        self.socket.send(message.encode())

        # Clear the input area
        self.inputArea.clear()
