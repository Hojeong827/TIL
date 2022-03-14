# 6자리의 로또번호를 생성하는 코드를 작성하세요.
# 6자리의 번호는 중복이 X
# 문자열, 숫자, 리스트
# while, not in, in, list.append(), break, len(), list.sort()
# 문제가 조금 복잡하면 간단한 기능부터 구현하고 업데이트를 하는 방법으로 해결
# 랜덤한 숫자 6개 출력 -> 숫자가 중복되지 않는 코드를 추가

import random
# random.randint(1,45)

lotto = []
# 랜덤한 숫자 6개를 while 문을 사용해서 작성
while True:
    number=random.randint(1,45)
    if number not in lotto:
        lotto.append(number)
    if len(lotto) >= 6:
        lotto.sort()
        break

print(lotto)