'''
Created on 2024. 4. 17.

@author: PC-02
'''
#위에서 부터 읽어 오는 인터프린터 계얼 언어고  자바는 컴파일러 언어이기 때문이다 .
def add_min_mul_div(a, b):
    return a+b ,a-b, a*b , a/b

sum = add_min_mul_div(4,2)


# print("minus", min)
print("sum", sum[3]) #tuple -- 멀티리턴 
# print("multiply", mul)
# print("divide", div)