'''
Created on 2024. 4. 22.

@author: PC-02
'''
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pip._vendor.typing_extensions import Self

form_class = uic.loadUiType("./myqt02.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        print(self.le.text())
        a= self.le.text()
        aa = int(a)
        aa = aa -1
        self.le.setText(str(aa))
        
        # a = a -1
        # self.le.setText(""+a)
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

