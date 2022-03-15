# 함수의 실행 시간을 출력하는 데코레이터 함수를 작성하세요.
import time
from unittest import result

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()            # code_1
        result = func(*args, **kwargs)      # code_2
        end_time = time.time()              # code_3
        print("running time : {}".format(end_time-start_time))
        return result
    return wrapper

@timer
def test1(num1, num2):
    data = range(num1, num2+1)
    return sum(data)

@timer
def test2(num1, num2):
    result = 0
    for num in range(num1, num2+1):
        result += num
    return result

test1(1,10000)
test2(1,10000)