# Python 2주 2일차 정리

## Module, Package
* 모듈 : 변수, 함수, 클래스를 모아놓은 (.py) 확장자를 가진 파일
* 패키지 : 모듈의 기능을 디렉토리별로 정리해 놓은 개념

 1. 모듈(Module)
- 모듈 생성
<pre><code>
    %%writefile dss.py      # 이 아래의 코드들에 writefile적용, dss.py파일을 만들어 아래의 코드들을 dss.py파일에 저장 

    num = 1234

    def disp1(msg):
        print("disp1", msg)
    def disp2(msg):
        print("disp2", msg)
    
    class Calc:
        def plus(self, *args):
            return sum(args)

    -----------실행------------
    writing dss.py              # 실행하면 자동으로 출력 및 모듈 생성
</code></pre>

- 모듈 호출 : import dss => dss.py 안에있는 변수, 함수 및 클래스들을 사용 가능.
<pre><code>
    dss.num
    1234                        # dss.py 안의 num 변수를 사용

    dss.disp1("python")         # dss.py 안의 disp1 함수 사용
    dip1 python

    calc = dss.Calc()           # dss.py 안의 Calc class 사용
    calc.plus(1,2,3,4)
    10
</code></pre>
- 모듈 안에 특정 함수, 변수, 클래스 호출   
=> from dss import num, disp2 => 이렇게 호출하면 dss.num, dss.disp2()대신 num, disp()로 쓸 수 있다.
- 모듈의 모든 변수를 가져옴   
=> from dss import * => 이렇게 호출하면 dss.py의 모든 변수, 함수, 클래스를 가져올 수 있다.

2. 패키지(Package)
- 패키지 생성
<pre><code>
   !mkdir -p school/dss        # 디렉토리 생성 : school 디렉토리 생성 후 밑에 dss디렉토리 생성
   !mkdir -p school/web        # 디렉토리 생성 : school 밑에 dss 와 web이라는 디렉토리 생성
   !tree school                # school 밑에 어떤 디렉토리가 있는지 보여주는 명령어
    
   패키지 사용시 디릭토리에 __init.py 파일을 추가, python3.3 이상에서는 필요 없다.   
   !touch school/dss/__init__.py              # touch : 파일을 만드는 명령어
   !touch school/web/__init__.py

   %%writefile school/dss/data1.py            # dss 에 data1라는 module 추가
   
   def plus(*args):
       print("data1")
       return sum(args)
   실행 => Writing school/dss/data1.py
    
   %%writefile school/dss/data2.py             # dss 에 data2라는 module 추가

   def plus2(*args):
       print("data2")
       return sum(args)
   실행 => Wrting school/dss/data2.py

   %%writefile school/web/url.py               # web 에 url이라는 module 추가

   def make(url):
       return url if url[:7] == "http://" else "http://" + url
   실행 => Writing school/web/url.py
</code></pre>

- 패키지 호출
<pre><code>
   import school.dss.data1             # data1 모듈 호출

   ----------실행--------------
   school.dss.data1.plus(1,2,3)
   data1
   6
    
   import school.dss.data1 as dss      # 짧게 쓰는 법 : as, import A as B, A를 B처럼 쓰겠다.

   ----------실행--------------
   dss.plus(1,2)
   data1
   3
</code></pre>
- from school.web import ur : from 뒤에는 디렉토리나 모듈이 올 수 있지만 import 뒤에는 모듈부터 가능하다.
- setup.py 설치 파일 만들기 : setuptools 사용
<pre><code>
   %%writefile school/dss/__init.py    
    __all__ = ["data1", "data2"]

    %%writefile school/setup.py

    from setuptools import setup, find_packages

    setup(
        name="dss",
        packages=find_packages(),
        include_package_data=True,
        version="0,0,1",
        author="DoojinPark",
        author_email="pdj1223@gmail.com",
        zip_safe=False,
    )

    ------------실행---------------
    Writing school/setup.py
    !rm dss.py                          # 중복을 피하기 위해서 삭제(임시)

    !pip list | grep dss                # dss가 들어간 패키지 설치 되어 있는지 검색
