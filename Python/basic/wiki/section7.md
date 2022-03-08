# Section 7 마크다운 정리

## Exercise 1-36: for loop으로 list의 원소 접근하기
* [exercise1-36](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-36.py)  
    For loop를 이용하여 list의 원소들에 차례대로 접근하는 코드 구현   
    For loop의 형식 : for (변수) in (list 또는 range를 이용하여 반복 횟수 지정):  

<pre><code>
    scores = [10, 20, 30]
    for score in scores:      # scores 안에 있는 원소들에 대해서 하나씩 접근을 하고 이를 scroe 라는 변수에 할당을 한다.
                              # 첫번째 loop에 socre 에 10이라는 원소가 할당, 두번째에는 20, 세번째에는 30이 할당된다.
        print score
</code></pre>

<pre><code>
    위의 반복문은 아래의 코드와 같다.   
    score = scores[0]   
    print(score)   
    score = scores[1]   
    print(score)   
    core = scores[2]   
    print(score)   
</code></pre>

## Exercise 1-37: List 원소들의 합 구하기
* [exercise1-37](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-37.py)  
    For loop를 이용하여 list 안의 원소들의 합을 구하는 코드 구현   

## Exercise 1-38: Iteration 횟수 구하기
* [exercise1-38](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-38.py)  
    For loop를 이용하여 Iteration 횟수 구하는 코드 구현   
    * for loop 에서 list 의 원소를 할당받을 변수가 필요 없거나 단순 반복만을 원한다면 변수 지정을 하지 않아도 된다.   
      ex) for _ in scores: => scores라는 리스트의 원소의 갯수만큼 단순 반복   

## Exercise 1-39: 1 부터 100까지의 합 구하기
* [exercise1-39](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-39.py)  
    For loop와 range() 를 이용하여 1부터 100까지의 합을 구하는 코드 구현   

## Exercise 1-40: 1 부터 100까지의 List 만들기
* [exercise1-40](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-40.py)  
    For loop, list(), append(), range() 를 이용하여 1부터 100까지의 List 를 만드는 코드 구현   

## Exercise 1-41: 100개의 0을 가진 List 만들기
* [exercise1-41](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-41.py)  
    For loop, list(), append(), range() 를 이용하여 100개의 0을 가진 List를 만드는 코드 구현   

## Exercise 1-42: for loop 으로 List 의 원소 접근하기(2)
* [exercise1-42](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-42.py)  
    For loop, range(), len()를 이용하여 list 의 원소에 접근하는 코드 구현   
    * list 의 원소에 접근하기 위해서는 index값 (위치 값) 이 필요한데 이를 for loop와 range(), len()를 이용하여 구현할 수 있다.   
    <pre><code>
    scores = [10, 20, 30, 40, 50]
    for score_idx in range(len(scores)):    #   len()를 이용하여 socres라는 list의 길이를 알아내어 
                                                range() 안에 넣음으로써 위치값을 score_idx에 넣는다.
        print(scores[score_idx])            #   그러면 scores의 index(위치값)에 따라서 출력을 할 수 있다.
    </code></pre>

## Exercise 1-43: for loop 으로 List 의 원소 수정하기
* [exercise1-43](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-43.py)  
    Exercise 1-42에서 index를 구하는 방법과 For loop를 이용하여서 List의 원소를 수정하는 코드 구현

## Exercise 1-44: 두 개의 List 접근하기
* [exercise1-44](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-44.py)  
    Exercise 1-44에서 index를 구하는 방밥과 For loop와 index값을 이용하여서 두개의 List에 접근하는 코드 구현