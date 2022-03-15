# 패스워드를 입력 받아야 함수가 실행되도록하는 데코레이터 작성
import random

def check_password(func):
    def wrapper(*args, **kwargs):
        pw="dss11"
        # check password
        input_pw=input("insert pw : ")
        if input_pw == pw:
            result = func(*args, **kwargs)
        else:
            result = "not allow!"
        return result
    return wrapper

@check_password
def plus(a,b):
    return a+b

@check_password
def lotto_func():
    lotto=[]
    while True:
        number = random.randint(1,45)
        if number not in lotto:
            lotto.append(number)
        if len(lotto) >= 6:
            lotto.sort()
            break
    return lotto

print(plus(1,2))
print(lotto_func())