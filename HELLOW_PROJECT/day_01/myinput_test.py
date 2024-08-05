'''
Created on 2024. 4. 15.

@author: PC-02
'''
# 좋아하는 수를 입력하세요. 6 
# 좋아하는 수를 입력하세요. 7
# 6과 7의 합은 13입니다.
a = input("좋아하는 수를 입력하세요 ")

b = input("또 좋아하는 수를 입력하세요 ")

sum_1 = int(a) + int(b);

print(a , "과" , b , "의 합은" , int(a) + int(b))

print("{}과 {}의 합은 {}입니다.".format(a,b,sum_1))