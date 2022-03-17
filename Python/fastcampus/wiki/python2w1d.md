# Python 2주 1일차 정리

## Class의 getter, setter
* 객체의 내부 변수에 접근할 때 특정 로직을 거쳐서 접근시키는 방법
* 클래스에서 메서드를 통해 속성의 값을 가져오거나 저장하는 경우, 값을 가져오는 메서드를 getter, 값을 저장하는 메서드를 setter라고 한다.   
* [getter와 setter의 추가 설명](https://jinmay.github.io/2019/11/23/python/python-class-first/)   
<pre><code>
class User:

    def __init__(seflf, first_name):
        self.first_name = first_name

    def setter(self, first_name):           # 3글자 이상부터 이름이 바뀔 수 있게 하는 조건
        if len(first_name) >= 3:
            self.first_name = first_name
        else:
            print("error")

    def getter(self):                       # 출력은 대문자로 출력하는 조건
        print("getter")
        return self.first_name.upper()
    
    name = property(getter, setter)         # property : name 이라는 변수에 getter와 setter에 접근할 수 있도록 함

user1 = User("andy")

# setter 함수 실행
user1.name = "a"
error                   # 조건에 성립하지 않기 때문에 error
user1.name = "jhon"     
user1.first_name
'jhon'                  # 조건에 성립하기 때문에 first_name이 jhon으로 바뀜(저장)

# getter함수 실행
user1.name
getter
'JHON'                  # 저장은 jhon으로 되어있지만 출력은 JHON으로 출력(값을 가져와 출력)

</code></pre>

## Non public
* magling 이라는 방법으로 다이렉트로 객체의 변수에 접근하지 못하게 하는 방법
<pre><code>
class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        # self.__num2 = num2              # num2 앞에 __붙은 것이 magling => 다이렉트로 접근이 불가하게 함
                                          # magling 에 의해서 실제로는 self._Calculator__num2 = num2 로 바뀌어서 저장
    
    def getter(self):
        return self.num2
        # return self.__num2

    # num2에 0이 들어가지 않도록 함
    def setter(self):
        num2 = 1 if num2==0 else num2
        self.num2 = num2
        # self.__num2 = num2
    
    def __disp(self):                     # magling은 함수에도 적용이 가능하다.
        print(self.num1, self.__num2)

    def div(self)
        self.__disp()
        return self.num1 / self.num2
        # return self.num1 / self.__num2

    number2 = property(getter, setter)

---------출력-----------
calc = Calculator(1,2)
calc.div()
0.5
calc.number2=0              # calc.number2에 0대신 1이 들어감
calc.num2=0                 # setter나 getter를 거치지 않고 다이렉트로 num2의 값에 접근했기때문에 0으로 바뀜
calc.div()                  # 0으로 나눌 수 없기 때문에
error!

***mangling 적용 후!***

calc.__num2                 # __init__의 __num2가 출력이 되어야 하는데 없는 변수로 나옴, error
error!
calc._Calculator__num2      # magling 에 의해서 변수 명이 바뀌어서 저장되었기 때문에 calc._Calculator__num2로 호출
2
=> 즉 setter함수를 거쳐야 함
calc.num2=0                 # 이는 Calculator 안에 num2라는 변수가 생성된거지 _Calculator__num2에 영향을 끼치지 않는다
calc.__num2=0               # 이러한 경우도 위와 마찬가지이다.
calc.__disp()               # 함수 또한 magling이 적용되었기 때문에 error가 발생한다.
</code></pre>

## is a & has a
* 클래스를 설계하는 개념   
* A is a B : A는 B 이다, 상속을 이용해서 클래스를 만드는 방법   
* A has a B: A는 B를 가진다, A가 B객체를 가지고 클래스를 만드는 방법   
<pre><code>
# 사람 : 이름, 이메일, 정보출력()
# is a
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
class Person2(Person):
    def info(self):
        print(self.name, self.email)

p=Person2("andy", "andy@gmail.com")     # Person2 는 Person을 상속받음
p.info()
andy andy@gmail.com

# has a
class Name:
    def__init__(self, name):
        self.name_str=name

class Email:
    def__init__(self, email):
        self.email_str=email

class Person:
    def __init__(self, name_obj, email_obj):
        self.name=name_obj
        self.email=email.obj
    def info(self):
        print(name.name_str, email.email_str)
name=Name("andy")
emil=Email("andy@gmail.com")
p=Person(name, email)           # 객체안에 객체를 넣어 호출, p객체는 name과 email의 객체를 가짐
</code></pre>

## Magic(Special) Method
* Python에 있는 여러 내장 함수들이 호출하는 메서드를 사용자 정의객체에 정의해서 내장함수를 사용할 수 있도록 하는 것
* compare   
    1. '__eq__' : ==
    2. '__ne__' : !=
    3. '__lt__' : <
* calculater
    1. '__add__' : +
    2. '__sub__' : -
* __repr__ : 객체의 내용을 출력(개발자용)
* __str__ : 객체의 내용을 출력   
* [스페셜 메소드에 대한 추가적인 설명](https://velog.io/@xchdtk/Python-Special-MethodMagic-method)