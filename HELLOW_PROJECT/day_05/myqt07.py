'''
Created on 2024. 4. 22.

@author: PC-02
'''
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pip._vendor.typing_extensions import Self
from random import random

form_class = uic.loadUiType("./myqt07.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        mine = self.pte_mine.toPlainText()
        print(mine)
        
        rnd = random()
        if rnd < 0.33:
            com = "주먹"
        elif rnd < 0.66:
            com = "가위"
        else :
            com = "보"    
        
        
        print(0,com)
        self.pte_com.setPlainText(com)

        str = ""
        if (mine == "가위" and com == "주먹") or (mine == "바위" and com == "보") or (mine == "보" and com == "가위"):
            str ="패배"
            print(1,str)
        elif (mine == "주먹" and com == "가위") or (mine == "보" and com == "바위") or (mine == "가위" and com == "보"):
            str ="승리"
            print(2,str)
        else :
            str = "비김"
            print(3,str)
        self.pte_result.setPlainText(str)
        print(str)
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

