# Section 16 마크다운 정리

## Exercise 1-82: Nested List 만들기 & 원소 접근하기
* [exercise1-82](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-82.py)  
    List로 2차원 배열을 만드는 방법과 각 원소에 접근하면 나오는 결과를 도출하는 코드 구현   
<pre><code>
scores = [[10,20,30], [50, 60, 70]]     # 2차원 배열을 만드는 법은 list 안에 list 를 넣는 방법이 있다.
print(scores)
[[10, 20, 30], [50, 60, 70]]

print(scores[0])                        # socres의 0번째 위치는 socres안의 첫번째 list의 위치
[10, 20, 30]

print(scores[1])
[50, 60, 70]

print(scores[0][0], scores[0][1], scores[0][2])     # 2차원 list 안의 원소를 호출하기 위해서는 두 list의 위치값이 필요
10 20 30

print(scores[1][0], scores[1][1], scores[1][2])
50 60 70
------------------------------------------------------------------------------------------------------------------------
score=[[10, 20], 30, 40]        # list 안에 list가 존재가 가능하지만 원소도 또한 같이 존재할 수 있다.
print(scores)
[[10, 20], 30, 40]

print(scores[0])
[10, 20]
print(scores[1])
30
print(scores[0][1])
20
</code></pre>

## Exercise 1-83: Nested List 원소 접근하기(2)
* [exercise1-83](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-83.py)  
    2차원 list와 반복문을 이용하여서 List의 각 원소에 접근하는 코드 구현

## Exercise 1-84: 학생별 평균점수 구하기
* [exercise1-84](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-84.py)  
    2차원 배열을 이용하여 학생별 평균 점수를 구하는 코드 구현

## Exercise 1-85: 과목별 평균점수 구하기
* [exercise1-85](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-85.py)  
    2차원 배열을 이용하여 과목별 평균 점수를 구하는 코드 구현