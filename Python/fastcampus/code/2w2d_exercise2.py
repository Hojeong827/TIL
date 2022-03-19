# 에러 생성 : 10 이상의 숫자가 입력되도록 하는 에러
# LowNumber

class LowNumber(Exception):
    
    def __str__(self):
        return "Number grater than 10"

def input_number(num):
    if num<=10:
        raise LowNumber()
    print(num)

input_number(12)            # 12 출력
input_number(8)             # 강제적으로 error 발생 됨