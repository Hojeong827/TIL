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