# Section 19 마크다운 정리

## Exercise 1-93: Euclidean Distance(4)
* [exercise1-93](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-93.py)  
    2차원 list를 이용하여서 Euclidean Distance 를 구하는 코드 구현

## Exercise 1-94: 과목별 최고점, 최우수 학생 구하기
* [exercise1-94](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-94.py)  
    2차원 list를 이용한 과목별 최고점 및 최우수 학생을 구하는 코드 구현

## Exercise 1-95: One-hot Encoding
* [exercise1-94](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-95.py)  
    2차원 list를 이용하여 One-hot Encoding을 구하는 코드 구현
    * One-hot Encoding : 단어 집합의 크기를 벡터의 차원으로 하고, 표현하고 싶은 단어의 인덱스에 1의 값을 부여하고, 다른 인덱스에는 0을 부여하는 단어의 벡터 표현 방식이다.    
    이렇게 표현된 벡터를 One-hot Vecotr라고 한다.  
    * [One-hot Encoding](https://wikidocs.net/22647) 
    <pre><code>
    이름 = [쥐, 소, 호랑이] => one_hot_vec = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    이름 = [쥐, 소, 호랑이, 토끼] => one_hot_vec = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    이런식으로 단어의 위치에 1의 값을 부여하고 표현하는 방법을 One-hot Encoding이라고 한다.
    </code></pre>

## Exercise 1-96: Accuracy 구하기(2)
* [exercise1-96](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-96.py)  
    Exercise 1-94에서 구한 One-hot Encoding을 이용하여서 예측값과 실제값 사이의 정확성을 측정하는 코드 구현