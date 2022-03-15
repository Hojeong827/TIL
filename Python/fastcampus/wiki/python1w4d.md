# Python 1주 4일차 정리

## -Scope 범위
* 함수 안에서 선언되는 변수와 함수 밖에서 선언되는 변수의 범위가 다르다.
* global(전역), local(지역)
1. Global(전역) 변수 : 함수 외부에서 선언된 변수로서 모든 함수에서 접근 가능
<pre><code>ex)
gv=10               # global 함수 : 함수 안과 밖에서 사용될 수 있는 변수
def echo():
    print(gv)
echo()
10
</code></pre>   

2. Local(지역) 변수 : 함수 내에서 선언된 변수로서 선언된 함수 내에서만 사용 가능
<pre><code>ex)
gv=10
def echo():
    gv=100          # local 함수 : 함수 안에서만 사용되는 변수.
    print(gv)
echo()              # echo안에서 gv가 선언되었고, echo함수를 호출하였기 때문에 100이 출력.
100
gv                  # global 함수를 출력하는 것이기 때문에 10이 출력.
10
------------------------------------------------------------------------------------------------------------------------
만약 지역변수의 값을 전역변수로서 쓰고 싶다면 global 이라는 명령어를 쓰면 된다.

gv=10
def echo():
    global gv       # 함수 안에서 지역변수를 전연변수로 참조하기 위해 선언.
    gv=100          # 전역변수 gv는 10의 값이 아닌 100의 값으로 바뀌게 된다.
echo()              # 하지만 이렇게 선언이 되어야지 선언이 되지 않으면 바뀌지 않는다.
gv
100
</code></pre>

## -Inner Function
* 함수가 지역영역에 선언, 함수 안에서 선언된 함수를 inner function 이라고 불린다   
=> 루프나 코드 중복을 피하기 위해서 또는 다른 함수 내에 어떤 복잡한 작업을 한 번 이상 수행할 때 유용하게 쓰인다.
<pre><code>
def outer (a,b):
    def inner (c,d):        # scopre 가 지역 함수이기 때문에 outer 안에서만 쓸 수 있다
        return c+d          
    return inner (a,b)      # outer를 호출 받아 1,2라는 값을 받고 return 에서 inner를 호출->inner가 1,2를 받아 3을 return
outer(1,2)
3
inner(3,4)         #지역 함수는 전역영역에서 사용이 불가하기 때문에 error 가 발생
error
</code></pre>
* 이러한 inner function을 전역 영역에서 쓰는 방법이 있다.
<pre><code>
def outer(a,b):
    def inner(c,d):
        return c+d
    return inner
outer(1,2)(3,4)             # outer 함수 선언을 하여 1,2 값을 보내지만 쓰이지 않고 return inner로 인해 3,4의 값을 보냄
                            # 즉 outer(1,2)(3,4) == inner(3,4) 와 같다.
7
</code></pre>

## -Call Back Function
* 함수를 argument, parameter 로 설정해서 사용
<pre><code>
def calc(func, a,b):    # 함수의 parameter에 다른 함수가 들어가 있고 이를 call back function이라고 부른다.
    return func(a,b)
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
calc(plus, 1, 2)        # 덧셈, plus 함수가 argument로 들어가 있다.
3
calc(minus, 2,1)        # 뺄셈, minus 함수가 argument로 들어가 있다.
1
</code></pre>

## -Lambda Function
* Parameter 를 간단한 계산으로 리턴되는 함수 : 삼항연산
* 선언 방법 : 함수명 = lambda a, b(parameter) : a+b(리턴되는 값)
<pre><code>
def plus(a,b):
    return a+b
plus(1,2)
3

위의 함수는 아래의 함수와 동일하다

plus = lambda a, b: a+b
plus(1,2)
3

이러한 lambda 함수는 call back function 안에 argument로 들어갈 수 있다.
def calc(func, a, b):                    # func 안에 lambda a,b: a*b가 들어가게 된다.
    a**=2
    b**=2
    return func(3,4)
calc(lambda a,b:a*b, 3,4)               # 이렇듯 미리 함수를 선언할 필요가 없다.
144
</code></pre>

## Map, Filter, Reduce
1. Map : 순서가 있는 데이터 집합에서 모든 값에 함수를 적용시킨 결과를 출력해주는 함수
* 선언 방법 : map(func, *iterable data(list 나 tuple, dict는 안됨))
<pre><code>
ls = [1, 2, 3, 4]

def odd_even(num):
    return "odd" if num % 2 else "even"     # num % 2 == 1(참) 이면 odd return 0(거짓)이면 even return

odd_even(3), odd_even(4)
('odd', 'even')
list(map(odd_even, ls))                     # ls 의 모든 값을 odd_even의 함수에 넣어서 결과값을 list에 저장
['odd', 'even', 'odd', 'even']
</code></pre>

2. Filter : 리스트 데이터에서 특정 조건에 맞는 value만 남기는 함수
* 선언 방법 : filter(func or none, iterable data)   => return only function is true
<pre><code>
ls = range(10)
list(filter(lambda data: True if data%2 else False, ls))
[1, 3, 5, 7, 9]             # ls 의 모든 값들이 lambda function에 의해서 True와 False로 정해지고 True인 값들만 filter되었음
</code></pre>

3. Reduce : 리스트 데이터를 처음부터 순서대로 특정 함수를 실행하여 결과를 누적시켜주는 함수
* 선언 방법 : reduce(func, sequence[, initial]) -> value   
=> ex) reduce(lambda x,y : x+y, [1,2,3,4,5]) => calculates ((((1+2)+3)+4)+5).   
=> 즉 1+2의 결과를 누적 => (1+2)+3의 결과를 누적 => 반복.... 즉 결과가 lambda의 x값으로 다음 순서의 값이 y로 들어감   
   
## Decorlator
* 코드를 바꾸지 않고 기능을 추가하거나 수정하고 싶을 때 사용하는 문법   
* Decorlator 의 사용법
<pre><code>
def c(func):            # func는 a()함수 (또는 b()함수) 를 받게된다. 그리고 이 func가 decorlator function이 된다.

    def wrapper(*args **kwargs):            # wrapper 함수 선언
        code_1
        result = func(*args, **kwargs)      # func는 a()함수(또는 b()함수)이기에 code_1, code_2, code_3가 실행
        code_3
        return result
    
    return wrapper      # wrapper 실행

@c                      # @c를 쓰면 def c가 실행이 되고, a()함수가 c 함수의 parameter 로 들어가게 된다.
def a():
    code_2

@c                      # @c를 쓰면 def c가 실행이 되고, b()함수가 c 함수의 parameter 로 들어가게 된다.
def b():
    code_4
</code></pre>
*[exercise1](https://github.com/Hojeong827/TIL/blob/main/Python/fastcampus/code/1w4d_exercise2.py)   
*[exercise2](https://github.com/Hojeong827/TIL/blob/main/Python/fastcampus/code/1w4d_exercise3.py)   
*[exercise3](https://github.com/Hojeong827/TIL/blob/main/Python/fastcampus/code/1w4d_exercise4.py)   