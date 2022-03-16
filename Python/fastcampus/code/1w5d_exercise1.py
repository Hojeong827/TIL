# pandas dataframe
import pandas as pd

# user data 를 입력 받아서 아이디와 패스워드를 체크하는 데코레이터 함수르르 코드로 작성하세요.
# 로그인 될 때마다 count를 1씩 증가
"""
ls = ["a", "b", "c"]
list(range(len(ls))
print(list(range(len(ls)))
[0, 1, 2]

list(zip(range(len(ls)),ls))                # 값을 묶어줌
print(list(zip(range(len(ls)),ls)))
[(0, 'a'), (1, 'b'), (2, 'c')]

for idx, data in list(zip(range(len(ls)),ls)):
    print(idx, data)
0 a
1 b
2 c

list(enumerate(user_datas))                 # index 값 자동으로 생성
[(0, {'user': 'test', 'pw': '1234', 'count': 0})
(1, {'user': 'python', 'pw': '5678', 'count': 0}]
"""
user_datas=[
    {"user":"test", "pw":"1234", "count": 0},
    {"user":"python", "pw":"5678", "count": 0},
]

def need_login(func):
    def wrapper(*args, **kwargs):
        # 아이디 패스워드 입력
        user, pw = tuple(input("insert user pw :").split(" "))
        
        # 존재하는 아이디와 패스워드 인지 확인
        # for idx, user_data in enumerate(user_datas):
        for idx, user_data in zip(range(len(user_datas)), user_datas):
            if (user_data["user"] == user) and (user_data["pw"] == pw):
                # count 데이터
                user_datas[idx]["count"]+=1
                # 함수 실행
                return func(*args, **kwargs)
        return "wrong login data!"
    return wrapper

@need_login
def plus(num1, num2):
    return num1+num2

print(plus(1,2))
print(user_datas)