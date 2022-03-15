# input 함수로 구분자는 " "으로 여러개의 숫자를 입력 받습니다.
# str.split(" ") 리스트로 만들고
# 만들어진 리스트의 값들을 int 형변환

datas = input("input numbers : ")
result = datas.split(" ")
print(result)   # result 라는 list에 string 형식으로 들어감
result = list(map(int, result))
print(result)   # result 라는 list에 string의 값들이 모두 int형으로 변환되어 저장