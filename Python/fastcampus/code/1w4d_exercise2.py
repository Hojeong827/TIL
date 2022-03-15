"""
#a
def plus(a,b):
    print("start")                          # code_1
    result = a+b                            # code_2
    print("result : {}".format(result))     # code_3
    return result

#b
def minus(a,b):
    print("start")                          # code_1
    result = a-b                            # code_4
    print("result : {}".format(result))     # code_3
    return result
"""
#c
def disp(func):
    
    def wrapper(*args, **kwargs):
        print("start")                          # code_1
        result = func(*args, **kwargs)          # code_2, code_4
        print("result : {}".format(result))     # code_3
        return result
    return wrapper

@disp
def plus(a,b):
    result = a+b                            # code_2
    return result

@disp
def minus(a,b):
    result = a-b                            # code_4
    return result
    
plus(1,2)
minus(2,1)