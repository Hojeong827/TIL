# Section 13 마크다운 정리

## Exercise 1-73: 최댓값, 최솟값 구하기(2)
* [exercise1-73](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-73.py)  
    반복문과 조건문을 이용하여서 점수들의 최댓값, 최솟값을 구하는 코드 구현   
    * method 1: 최댓값과 최솟값의 변수들을 scores라는 list 의 0번째 위치의 값으로 초기화 시킨후    
    조건문으로 대소비교를 통해서 최댓값과 최솟값을 찾는 방법   
    * method 2: 최댓값과 최솟값의 변수들을 None 으로 초기화 시켜 조건문으로    
    변수가 None or 대소비교 를 통해서 최댓값과 최솟값을 찾는 방법   

## Exercise 1-74: Normalization
* [exercise1-74](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-74.py)  
    exercise 1-73에서 구한 최댓값과 최솟값을 이용하여서 Normalization을 하는 코드 구현
    * Normalization : 한 특성 내에 가장 큰 값은 1로, 가장 작은 값은 0으로 변환되고 나머지 값들은 0과 1사이의 값들로 변환시켜주는 작업   
    => 수식 : (x-Min)) / (Max-Min)
    * 머신러닝 알고리즘은 데이터가 가진 feature(특성)들을 비교하여 데이터의 패턴을 찾는데 이 데이터가 가지는 feature의 스케일이 심하게 차이가 나는 경우가 문제가 된다.    
    이를 해결하기 위해서 모든 데이터의 포인트가 동일한 정도의 스케일(중요도)로 반영되도록 해주는 것이 정규화(Normalization)의 목표.   

## Exercise 1-75: 최댓값, 최솟값의 위치 구하기
* [exercise1-75](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-75.py)  
    for loop 와 조건문을 이용하여서 최댓값과 최솟값의 위치를 구하는 코드 구현
