'''
Created on 2024. 4. 18.

@author: PC-02
'''

class LeeJY:
    def __init__(self):
        self.money = 100
    
    def yakun(self):
        self.money = self.money +1
        
class ElonMask:
    def __init__(self):
        self.skill_gas = 10000
    
    def getPenalty(self, cnt):
        self.skill_gas -= cnt;
        
class SungJae(LeeJY,ElonMask):
    def __init__(self):
        LeeJY.__init__(self)
        ElonMask.__init__(self)
        # super().__init__(self)
            
if __name__ == '__main__':
    # ljy =LeeJY()
    # em = ElonMask()
    sj = SungJae()
    
    print(sj.skill_gas , sj.money , sj.getPenalty(13) , sj.yakun() , sj.skill_gas , sj.money)
    
    # print(ljy.money , ljy.yakun() , ljy.money)
    # print(em.skill_gas , em.getPenalty(30) , em.skill_gas)