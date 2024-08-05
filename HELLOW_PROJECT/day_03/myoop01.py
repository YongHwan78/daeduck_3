'''
Created on 2024. 4. 17.

@author: PC-02
'''

class Animal:
    def __init__(self): # JAVA에서 셍성자
        self.flagM = True
        print("생성자")
    def gotoThai(self):
        self.flagM = not self.flagM
    
    def __del__(self):
        print("소멸자")
    

if __name__ == '__main__':
        
    ani = Animal()
    
    print("1",ani.flagM)
    ani.gotoThai()
    print("1",ani.flagM)
    
    