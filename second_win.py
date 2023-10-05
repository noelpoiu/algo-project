from pyQt5.QtCore import Qt
from pyQt5.Qwidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QInputDialog
from instr import *
class Testwin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        name = buttontext(txt_title)
        input1 = QInputDialog()
        full = buttontext(text60)
        test1 = QPushButton(buttontext)
        input2 = QInputDialog()
        back = buttontext(text3)
        input3 = QInputDialog()
        tarining = buttontext(text5)
        squats = QPushButton(buttontext2)
        back2 = buttontext(text6)
        final = QPushButton(buttontext3)
        input4 = QInputDialog()
        input5 = QInputDialog()

        results = QPushButton(buttontext4)
        
      