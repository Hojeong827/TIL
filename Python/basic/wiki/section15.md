# Section 15 마크다운 정리

## Exercise 1-77: Accuracy 구하기
* [exercise1-77](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-77.py)  
    for loop와 조건문을 이용하여 예측값과 실제값을 이용한 accuracy를 구하는 코드 구현

## Exercise 1-78: Confusion Vector 구하기
* [exercise1-78](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-78.py)  
    exercise1-77에서 배운 accuracy를 구하는 방법을 이용하여 Confusion Vector를 구하는 코드 구현   
    * Confusion Vector (혼돈 행렬): 분류가 Y, N 두 종류가 있다고 할 때, 모델에서 구한 분류의 예측값과 데이터의 실제값의 발생 빈도를 나열한 행렬  
    => 분류 모델의 학습 성능 평가를 위한 행렬   
    [Confusion Vector의 자세한 설명은 링크 참조](https://nittaku.tistory.com/294)
    <pre><code>
    predictions = [0, 1, 0, 2, 1, 2, 0]
    labels = [1, 1, 0, 0, 1, 2, 1]
    M_class = None                      # M_class는 labels 안에 원소들이 0에서 부터 몇까지 있는지를 판별하는 변수
                                          M_class가 3이면 labels 안에 0, 1, 2가 존재.
    for label in labels:
        if M_class==None or label> M_class:
            M_class = label
    M_class+=1
    class_cnts, correct_cnts, confusion_vec = list(), list(), list()
    for _ in range(M_class):            # 초기화시키는 작업
        class_cnts.append(0)            # class_cnt의 위치값이 의미하는 것은 labels에서 0, 1, 2가 몇개가 존재하는지의 의미
                                          ex) class_cnt[0]=4 => labels 안에서 0이 4개가 존재
        correct_cnts.append(0)          # correct_cnt의 위치값이 의미하는 것은 예측값과 실제값이 몇개가 일치하는지의 의미
                                          ex) correct_cnt[0]=2 => predictions와 labels에서 0의 위치가 2개가 일치.
        confusion_vec.append(None)
    
    for pred_idx in range(len(predictions)):        # 예측값과 실제값이 동잃한지 판단하는 반복문
        pred=predictions[pred_idx]
        label=labels[pred_idx]
    
        class_cnts[label]+=1                        # labels안에서 동일한 원소가 몇개가 있는지 원소별로 갯수를 세는 작업
        if pred == label:                           # 예측값과 실제값이 동일하다면 correct_cnt 횟수 증가
            correct_cnts[label]+=1
        
    for class_idx in range(M_class):                # confusion_vector 구하기 (각 원소별로 맞춘값 / 원소별 원소의 갯수)
        confusion_vec[class_idx] = correct_cnts[class_idx]/class_cnts[class_idx]
    print("confusion vector: ", confusion_vec)
    </code></pre>


## Exercise 1-79: Histogram 구하기
* [exercise1-79](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-79.py)  
    for loop와 조건문을 이용하여 histogram을 구하는 코드 구현   
    * Histogram : 도수분포를 나타내는 그래프를 말하며 흔히 기둥그래프를 의미.   
    => 코드 내에서는 기둥의 크기를 숫자로 표현

## Exercise 1-80: 절댓값 구하기
* [exercise1-80](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-80.py)  
    for loop 와 조건문을 이용하여 원소들의 절댓값을 가지는 list를 만드는 코드 구현

## Exercise 1-81: Manhattan distance
* [exercise1-81](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-81.py)  
    Exercise 1-80에서 절댓값을 만드는 방법을 이용하여 Manhattan distance를 계산하는 코드 구현   
    * [Manhattan distance](https://needjarvis.tistory.com/455)
    => 두 점 (x1, y1), (x2, y2) 사이의 멘하튼 거리를 구하는 공식 : |x1-x2| + |y1-y2|   