'''
Created on 2024. 4. 16.

@author: PC-02
'''
# 홀짝을 입력해주세요
# 나 : 홀 
# 컴 : 짝
# 결과 짐 

from random import random

com = ["홀","짝"]

mine = ""

result = ""


mine = input("홀짝을 입력해주세요")
num = int(random()*2)
if com[num] == mine :
    result = "플레이어 승"
else:
    result = "플레이어 짐"
    
print("결과 : " +result)
print("컴 : " +com[num])
print("유저 : "+ mine)

