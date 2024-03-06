import sys
import datetime
import PyQt6.QtGui
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

calendar_week_days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота',
                      7: 'Воскресенье', }


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(
            "background-image: url(Mainscreen.png); background-attachment: fixed, scroll; background-repeat: no-repeat;")
        self.setGeometry(0, 0, 1280, 800)

        self.labelGif = QLabel("Clock", self)
        self.labelGif.setGeometry(PyQt6.QtCore.QRect(0, 0, 150, 150))
        self.movie = PyQt6.QtGui.QMovie("watch-bright_circle.gif")
        self.labelGif.setStyleSheet("background-image: url();")
        self.labelGif.setScaledContents(True)
        self.labelGif.setMovie(self.movie)
        self.labelGif.move(350, 600)
        self.movie.start()

        PyQt6.QtGui.QFontDatabase.addApplicationFont('fonts\Tokeely_Brookings_Schatten.ttf')
        self.labelDate = QLabel("day_n_date", self)
        self.labelDate.setGeometry(PyQt6.QtCore.QRect(0, 0, 300, 200))
        self.labelDate.setStyleSheet("background-image: url(); color: rgb(255,255,255); font-weight: bold;")
        self.labelDate.setFont(PyQt6.QtGui.QFont('Tokeely Brookings Schatten', 40))
        self.labelDate.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDate.setScaledContents(True)
        self.labelDate.move(970, 200)
        self.labelDate.setText(
            str(calendar_week_days[datetime.datetime.now().isoweekday()]) + '\n' + '\n' + datetime.datetime.now().strftime(
                "%d.%m.%Y"))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
