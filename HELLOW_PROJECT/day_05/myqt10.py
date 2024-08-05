'''
Created on 2024. 4. 22.

@author: PC-02
'''
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pip._vendor.typing_extensions import Self

form_class = uic.loadUiType("./myqt10.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        first_num = self.le_first.text()
        last_num = self.le_last.text()
        
        first_inum = int(first_num)
        last_inum = int(last_num)
        line = ""
        for i in range(first_inum , last_inum+1):
            line += self.star(i)
        
        self.pte.setPlainText(line )
        
    def star(self, cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

