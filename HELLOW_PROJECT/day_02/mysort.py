'''
Created on 2024. 4. 16.

@author: PC-02
'''
import random

# arr = list(range(1, 45 + 1))  
#
# for i in range(1000):
#     rnd = int(random.random() * 45)
#     par = arr[0]
#     arr[0] = arr[rnd]
#     arr[rnd] = par

arr = [5 ,6 , 3,16 , 8 , 12]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            param = arr[j]
            arr[j] = arr[i]
            arr[i] = param
            
            
            # param = arr[i]
            # param2 = arr[j]
            # arr[i] = param2
            # arr[j] = param
         
         
print(arr)
         
         
         