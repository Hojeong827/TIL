import numpy as np

# 1.부터 20까지 랜덤한 숫자를 가지는 5*5 행렬 생성
# 최대값에는 MAX, 최소값에는 MIN 문자열이 들어가도록 치환하는 코드
# 최대값과 최소값 함수 : np.max(nndarray), np.min(ndarray)

datas = np.random.randint(1, 20, (5,5))
print(datas)

min_num, max_num = np.min(datas), np.max(datas)
print(min_num, max_num)

idx_min = datas == min_num
idx_max = datas == max_num

result = datas.astype("str")

result[idx_min] = "MIN"
result[idx_max] = "MAX"

print(result)