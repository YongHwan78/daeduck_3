'''
Created on 2024. 4. 16.

@author: PC-02
'''
import random
# arr = [1,2,3,4,5]
# for i in range(100):
#     rnd = int(random.random()*5)
#     param = arr[0]
#     arr[0] = arr[rnd]
#     rnd = param
# print(arr)

arr = [1,2,3,4,5,6,7,8,9] 
arr2 = list(range(1,9+1))  # 함수형 배열을 바꿈  

for i in arr:
    rnd = int(random.random()*9)
    par = arr[0]
    arr[0]= arr[rnd]
    arr[rnd] = par

print(arr[0], arr[1], arr[2])
#
#
# arr = list(range(1, 45+1))
# arr2 = [0] * 9  
# i = 0
#
# while i < 9:
#     arr2[i] = random.randint(1, 45)  
#     while arr2[i] in arr2[:i]: 
#         arr2[i] = random.randint(1, 45)
#     i += 1
#
# print(arr2)