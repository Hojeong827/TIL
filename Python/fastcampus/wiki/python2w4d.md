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

## Apply 함수
* map 함수와 비슷한 역할을 하는 함수
<pre><code>
# email 컬럼에서 메일의 도메인만 가져와서 새로운 domain 컬럼을 생성

def domain(email):
    return email.split("@")[1].split(".")[0]

print(doamin(df.loc[0]["email"]))
'gamil'

print(df["email"].apply(domain))                # df["email"]에 domain 함수를 적용
0   gamil
1   daum
2   naver

df["domain"]=df["email"].apply(domain)          # df 에 도메인 column 이 추가가 되고 domain 값이 추가

df["domain"] = df["email"].apply(lambda email: email.split("@")[1].split(".")[0])
=> 함수 선언 없이 lambda를 이용하는 것도 가능
</code></pre>

## Append 함수
* 데이터 프레임을 합치는 함수(세로로만 가능)
* [reset_index](https://kongdols-room.tistory.com/123)
<pre><code>
df = pd.DataFrame([1, 2, 3])
0   1
1   2
2   3
df2 = pd.DataFrame([4, 5 6])
0   1
1   2
2   2

df3=df1.append(df2)             # 세로로 합쳐졌지만 인덱스도 그래도 합쳐진다
0   1
1   2
2   3
0   4
1   5
2   6

# 인덱스 재정렬 : reset_index
df3.reset_index(drop=True, inplace=True)        # drop은 인덱스로 세팅한 열을 DataFrame 내에서 삭제할지 여부를 묻는다
                                                # inplace는 원본객체를 변경할지 여부를 묻는다
</code></pre>

## Concat 함수
* row 나 column으로 데이터 프레임을 합칠 때 사용
<pre><code>
df = pd.DataFrame([1, 2, 3])
df2 = pd.DataFrame([4, 5 6])

df3 = pd.concat([df, df2]).reset_index(drop=True)
0   1
1   2
2   3
3   4
4   5
5   6

pd.concat([df3, df1], axis=1)                 # 가로로 합치기
0   1   1
1   2   2
2   3   3
3   4   NaN                                   # df1에는 값이 없기 때문
4   5   NaN
5   6   NaN                     

pd.concat([df3, df1], axis=1, join"inner")    # inner는 교집합 outer는 위와 같음
0   1   1
1   2   2
2   3   3
</code></pre>

## Group by 함수
* 특정 컬럼의 중복되는 데이터를 합쳐서 새로운 데이터 프레임을 만드는 방법
* [Groupby에 대한 자세한 설명](https://yganalyst.github.io/data_handling/Pd_13/)
<pre><coce>
datas = {
    "number1":[1, 2, 3, 4, 5, 6],
    "number2":[1, 2, 3, 1, 3, 1],
}
df=pd.DataFrame(datas)
   number1     number2
0      1           1
1      2           2
2      3           2
3      4           1
4      5           3
5      6           1

1. size()
df.groupby("number2").size()           # 중복된 개수 출력
number2
   1      3
   2      1
   3      2

result = df.groupby("number2").size().reset_index(name="count")      
=>중복된 개수를 출력하는 column의 이름 지정
    number2     count
0       1         3
1       2         1
2       3         2

# sort_values : 설정한 컬럼으로 데이터 프레임을 정렬
result_df.sort_values(["count"], ascending=False)       # ascending : 오름차순 or 내림차순
    number2     count
0       1         3
2       3         2
1       2         1                                     # 또한 inplace도 적용가능하다

2. agg() : 여러개의 열에 여러가지 함수를 적용 가능
df.groupby("number2").agg("min").reset_index()          # 최소값
df.groupby("number2").agg("max").reset_index()          # 최대값
df.groupby("number2").agg("mean").reset_index()         # 평균
</code></pre>

## Merge 함수 = sql(join)
* 두개 이상의 데이터 프레임을 합쳐서 결과를 출력하는 방법
[merge에대한 추가적인 설명](https://yganalyst.github.io/data_handling/Pd_12)
<pre><code>
datas1 = {
    "num":[1, 2, 3],
    "city":["seoul", "busan", "daejeon"],
}
df1=pd.DataFrame(datas1)

datas2 = {
    "num":[1, 2, 3],
    "population":[3000, 2000, 1500],
}
df2=pd.DataFrame(datas2)

result = pd.merge(df1, df2)
    num      city     population
0    1      seoul       3000
1    2      busan       2000
2    3      daejeon     1500

</code></pre>