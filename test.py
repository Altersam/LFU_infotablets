import sys
import datetime
import PyQt6.QtGui
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = "0"
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-image: url(Mainscreen.png); background-attachment: fixed, scroll; background-repeat: no-repeat;")
        self.setGeometry(0, 0, 1280, 800)




    def retranslateUI(self):
        self.label_before_Bell.setText(self.time_before())
        self.t = self.ticking()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    timer = PyQt6.QtCore.QTimer()
    timer.timeout.connect(lambda: window.retranslateUI())
    timer.start(600)

    window.show()

    sys.exit(app.exec())
