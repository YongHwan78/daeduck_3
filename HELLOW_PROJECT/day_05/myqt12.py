import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("./myqt12.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myClick)
        self.com = self.rnd()
        print(self.com)
    def myClick(self):
        mine = self.le.text()
        s = str(self.getS(mine))
        b = str(self.getB(mine))
        self.oldText = self.te.toPlainText()
        self.te.setText(self.oldText+mine+"\t strike:" + s + "\t" +"ball:" + b + "\n" +"====================" + "\n")
        
        if s=="3":
            QMessageBox.about(self, '축하합니다', mine)
            return;
        
    def rnd(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(arr)
        com = ''.join(map(str, arr[:3]))
        return com
    
    def getS(self, mine):
        ret = 0
        c1, c2, c3 = self.com[0], self.com[1], self.com[2]
        m1, m2, m3 = mine[0], mine[1], mine[2]
        
        if c1 == m1:
            ret += 1
        if c2 == m2:
            ret += 1
        if c3 == m3:
            ret += 1
        
        return ret
    
    def getB(self, mine):
        ret = 0
        c1, c2, c3 = self.com[0], self.com[1], self.com[2]
        m1, m2, m3 = mine[0], mine[1], mine[2]
        
        if c1 == m2 or c1 == m3:
            ret += 1
        if c2 == m1 or c2 == m3:
            ret += 1
        if c3 == m2 or c3 == m1:
            ret += 1
        
        return ret
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
