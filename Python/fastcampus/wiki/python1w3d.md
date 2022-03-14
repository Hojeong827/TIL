# Python 1주 3일차 정리

## -함수(Function)
* 함수란 반복되는 코드를 묶음으로서 효율적인 코드를 작성하도록 해주는 기능   
=> 코드를 구현하다보면 반복되는 작업으로 인하여 불필요하게 코드의 길이가 늘어나게 되는데 이를 함수로서 나타내어 간단하게 표현이 가능하다

## -함수 선언 
* 선언 방법 및 구조
<pre><code>def 함수명(매개변수):
    <수행할 문장>
    <수행할 문장>
    ...
</code></pre>
* def 는 함수를 만들 때 사용하는 예약어이다.   
함수명은 마음대로 지정할 수 있으며, 매개변수(parameter)는 이 함수를 호출할 때 전달되는 값을 받는 변수이다.   
<pre><code>
ex) def grade(point):       # 이 함수의 이름은 grade 이며 입력으로 1개의 값을 point라는 매개변수에 받는다
        if point >= 90:
            print("A")
        elif point >=80:
            print("B")
        else:
            print("C")
</code></pre>

## -함수 호출
* 함수를 호출하기 위해서는 함수의 이름과 argument를 호출하면 된다.   
=> 함수가 호출이 되면 함수 안의 코드가 수행이 되며 수행이 완료되면 다시 원래의 코드로 돌아와 다음 코드를 수행하게 된다.   
=> Argument : 함수를 호출할 때 함수에 보내주는 데이터
<pre><code>ex) grade(86)        # grade 함수를 호출하고 86이라는 값을 함수에 전달한다. 이 값을 argument 라고 한다.
    B                # grade 함수에 point라는 매개변수에 86이라는 값을 받게 되고 안에 조건문 명령에 따라서 B를 출력하게 된다.
</code></pre>

## -Parameter & Argument
1. default parameter : argument가 보내주는 값과 parameter가 받아야 하는 값의 개수의 차이가 생겼을 때 이용 가능.
<pre><code>
def add(num1, num2=10):       #  num2 : default parameter, argument에서 값을 다 받지 못하였을 때 default값이 들어간다.
                                => argument가 1개 또는 2개를 받을 수 있는 funciton이 된다.
    print(num1+num2)

add(3,5)
8
add(3)
13
</code></pre>

2. keyword argument : parameter 값이 여러개일 때 그 중 특정 하나의 parameter의 값만 바꾸고 싶을 때 이용 가능.
<pre><code>
def add(num1, num2=10, num3=20):
    print(num1+num2-num3)

add(3, num3=100)        # num2 는 argument에서 지정하지 않아서 default값이 들어가지 않았지만 num3에 100을 지정해 줌으로써
                          default값이 아닌 100이 입력되게 된다. 이렇게 argument 값을 지정하는 것이 key argument이고 순서에 상관없이 
                          쓸 수 있다.
</code></pre>

## Return
* return 은 함수를 실행한 결과를 저장할고 싶을 때 사용. 또한 함수에서 return이 실행이 되면 그 함수는 **무조건 종료가 된다.**
<pre><code>
def plus(num1, num2):    # 함수안에서 출력해주는 명령은 있지만 결과를 보내주는 명령은 없다. 따라서 이를 보내줄 명령이 필요함.
    print(num1+num2)

result = plust(1, 2)
print(result)

3                       # plus 함수 내에서 출력
None                    # main 코드에서 result를 출력했지만 값이 들어있지 않기 때문에 None이 출력됨

따라서 return num1+num2를 plus 함수 안에 넣어주어야 함.

def plus(num1, num2):    
    print(num1+num2)
    return num1+num2    # main 함수의 result라는 변수에 3이라는 값을 보내줌 그리고 함수 종료

result = plust(1, 2)
print(result)

3                       # plus 함수 내에서 출력
3                       # main 코드에서 result안에 1+2=3이라는 결과를 받았기 때문에 3을 출력
</code></pre>

## *args, **kwargs
* 함수를 호출할 때 argument 와 keyword argument의 개수를 특정지을 수 없을 때 사용   
=> *args는 단순 argument만을 받을 수 있고, **kwargs는 keyword argument 만을 받을 수 있다.
<pre><code>
def plus(*args, **kwargs):                
    print(type(args), args)
    print(type(kwargs), kwargs)
    return sum(args)+sum(list(kwargs.values()))     # kwargs는 데이터 값이 dict이기에 key값들의 value들을 list로 만들어야함

print(plus(1,2,3,4,5, num1=6, num2=7))

class 'tuple' (1,2,3,4,5)                           # args의 데이터 타입은 tuple이고 (1,2,3,4,5)가 모두 들어있다.
class 'dict' {'num1': 6, 'num2': 7{}}
28
</code></pre>

* 이와 반대인 예제도 있다
<pre><code>
def func(num1, num2, num3):
    return num1+num2+num3

data=[1,2,3]
print(func(*data))                        # list의 데이터를 하나씩 argument로 호출한다는 뜻!  == func(1,2,3)
6

print(func(data))                         # num1에 data라는 list의 값이 모두 들어가기 때문에 num2와 num3는 값이 비게 된다. 
                                            => 에러 발생! == func([1,2,3])

data = {
    "num2": 100,
    "num3": 200,
}
print(func(1,**data))                     # func(1, num2=100, num3=200)
301
</code></pre>