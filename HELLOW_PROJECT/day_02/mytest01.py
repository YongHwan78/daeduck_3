'''
Created on 2024. 4. 16.

@author: PC-02
'''
# 출력단수를 입력하시오

num= int(input("출력단수를 입력하시오"))
for i in range(1,9+1):
    print ("{} * {} = {}".format(num, i , num*i))