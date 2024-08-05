'''
Created on 2024. 4. 22.

@author: PC-02
'''
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pip._vendor.typing_extensions import Self

form_class = uic.loadUiType("./myqt3.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        a= self.le01.text()
        b= self.le02.text()
        aa = int(a)
        bb = int(b)
        sum = aa - bb
        sumStr = str(sum)
        self.le03.setText(sumStr)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

