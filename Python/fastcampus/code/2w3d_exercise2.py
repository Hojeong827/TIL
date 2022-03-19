# filter 함수를 구현하여 1~10까지의 숫자에서 홀수만 출력하는 코드를 작성하세요

ls = range(1,11)

# filter 함수 사용
# list(filter(lambda number: number % 2, ls))

def filter_func(func, datas):
    return [data for data in datas if func(data)]

print(filter_func(lambda number : number % 2, ls))