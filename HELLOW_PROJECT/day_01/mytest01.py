'''
Created on 2024. 4. 15.

@author: PC-02
'''
#첫수를 입력하시오
#끝수를 입력하시오 
#1에서 4까지의 합은 10입니다.
fristNum = input("첫수를 입력하시오");
endNum = input("끝수를 입력하시오");
arr =range(int(fristNum), int(endNum) +1)
sum1 = 0;

for i in arr:
    sum1 += i
    
print("{}에서 {}까지의 합은 {}입니다.".format(fristNum,endNum,sum1))

