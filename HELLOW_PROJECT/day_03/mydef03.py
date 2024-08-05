'''
Created on 2024. 4. 17.

@author: PC-02
'''
from random import random

def getHJ():
    rnd= random()
    if rnd > 0.5 :
        com = "홀"
    else :
        com = "짝"
    return com

print("com", getHJ());