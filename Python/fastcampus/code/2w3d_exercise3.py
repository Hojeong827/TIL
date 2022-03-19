# reduyce 함수를 구현

# reduce 함수 사용
# reduce(lambda num1, num2: num1+num2, ls)

ls = [1, 2, 3, 4, 5]
def reduce_func(func, ls):
    result = ls[0]
    del ls[0]
    for data in ls:
        result = func(result, data)
    return result

print(reduce_func(lambda num1, num2: num1+num2, ls))