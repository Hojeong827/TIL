numbers = [1, 4, 5, 6, 4, 2, 1]
iter_cnt=0

for idx in numbers: # for 문이 얼마나 반복되었는지에 대한 코드
    iter_cnt+=1
    
print(iter_cnt)

iter_cnt=0
for _ in numbers:   # 만약 numbers 안에 있는 원소의 할당이 필요 없다면 변수 지정을 하지 않아도 된다.
    iter_cnt+=1
    
print(iter_cnt)