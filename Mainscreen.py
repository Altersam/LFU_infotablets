import sys
import datetime
import PyQt6.QtGui
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

calendar_week_days = {1: 'Понедельник',
                      2: 'Вторник',
                      3: 'Среда',
                      4: 'Четверг',
                      5: 'Пятница',
                      6: 'Суббота',
                      7: 'Воскресенье', }
lessons_time = {"0": ["08:30", "09:15"],
                     "1": ["09:30", "10:15 "],
                     "2_10": ["10:35", "11:20"], "2_8911": ["10:20", "11:05"],
                     "3": ["11:30", "12:15"],
                     "4": ["12:25", "13:10"],
                     "5": ["13:20", "14:05"],
                     "6_10": ["14:35", "15:20"], "6_8911": ["14:10", "14:55"],
                     "7": ["15:30", "16:15"],
                     "8": ["16:25", "17:10"],
                     "9": ["17:20", "18:05"]
                }


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = "0"
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
            str(calendar_week_days[
                    datetime.datetime.now().isoweekday()]) + '\n' + '\n' + datetime.datetime.now().strftime(
                "%d.%m.%Y"))

        self.labelClock = QLabel("Clock", self)
        self.labelClock.setGeometry(PyQt6.QtCore.QRect(0, 0, 400, 280))
        self.labelClock.setStyleSheet("background-image: url(); color: rgb(255,255,255); font-weight: bold;")
        self.labelClock.setFont(PyQt6.QtGui.QFont('Tokeely Brookings Schatten', 60))
        self.labelClock.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelClock.setScaledContents(True)
        self.labelClock.move(10, 500)
        self.labelClock.setText(
            str("Время" + '\n' + datetime.datetime.now().strftime("%H : %M") + '\n'))

        self.label_before_Bell = QLabel("Clock", self)
        self.label_before_Bell.setGeometry(PyQt6.QtCore.QRect(0, 0, 400, 200))
        self.label_before_Bell.setStyleSheet("background-image: url(); color: rgb(255,255,255); font-weight: bold;")
        self.label_before_Bell.setFont(PyQt6.QtGui.QFont('Tokeely Brookings Schatten', 35))
        self.label_before_Bell.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_before_Bell.setScaledContents(True)
        self.label_before_Bell.move(10, 650)
        now_time = datetime.datetime.now().strftime("%H:%M")
        for i in lessons_time.keys():
            if int(lessons_time[i][0][0:2]) < int(now_time[0:2]) < int(lessons_time[i][1][0:2]):
                if  (i =="2_8911" or i == "6_8911") and 1:  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    self.x = str((int(lessons_time[i][1][3:5]) + int(now_time[3:5])) % 60) + " минут"
            elif int(now_time[0:2]) < int(lessons_time[i][0][0:2]):
                if (i == "2_8911" or i == "6_8911") and 1:  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    self.x = str((int(lessons_time[i][0][3:5]) + int(now_time[3:5])) % 60) + " минут"
            else:
                self.x = str((int(lessons_time[i][1][3:5]) + int(now_time[3:5])) % 60) + " минут"
        self.label_before_Bell.setText(str("До звонка" + '\n' + self.x))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
