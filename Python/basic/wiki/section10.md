# Section 10 마크다운 정리

## Exercise 1-53: Hadamard Product(4)
* [exercise1-53](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-53.py)  
    For loop를 이용하여서 Hadamard Product를 하는 코드 구현   
    exercise 1-28 에서는 list 의 원소들 각각을 가지고 계산을 했다면 1-53에서는 반복문을 통한 계산을 실행   
    * method 1: list v3를 만들어서 for loop 안에서 차례대로 계산한 값을 append() 하는 방법
    * method 2: 3개의 공간을 가진 list v3를 만들어 0으로 초기화 한 뒤 for loop 안에서 계산한 값을 집어 넣는 방식   
    => method 1에서는 계산된 값이 생길 때마다 공간을 만들어서 하나씩 집어 넣었다면    
    method 2에서는 미리 공간을 만들어서 그 공간에 값을 집어 넣는 것이 차이점이다.   

## Exercise 1-54: Vector Norm(3)
* [exercise1-54](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-54.py)  
    For loop를 이용하여 Vector Norm을 구하는 코드 구현   
    exercise 1-31 에서도 또한 list의 원소들 각각을 가지고 계산을 한 것을 for loop 의 변수 할당을 이용하여서 계산.
    <pre><code>
    v1=[1,2,3]
    for dim_val in v1:
        square_sum+=dim_val**2  # for문에 할당된 변수를 이용하여 계산.
    norm = squre_sum**0.5
    </code></pre>

## Exercise 1-55: Making Unit Vectors(3)
* [exercise1-55](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-55.py)  
    Exercise 1-54에서 구한 Vector Norm 과 index값 을 이용하여서 Unit Vector를 만드는 코드 구현

## Exercise 1-56: Dot Product(3)
* [exercise1-56](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-56.py)  
    For loop 를 이용하여서 Dot product 를 하는 코드 구현

## Exercise 1-57: Euclidean Distance(3)
* [exercise1-57](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-57.py)  
    For loop 를 이용하여서 Euclidean Distance 를 구하는 코드 구현

## Exercise 1-58: Mean Squared Error(3)
* [exercise1-58](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-58.py)  
    For loop 를 이용하여서 Mean Squared Error 를 구하는 코드 구현

## Exercise 1-59: 숫자 빈도 구하기
* [exercise1-59](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-59.py)  
    For loop 를 이용하여서 중복된 숫자의 횟수를 구하는 코드 구현
    <pre><code>
    numbers = [0,2,4,2,1,4,3,1,2,3,4,1,2,3,4]
    number_cnt=[0,0,0,0,0]
    for num in numbers:
        number_cnt[num]+=1      # numbers의 원소들이 num이라는 변수에 차례대로 할당 
                                => number_cnt의 num 번째의 값을 증가시켜준다 
                                => number_cnt의 num 번째의 값 = num 이 반복된 횟수
                                (c++와 다르게 python에서는 number_cnt++ 이라는 명령어는 듣지 않는다.)
    </code></pre>