'''
Created on 2024. 4. 22.

@author: PC-02
'''
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pip._vendor.typing_extensions import Self

form_class = uic.loadUiType("./myqt04.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        num1 = self.le01.text()
        num2 = self.le02.text()
        num1I = int(num1)
        num2I = int(num2)
        multi = self.le03.text()
        multiI = int(multi)
        sum = 0;
        for a in range(num1I, num2I+1):
            if a%multiI == 0:
                sum += a 
                
        self.le04.setText(str(sum));
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

