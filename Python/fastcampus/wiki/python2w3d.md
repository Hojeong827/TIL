# Python 2주 3일차 정리

## 상관 계수(Correlation Coefficient)
* Index
    1. 분산
    2. 공분산
    3. 상관계수
    4. 결정계수

<pre><code>
import numpy as np

data1 = np.array([80, 85, 100, 90, 95])
data2 = np.array([70, 80, 100, 95, 95])
</code></pre>

## 분산(Variance)
* 1개의 이산정도를 나타냄
* 편차제곱의 평균 : variance = sigma(value-average)^2 / n
<pre><code>
# variance code
def variance(data):
    
    avg = np.average(data)
    var = 0

    for num in data:
        var += (num-abg)**2

    return var

print(variance(data1), variance(data2))         # (50.0, 126.0)
%%time
variance(p_data1)                               # Wall time: 518ms

* numpy 패키지를 이용
print(np.var(data1), np.var(data2))             # (50.0, 126.0)
%%time
variance(p_data1)                               # Wall time: 2.94ms  =>  일반함수보다 월등히 빠름
표준편차 : np.std(data1)
</code></pre>

## 공분산(covariance)
* 2개의 확률변수의 상관정도를 나타냄
* 평균 편차곱 : covariance = sigma(x_value-x_average)(y_value-y_average) / n
* 방향성은 보여줄 수 있으나 강도를 나타내는데 한계가 있다. 데이터의 크기에 따라서 값의 차이가 크다는 단점
* numpy 를 이용한 코드 : np.cov(data1, data2)
* 출력 => array([data1 by data1, data1 by data2], [data2 by data1], [data2 by data2]) 의 형태로 출력
* 우리가 필요한 값은 data1 과 data2 상관정도이기 때문에 array[0][1] 또는 array[1][0]을 사용
* 즉 np.cov(data1, data2)[0, 1] 사용!

## 상관계수(correlation coefficient)
* 공분산의 한계를 극복하기 위해서 만들어짐.
* -1 ~ 1까지의 수를 가지며 0과 가까울 수록 상관도가 적음을 의미
* 1에 가까울 수록 같이 움직임, -1에 가까울 수록 반대로 움직임
* x의 분산과 y의 분산을 곱한 결과의 제곱근을 나눠주면 x나 y의 변화량이 클수록 0에 가까워짐
* numpy 를 이용한 코드 : np.corrcoef(data1, data2)[0, 1] ([0, 1]은 위의 공분산과 같은 이유)

## 결정계수(coefficient of determination: R-sqaured)
* x로부터 y를 예측할 수 있는 정도
* 상관계수의 제곰 (상관계수를 양수화)
* 수치가 클 수록 회기분석을 통해 예측할 수 있는 수치의 정도가 더 정확
* np.corrcoef(data1, data2)[0, 1]**2

## linspace, logspace 함수
* linspace : 설정한 범위에서 선형적으로 분할한 위치의 값을 출력   
=> np.linspace(0, 100, 5)       :           array([ 0., 25., 50., 75., 100.])
* logspace : 설정한 범위에서 로그로 분할한 위치의 값을 출력   
=> np.logspace(2, 4, 3)         :           array([ 100., 1000., 10000.])

## numpy random
* seed : 랜덤값의 설정값
* rand : 0 에서 1 사이의 균등분포로 난수를 발생
* randn : 0에 가까운 정규분포로 난수를 발생
* randint : 균등분포로 정수값을 발생
* suffle : 행렬 데이터를 섞어 줍니다.
* choice : 특정 확률로 데이터를 선택
* unique : 어떤 원소가 나왔는지와 그 원소들이 몇번 반복되었는지 알기 위한 함수

## 행렬 데이터의 결합
* concatenate
<pre><code>
na1 = np.random.randint(10, size=(2,3))         # array([[3, 0, 0], [5, 7, 5]])
na2 = np.random.randint(10, size=(3,2))         # array([[0, 8], [6, 5], [1, 7]])
na3 = np.random.randint(10, size=(3,3))         # array([[4, 3, 6], [1, 4, 0], [8, 5, 4]])

# 세로 결합
np.concatenate((na1, na3))                      # na1 과 na2는 배열크기가 다르기 때문에 불가
=> array([[3, 0, 0], 
          [5, 7, 5], 
          [4, 3, 6], 
          [1, 4, 0], 
          [8, 5, 4]])

# 가로 결합
np.concatenate((na2, na3), axis=1
=> array([0, 8, 4, 3, 6], 
         [6, 5, 1, 4, 0], 
         [1, 7, 8, 5, 4]]))

# c_, r_                                        # column, row
np.c_[np,array([1, 2, 3]), np,array([4, 5, 6])]
=> array([[1, 4],
          [2, 5],
          [3, 6]])

np.r_[np,array([1, 2, 3]), np,array([4, 5, 6])]
=> array([1, 2, 3, 4, 5, 6])
</code></pre>