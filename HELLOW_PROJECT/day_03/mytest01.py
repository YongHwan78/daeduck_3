'''
Created on 2024. 4. 17.

@author: PC-02
'''
# 첫변수를입력하시오
# 끝 변수를 입력하시오 

# ***
# ****
# *****
num1 = int(input("첫 변수를 입력하시오 "))
num2 = int(input("끝 변수를 입력하시오 "))
def star(cnt):  # 함수를 for문안에서 출력해서 간소화 시킴 
    ret = ""
    for i in range(cnt):
        ret += "★"
    return ret


for i in range(num1, num2+1):
    print(star(i))