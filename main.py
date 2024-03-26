import download as pytube
from interface import InterfacePyTube
from PySide6.QtWidgets import (
    QApplication,
)
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = InterfacePyTube()
    window.show()
    sys.exit(app.exec())
