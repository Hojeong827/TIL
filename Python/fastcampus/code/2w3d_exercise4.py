import numpy as np

# 100~130 까지 랜덤한 숫자를 가지는 8*8행렬을 만들고,
# 3의 배수는 fiz, 5의 배수는 buz, 3과 5의 배수는 fbz 문자로 변환
# 랜덤한 행렬 데이터
# 데이터 타입이 정수 -> 문자열 : ndarray.astype()

datas = np.random.randint(100, 130, size=(8, 8))

# 3의 배수, 5의 배수, 15의 배수 위치값에 대한 T, F matrix 생성
idx_3 = datas % 3 == 0
idx_5 = datas % 5 == 0
idx_15 = datas % 15 == 0

# 데이터의 타입을 str으로 변환
result = datas.astype("str")

# T, F matrix를 이용하여 특정 조건의 데이터를 선택 후 브로드캐스팅하게 값을 대임
result[idx_3] = "fiz"
result[idx_5] = "buz"
result[idx_15] = "fbz"

print(result)