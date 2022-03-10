# Section 11 마크다운 정리

## Exercise 1-60: 합격 알려주기
* [exercise1-60](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-60.py)  
    조건문 if의 기본적인 사용법을 익히는 코드 구현
    * 조건문 if 란 "만약에" 에 대한 처리를 하게 해주는 명령문, 주로 대소비교를 이용 (참이면 1 거짓이면 0)   
    * 쓰는 법 : if (조건문):    
    => : 파이썬에서는 다음 줄에 문법이 이어집니다의 의미.   
    * 예시로 if a>10: 이라는 조건문을 만들었을 때 a가 10 보다 크다면 다음 문법을 이어나가지만    
    그렇지 않다면 조건문 안에 있는 명령문을 실행하지 않는다.
    * 비교 연산의 종류   
    <pre><code>
    1. ==, !=  : 같은지 다른지를 비교하는 연산자
       a, b = 10, 20
       if a != b:
            print("같다")    
    2. <, >, >=, <= : 대소비교하는 연산자
       a, b = 10, 20
       if a < b
            print("b가 a 보다 크다")
    </code></pre>
    * 논리 연산의 종류
    <pre><code>
    1. and, or, not
        a and b : 조건문 a와 b가 모두 만족되어야 참
        a or b : 조건문 a 또는 b가 만족되면 참
        not a : 조건문 a 가 거짓이면 참
    2. in, not in : 특정 자료형 안에 하나의 요소가 있는지 없는지를 판별하는 연산자
       if 10 in [10, 11, 12]
            print("10 이 포함되어 있음")    # 10이 자료형안에 있으므로 참
    </code></pre>


## Exercise 1-61: 합격/불합격 알려주기
* [exercise1-61](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-61.py)  
    조건문 if 와 else의 사용법을 익히는 코드 구현   

## Exercise 1-62: 초를 분초로 표현하기
* [exercise1-62](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-62.py)  
    if 와 else를 이용하여서 초를 분초로 표현하는 코드 구현

## Exercise 1-63: 초를 시분초로 표현하기
* [exercise1-63](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-63.py)  
    elif의 기본적인 사용법과 이를 이용하여서 초를 시분초로 표현하는 코드 구현   
    * if : 만약에, elif : 만약에 그렇지 않다면 다른 조건은?, else : 만약에 그렇지 않다면    
    => 무조건 if 다음에 elif 그리고 else 순으로 작성되어야 한다.
    
## Exercise 1-64: 홀수 짝수 구하기
* [exercise1-64](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-64.py)  
    조건문인 if 와 else 를 이용하여서 홀수/짝수 를 구하는 코드 구현

## Exercise 1-65: 두 수 비교하기
* [exercise1-65](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-65.py)  
    조건문을 이용하여서 두 수 를 비교하는 코드 구현

## Exercise 1-66: 성적으로 평점으로 바꾸기
* [exercise1-66](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-66.py)  
    조건문을 이용하여서 성적을 평점으로 바꾸는 코드 구현