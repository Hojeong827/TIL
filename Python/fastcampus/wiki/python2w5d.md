# Python 2주 5일차 정리

## Pandas Pivot
* 데이터 프레임의 컬럼 데이터에서 index, column, value를 선택해서 데이터 프레임을 만드는 방법
* 작성법
    1. 'df.pivot(index, columns, values)' : groupby 하고 pivot을 실행
    2. 'df.pivot_table(values, index, columns, aggfunc)' : groupby를 하지 않고 pivot을 실행
<pre><code>
ex) 데이터 프레임 하나를 예시로 들자면
index   A   B   C
  1     a   1   100
  2     b   2   200
  3     c   3   300
  4     d   4   400
  
  A column의 값이 index가 되고, B column의 값이 column이 되고 C column의 값이 value값이 된다고 하면

  index     1   2   3   4
    a      100 NaN NaN NaN
    b      NaN 200 NaN NaN
    c      NaN NaN 300 NaN
    d      NaN NaN NaN 400

pivot을 통해서 새로운 데이터 프레임을 생성할 수 있다.
</code></pre>

## Pandas io(input, output)
* 데이터 프레임을 저장, 로드
<pre><code>
# load
result = pd.read_csv(파일명)

# save
result.to_cdv(파일명, index=False)  # 보통 index값은 저장하지 않는다(저장공간을 줄이기 위해서)
</code></pre>

## 선형회귀분석 (Linear Regression())
* 선형회귀란?     
머신 러닝의 목적으로는 실제 데이터를 바탕으로 모델을 생성해서 만약 다른 입력값을 넣었을 때 발생할 출력값을 예측하는데 있다.    
이 때 우리가 찾아낼 수 있는 가장 직관적이고 간단한 모델이 선(line)이다.    
그래서 데이터를 놓고 그걸 가장 잘 설명할 수 있는 선을 찾는 분석하는 방법을 선형회귀분석(linear regression)이라고 한다.   
* [선형회기분석 자세히](https://hleecaster.com/ml-linear-regression-example/)
* scikit-learn 패키지
    1. 데이터 마이닝 및 데이터 분석, 모델을 위한 도구
    2. 상업적으로 사용이 가능한 오픈소스
* 분석 절차
    1. 데이터 로드
    2. 데이터 전처리
        - 독립변수와 종속변수를 나눠줌
        - 학습 데이터와 테스트 데이터를 나눠줌
    3. 데이터 분석 : 선형회귀 모델
    4. 성능평가 : MAE
    5. 예측 코드 작성