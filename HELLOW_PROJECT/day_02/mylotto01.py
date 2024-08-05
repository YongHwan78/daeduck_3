'''
Created on 2024. 4. 16.

@author: PC-02
'''
import random
arr = [1,2,3,4,5]
for i in range(100):
    rnd = int(random.random()*5)
    param = arr[0]
    arr[0] = arr[rnd]
    rnd = param
    

print(arr)



