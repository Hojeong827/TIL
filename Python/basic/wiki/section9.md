# Section 9 마크다운 정리

## Exercise 1-49: 분산과 표준편차(3)
* [exercise1-49](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-49.py)  
    앞서 배운 분산과 표준편차를 구하는 코드를 for loop와 list 를 이용하여서 구현   
    Exercise 1-26과 비교하면 Exercise 1-26 에서는 인덱스 값에 따른 데이터 값을 모두 더하는 방법으로 평균 및 분산, 표준편차를 구하는 방식이었다.   
    Exercise 1-49에서는 이를 반복적인 작업을 통해서 간단하게 표현하였는데 데이터의 양이 많을 수록 반복문 없이 계속적으로 더하는   
    방식은 코드를 짜는데 있어서 비효율적(코드의 길이 & 시간)이기 때문에 반복문을 통한 코드가 시간 상으로도 더욱 효율적인 모습을 보인다.

## Exercise 1-50: Standardization(3)
* [exercise1-50](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-50.py)  
    Exercise1-49 에서 구한 분산과 표준편차를 이용하여서 for loop와 위차값(index)을 통해 Standardization을 하는 코드 구현   
    Exercise 1-27과 비교해 보았을 때, 1-27 에서는 scores[0]~scores[2]까지의 값을 각각 모두 계산하는 방법을 택했다.    
    하지만 이를 1-49 에서는 반복문과 index값을 이용하여서 모든 socres값의 sum값 뿐만 아니라 square_sum값도 for loop 안에서 처리할 수 있다는 것이 차이이다.   

## Exercise 1-51: 분산과 표준편차(4)
* [exercise1-51](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-51.py)  
    For loop 와 data index를 통해 두 list에 대한 분산과 표준편차를 구하는 코드 구현

## Exercise 1-52: Standardization(4)
* [exercise1-52](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-52.py)  
    Exercise 1-51 과 for loop를 이용하여서 두 list의 Standardization을 구하는 코드 구현