</code></pre>

- 패키지 설치(터미널에서 실행) : school $ python setup.py develop   
- 패키지 제거(터미널에서 실행) : pip unistall dss   

## 예외 처리
* 코드를 실행중에 에러가 발생한 경우 에러를 처리하는 방법
* try, except, finally, raise
<pre><code>
# tyr, except : error 가 발생해도 코드를 중단하지 않고 계속적으로 실행하고 싶을 때 사용
ls = [1, 2, 3]
print(ls[3])                            # error 발생                
print("Done!")                          # Done 이 출력되지 않고 종료됨

---------------------------------------
try:                                    # try 부분에서 error 가 발생했을 때 except 코드가 실행됨
    print(ls[3])
except Exception as e:
    print("error")
    print(e)                            # error 에대한 설명을 출력, 그 후 Done 출력
print("Done")

# finally : try, except 구문이 실행된 후 finally 구문이 실행
try:
    1/0                                 # 에러 발생
except:                                 # except 구문 실행
    print("error")
finally:                                # except 가 실행된 후 finally 실행 (try가 참이고 except 가 실행되지 않아도 실행됨)
    print("Done")

# raise : 강제로 error 를 발생시키는 명령
try:
    1/0                                 # 에러 발생
except Exception as e:
    print("error")
    raise(e)                            # 강제적으로 error 발생, 그 후 Done 출력하지 않음

print("Done")
</code></pre>

## Numpy
* 행렬 데이터 생성, 수정, 계산등을 빠르게 처리해 주는 패키지
* 특징
    1. C, C++, 포트란으로 작성됨
    2. 선형대수학을 빠르게 연산 : 스칼라, 벡터, 메트릭스
    3. 사용하기 위해서 : import numpy as np

* 행렬 데이터 생성
* ndarray : 한가지 데이터 타입만 값으로 사용이 가능!
<pre><code>
array = np.array([1,2,3])
print(type(array), array)                  # (numpy.ndarray, array([1, 2, 3]) => 1차원 행렬

array2 = np.array(
    [[1, 2, 3],
    [4, 5, 6]],]
)
print(array2, array2.ndim, array2.shape)            # (array([[1, 2, 3],[4, 5, 6]]), 2, (2, 3))

* 행렬의 모양(shape) 변경하기 : reshape
array2.reshape(3, 2)                    # array([1, 2], [3, 4], [5, 6])
array2.reshape(6)                       # array([1, 2, 3, 4, 5, 6])

* 행렬 데이터의 선택 : offset index : masking
array2[1]                               # array([4,5,6])
array2[1][2]                            # 6, 이는 array2[1, 2] 와도 같은 표현
array2[1][:2]                           # array([4, 5])
array2[2][::-1]                         # array([6, 5, 4])

* 행렬 데이터 수정
array2[1][2]=10                         # array([1, 2, 3], [4, 5, 10])
array2[0]=0                             # array([0, 0, 0], [4, 5, 10])  : 브로드 캐스팅
array2[0] = [7, 8, 9]                   # array([7, 8, 9], [4, 5, 10])

* 조건으로 선택
array2 > 7                              
idx = array2 > 7
print(idx)                              # array([False, True, True], [False, False, True])
print(array2[idx])                      # array([8, 9, 10]) : 조건에 참인 부분만 출력
araay2[idx] = 100                       # array([7, 100, 100], [4, 5, 100])

* 행렬 데이터의 생성 2
data = np.zeros((2,3))
print(data)                             # array([0., 0., 0.], [0., 0., 0.]) : data type 이 flaot
data2 = data.astype("int")              # float type을 int형으로 변경

* arrange
np.arrange(5)                           # array([0, 1, 2, 3, 4])
np.arrange(5,10)                        # array([5, 6, 7, 8, 9])
np.arrange(5, 10, 2)                    # array([5, 7, 9])
</code></pre>

