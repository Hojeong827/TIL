# map 함수를 map_func 함수의 이름으로 구현하세요.
# 리스트의 데이터를 아래의 예제와 같이 더하는 함수를 만드는데 따로 함수를 선언해서 사용하지 말고 map의 첫번째
# 파라미터에 lambda 함수로 구현하세요
# zip(args) : zup((ls1, ls2, ls3))
# zip(*args) : zip(ls1, ls2, ls3)

ls1 = [1, 2, 3, 4]
ls2 = [5, 6, 7]
ls3 = [9, 10, 11, 12]
# list(map(lambda *args : sum(args), ls1, ls2, ls3))

def map_func(func, *args):
    return [func(*datas) for datas in zip(*args)]

print(list(zip(ls1, ls2, ls3)))
print(map_func(lambda *args : sum(args), ls1, ls2, ls3))