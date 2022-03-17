# Python 1주 5일차 정리

## 생성자
* 클래스가 객체로 생성될 때 실행되는 함수
* 변수(재료)를 추가할 때 사용됩니다.
* 클래스 내에서 특별한 이름(__init__)을 갖기만 하면 객체가 생성될 때 자동으로 호출되는 함수
* 객체를 초기화 하거나 초기값을 설정하는데 유용하게 사용   
[생성자에 대한 추가적인 설명](https://blog.hexabrain.net/285)
<pre><code>
class Calculator:       
    # 생성자 함수 : __init__
    def __init__(self, num1, num2):         # 클래스 안에서 자동으로 호출
        self.num1=num1
        self.num2=num2

    def plus(self):
        return self.num1+self.num2

    def minus():
        return self.mun1-self.num2

calc1=Calculator(3,4)                       # __init__안에 num1과 num2에 값을 설정
calc1.plus()
7
</code></pre>

## 상속
* 기존에 정의한 클래스의 속성 및 기능을 가져다가 그 기능을 그대로 사용, 변경 또는 추가할 때 쓰는 방법
* 중복된 기능을 재정의 할 필요가 없다는 장점
<pre><code>
# plus 기능을 가진 계산기
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def plus(self):
        return self.num1 + self.num2

calc=Calculator(1,2)
calc.plus()

# minus 기능을 추가한 계산기
class Calculator2:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 * self.num2

calc2=Calculator2(1,2)
calc2.plus(), calc2.minus()             # plus와 minus 둘다 기능하지만 코드의 반복으로 인하여 코드의 길이가 불필요하게 늘어남

# 상속을 사용하여 minus 함수를 추가
class Calculator3(Calculator):          #Calculator3 에 Calculator의 기능을 상속
    def minus(self):
        return self.num1 * self.num2

calc3=Calculator3(1,2)
calc3.plus(), calc.minus()              # plus 와 minus 둘다 기능
</code></pre>

## 메서드 오버라이딩(Method Overriding)
* 부모 클래스로부터 상속받은 특정 메소드를 자식 클래스에서 재정의하는 작업을 의미
* ***주의할 점으로 Method Overriding을 활용하면 부모 클래스에서 정의한 메소드의 기능을 자식 클래스에서 재활용이 블가능***
<pre><code>
class Calculator4(Calculator3):
    def plus(self):                    # Calculator3 안에 있는 plus 함수를 다시 재정의하여 기능을 바꿈
        return self.num1**2 + self.num2**2

calc4=Calculator(1,2)
print(calc4.plus())
5
</code></pre>

## Super
* 부모 클래스에서 사용된 함수의 코드를 가져다가 자식 클래스의 함수에서 재사용할 때 사용
<pre><code>
class A:
    def plus(self):
        code1
        
class B(A):
    def minus(self):
        super().plus()      # 이 뜻은 부모 클래스의 plus 함수를 호출한다는 의미이다.
        code2

ex)
class Marine:
    def __init__(self):
        self.health = 40
        self.attack_pow = 5
    def attack(self, unit):
        unit.health -= self.attack_pow
        if unit.health <= 0:
            unit.health = 0

class Marine2(Marine):
    def __init__(self):             # 부모 클래스의 코드를 오버라이딩 했지만 코드의 반복이 있다.
        self.health=40
        self.attack_pow=5
        self.max_health=40

따라서 이를 줄여보자면
claa Marine2(Marine):
    def __init__(self):
        super().__init__()          # super 로 인해서 불필요한 코드의 중복을 줄였다
        self.max_health=40

marine=Marine2()
marine.health, marin.attack_pow, marine.max_health
(40, 5, 40)
</code></pre>