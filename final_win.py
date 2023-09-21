from pyQt5.QtCore import Qt
from pyQt5.Qwidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *
 
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()


        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.text7 = QLabel(text7)
        self.text8 = QLabel(text8)
        self.layout = QVBoxLayout()
        self.text7.addWidget(self.layout)
        self.text8.addWidget(self.layout)
