'''
Created on 2024. 4. 15.

@author: PC-02
'''
#첫수를 입력하시오
#끝수를 입력하시오 
#1은 3보다 작다 

num1 = input("첫수를 입력하시오");
num2 = input("끝수를 입력하시오");

if int(num1) < int(num2):
    print("{}는 {}보다 작다".format(num1,num2))
elif int(num1) > int(num2): 
    print("{}는 {}보다 크다".format(num1,num2))   
else:
    print("{}과 {}같다".format(num1,num2))   