# Python 2주 4일차 정리

## Pandas
* 데이터 분석을 위한 사용이 쉽고, 성능이 좋은 오픈소스 python 라이브러리
* R 과 Pandas 의 특징
    - R보다 Pandas 가 학습이 쉽다.
    - R보다 Pandas 가 성능이 좋다.
    - R보다 Python은 활용할 수 있는 분야가 많다.
* 크게 두가지 데이터 타입을 사용합니다.
    - Series : index 와 Value로 이루어진 데이터 타입
    - DataFrame : index(row), column, value로 이루어진 데이터 타입

## Series
* 동일한 데이터 타입의 값을 가진다.
* Series : value 만 설정하면 index는 0부터 자동으로 설정
<pre><code>
import numpy as np
import pandas as pd

data = pd. Series(np.rnadom.randint(10, size=5))
print(data)
0 5
1 5
2 3
3 0
4 3
dtype : int64

# index 설정
data = pd.Series(np.random.randint(10, size=5), index=list("ABCDE"))
print(data)
A 3
B 7
C 3
D 3
E 6
dtype: int64

print(data.index, data.values)
(Index(['A', 'B', 'C', 'D', 'E'], dtype = 'object'), array([3, 7, 3, 3, 6]))

print(data["B"], data.B)            # data.B는 index값이 숫자가 아닌경우에 쓸 수 있다.
(7, 7)
data["C"]=10                        # C 위치의 값을 수정할 수도 있다.
print(data*10)                      # 모든 값에다가 10을 곱해줄 수 도 있다.
print(data[["B", "E"]])             # 여러개 출력도 가능하고 offset index도 또한 이용이 가능
B 7
E 6
dtype 7 6

# index, value 설정
data2 = pd.Series({"D":3, "E":5, "F"7})
print(data2)
D   3
E   5
F   7
dtpte: int64

result=data+data2                   # 연산할 때 같은 index 값끼리 연산이 된다.
print(result)
A   NaN                             # data에는 값이 있지만 data2에는 값이 없기 때문에 연산 불가 
B   NaN
C   NaN
D   6.0                             # data 와 data2 값이 들어있기 때문에 연산
E   11.0
F   NaN
dtype: float64
</code></pre>

## Data Frame
* Data Frame은 여러개의 Series로 구성
* 같은 컬럼에 있는 value값은 같은 데이터 타입을 가진다.
- 데이터 프레임 생성 1 : 딕셔너리의 리스트
<pre><code>
datas = {
    "name":["dss", "fcamp"],
    "email":["dss@gamil.com", "fcamp@daum.net"],
}
print(df = ppd.DataFrame(datas))                    # 딕셔너리의 리스트는 column으로 데이터가 들어간다
    name        email
0   dss         dss@gamil.com
1   fcamp       fcamp@daum.net
</code></pre>

- 데이터 프레임 생성 2 : 리스트의 딕셔너리
<pre><code>
datas = [
    {'name':'dss', 'email':'dss@gamil.com'},
    {'name':'fcamp"' 'eamil': 'fcamp@daum.net'}
]
df=pd.DataFrame(datas)
    email           name                            # 리스트의 딕셔너리는 row로 데이터가 들어간다
0   dss@gamil.com   dss
1   fcamp@daum.net  fcamp       
</code></pre>

- 인덱스를 추가하는 방법
<pre><code>
df = pd.DataFrame(datas, index=["one", "two"])      # index 값을 one, two로 설정
print(df)
      name        email
one   dss         dss@gamil.com
two   fcamp       fcamp@daum.net

df.index                                            # index 값 호출
df.columns                                          # column 값 호출
df.values                                           # value 값 호출
</code></pre>

- 데이터 프레임에서 데이터의 선택 : row, column, (row,column)
<pre><code>
# row 선택 : loc
print(df.loc[1])
name                 fcamp
email       fcamp@daum.net
print(df.loc[1]["email"])
'fcamp@daum.net'

df.loc[2]={"name":"andy", "email":"andy@naver.com"}         # index가 있으면 수정, 없으면 추가

# column 선택
df["name"]                                                  # name column 선택
df["id"] = range(1,4)   # np.array(1,4)                     # column 에 id 와 값 추가

# row, column 선택
df.loc[row, column]
print(df.loc[[0, 2], ["email", "id"]])
            email       id
0   dss@gamil.com        1
2  andy@naver.com        3

# 컬럼 데이터 순서 설정
df[["id", "name", "email"]]                         # list 타입으로 쓴 순서대로 출력

# head, tail
df.head(2)                                          # 위에서부터 2개를 출력
df.tail(2)                                          # 밑에서부터 2개를 출력
</code></pre>
