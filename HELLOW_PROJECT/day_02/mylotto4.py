'''
Created on 2024. 4. 16.

@author: PC-02
'''
import random

arr = list(range(1,45+1))  
arr2 = {
    1,2,3,4,5,    6,7,8,9,10,
    11,12,13,14,15,    16,17,18,19,20,
    21,22,23,24,25,    26,27,28,29,30,
    31,32,33,34,35,    36,37,38,39,40,
    41,42,43,44,45    
    }        
for i in range(1000):
    rnd = int(random.random()*45)
    par = arr[0]
    arr[0]= arr[rnd]
    arr[rnd] = par


for i in range(6):
    for j in range(6):
        if arr[i] < arr[j]:
            param = arr[j]
            arr[j] = arr[i]
            arr[i] = param
            # param = arr[i]
            # param2 = arr[j]
            # arr[i] = param2
            # arr[j] = param
         
         
print(arr[0] ,end=",")
print(arr[1],end=",")
print(arr[2],end=",")
print(arr[3],end=",")
print(arr[4],end=",")
print(arr[5])
