'''
Created on 2024. 4. 16.

@author: PC-02
'''
import random

arr = list(range(1,45+1))  
            
for i in range(1000):
    rnd = int(random.random()*45)
    par = arr[0]
    arr[0]= arr[rnd]
    arr[rnd] = par


print(arr[0] ,end=",")
print(arr[1],end=",")
print(arr[2],end=",")
print(arr[3],end=",")
print(arr[4],end=",")
print(arr[5])
#
#
# arr = list(range(1, 45+1))
# arr2 = [0] * 6  
# i = 0
#
# while i < 6:
#     arr2[i] = random.randint(1, 45)  
#     while arr2[i] in arr2[:i]: 
#         arr2[i] = random.randint(1, 45)
#     i += 1
#
# print(arr2)