'''
Created on 2024. 4. 22.

@author: PC-02
'''
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pip._vendor.typing_extensions import Self
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("./myqt09.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myClick)
        self.rnd()
        self.flag = True
    def rnd(self):
        self.rnd = int(random()*99)+1
        print(self.rnd)
        
    def myClick(self):
        str =""
        mine_num = self.le.text()
        mine_inum = int(mine_num)
        if self.rnd > mine_inum:
            str = mine_num + "\t up \n" 
        
        elif self.rnd < mine_inum: 
            str = mine_num + "\t down \n"
        else :
            str = mine_num + "\t ok \n"
            # 
            QMessageBox.about(self,"updounaGame" , str)
            self.te.setText("")
            self.flag = False
        if self.flag:    
            str_old = self.te.toPlainText()
            self.te.setText(str_old+"\n"+str)
            self.le.setText("")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

