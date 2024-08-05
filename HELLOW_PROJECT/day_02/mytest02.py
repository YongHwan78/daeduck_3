'''
Created on 2024. 4. 16.

@author: PC-02
'''
# 문제 1
# 가위 / 바위 / 보 
# 나 
# 컴 
# 결과 
from random import random

arr = ["가위", "바위", "보"]
com = arr[int(random()*3)]
my = input("가위/바위/보를 입력하세요")
result =""

if((com =="가위" and my=="보") or (com=="바위" and my=="가위") or (com=="보" and my=="바위")):
    result = "졌습니다."
elif((my=="가위" and com=="보") or (my=="바위" and com=="가위") or (my=="보" and com=="바위")):
    result = "이겼습니다"
else:
    result ="비겼습니다."

print("com : {} my : {} {}".format(com , my , result))
