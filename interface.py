# Create a interface using pyside6 that take a video path and download it

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QWidget, QLabel
import sys
from pytube import YouTube

class InterfacePyTube(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyTube")
        self.resize(400, 100)

        layout = QVBoxLayout()

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download_video)
        layout.addWidget(self.download_button)

        self.status_label = QLabel()
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def download_video(self):
        url = self.url_input.text()
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        self.status_label.setText("Vídeo baixado")
