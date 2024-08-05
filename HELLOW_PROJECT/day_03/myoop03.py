'''
Created on 2024. 4. 17.

@author: PC-02
'''

from day_03.myoop01 import Animal


class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skill_commnication = 1
        print("human생성자")
           
    def momstouch(self, stroke):
        self.skill_commnication += stroke 
    
    

if __name__ == '__main__':
    hum = Human()
    print(hum.skill_commnication)
    print(hum.flagM) 
    hum.gotoThai()
    print(hum.flagM) 
    hum.momstouch(13)
    print(hum.skill_commnication)
    