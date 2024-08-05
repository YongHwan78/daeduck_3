'''
Created on 2024. 4. 16.

@author: PC-02
'''
# 문제 2 숫자 맘추기 
from random import random

com = int((random()*99)) +1
print(com)
i = 0;
flag_ans = False

while True:
    num = int(input("수를 입력하시오 "))
    if i > 10 : 
        print("똑바로하세요")
        break
    if num < com :
        print("{} UP".format(num))
    elif num > com:
        print("{} DW".format(num))
    else:
        print("{} RS".format(num))
        flag_ans = True
        break
    i = i+1;


# for문일때 
if not flag_ans:
    print("똑바로하세요")