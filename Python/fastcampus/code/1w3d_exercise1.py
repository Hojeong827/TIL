# 문장을 입력받아서 문법에 맞도록 결과를 출력하는 코드 작성
# 마지막 문자는 .이 잇을 수도 있고 없을 수도 있습니다.
# 논리적인 문제해결 순서 -> 코드로 연결
# str.upper(), str.lower, offset index [], str.__add__(문자열 덧셉)

# python IS the best Language / python IS the best Language.
# Python is the best language.

# 1 문자열 입력받기
sentence = input("input sentence: ")

# 2 모두 소문자로 변경
result=sentence.lower()

# 3 가장 앞글자 대문자로 변경
result=result[0].upper() + result[1:]

# 4 마지막 문자가 . 인지 아닌지 확인해서 . 이 아니면 . 추가
if result[-1]!="python.":
    result+="."

print(result)