from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Stop Watch")
        self.setGeometry(100, 100, 400, 500)
        self.UiCmpt()
        self.show()

    def UiCmpt(self):
        self.count = 0
        self.flag = False
        self.label = QLabel(self)
        self.label.setGeometry(75, 100, 250, 70)
        self.label.setStyleSheet("border : 4px solid black;")
        self.label.setText(str(self.count))
        self.label.setFont(QFont('Arial', 25))
        self.label.setAlignment(Qt.AlignCenter)
        start = QPushButton("Start the Stopwatch", self)
        start.setGeometry(125, 250, 150, 40)
        start.pressed.connect(self.start)
        pause = QPushButton("Pause the Stopwatch", self)
        pause.setGeometry(125, 300, 150, 40)
        pause.pressed.connect(self.pause)
        re_set = QPushButton("Reset the Stopwatch", self)
        re_set.setGeometry(125, 350, 150, 40)
        re_set.pressed.connect(self.re_set)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def showTime(self):
        if self.flag:
            self.count += 1 
            text = str(self.count / 10)
            self.label.setText(text)

    def start(self):
        self.flag = True

    def pause(self):
        self.flag = False

    def re_set(self):
        self.flag = False
        self.count = 0
        self.label.setText(str(self.count))

        

    
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

print()