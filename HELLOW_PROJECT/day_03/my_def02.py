'''
Created on 2024. 4. 17.

@author: PC-02
'''

def multiply(a,b):
    return a*b

def showDan(dan):
    for i in range(1, 9 + 1):
        print("{} * {} = {} ".format(dan , i , multiply(i,dan)))

    
showDan(7)
