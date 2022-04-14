# Matplotlib

## Lecture 1-01

## 1. Figures & Axes
- Figure : 그래프를 그리기 위한 창을 의미한다. Figure안에서 여러개의 Axes를 그릴 수 있다.   
- Axes : Axes 는 figure 내에서 축을 가지는 하나의 좌표평면과 같은 개념. 실제로 데이터가 그려지는 곳은 Axes 이다.   
    - 하나의 그래프를 **ax** 라고 부르며 **ax**가 여러개 모인 것을 **axes** 라고 한다.   

## 2. plt.figure(Making Figures)
Figure를 만들기 위해서는 우선 **matplotlib.pyplot** 라이브러리를 불러와야한다.   
```py
import matplotlib.pyplot as plt
import numpy as np
```
라이브러리를 불러옴으로서 그래프를 그릴 수 있는 명령어를 쓸 수 있게 됐다.   
figure를 그리는 가장 첫 명령어로는 **plt.figure()** 가 있는데 이를 임의의 변수 fig에 return해 줄 것이다.   
```py
fig = plt.figure()  # an empty figure with no Axes
```
그러면 fig라는 object 의 이름으로 plt.figure()의 리턴값을 받게 되는데 **instance**라고 부를 수 있게 된다.    
즉 fig를 이용해서 matplotlib에서 제공하는 다양한 method들을 이용할 수 있게 되는 것이다.   
또한 **plt.figure()** 에서 주로 쓰이는 함수로서 figure의 크기와 색깔을 정하는 함수를 이용해 원하는 설정으로 figure를 만들 수 있다.
```py
fig = plt.figure(figsize=(7, 7))                        # figure 의 크기를 정하는 함수
fig = plt.figure(figsize=(7, 7), facecolor='linen')     # figure 의 색깔을 정하는 함수 ('linen'은 색깔의 한 종류)
```

## 3. fig.add_subplot(Adding Subplots)
이제 Figure를 그렸으면 Figure안에 들어갈 그림(ax)를 그릴 차례이다.
```py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 7), facecolor='linen')           # 빈 figure생성
ax = fig.add_subplot()                                        # figure 안에서 ax라는 object를 할당 받음
ax = fig.add_subplot(111)                                     # ax = fig.add_subplot(1, 1, 1) 과 같은 표현
ax = fig.add_subplot(111, facecolor = 'r')                    # facecolor 를 이용하여 ax의 색깔을 정할 수 있다.
```
**fig.add_subplot()** 을 하게 되면 figure안에 그림이 생기게 되는데 우리는 이제 이 그림을 이용하여 그래프를 그릴 것이다.   
figure 안에서 ax라는 object를 할당 받아 lineplot, scatterplot, histogram 등등의 여러 그래프를 그릴 수 있다.   
```py
ax = fig.add_subplot(111)                                     # ax = fig.add_subplot(1, 1, 1) 과 같은 표현
```
subplot안의 숫자가 의미하는 바는 row의 개수, column의 개수, 그리고 마지막은 ax가 몇번째 ax인지를 나타낸다.   
또한 ax의 위치는 왼쪽에서부터 오른쪽, 그리고 위에서 아래로 내려가는 방향으로 샌다. 
```py
ax1 = fig.add_subplot(221)                  # (1,1)의 위치
ax2 = fig.add_subplot(222)                  # (1,2)의 위치
ax3 = fig.add_subplot(223)                  # (2,1)의 위치
ax3 = fig.add_subplot(224)                  # (2,2)의 위치
```
만일 2개의 작은 그래프와 하나의 큰 그래프를 그리고 싶을 때 쓰는 방법이 있다.
```py
ax1 = fig.add_subplot(221)                  # 2 x 2 에서 1번째 위치에 그래프를 그림
ax2 = fig.add_subplot(222)                  # 2 x 2 에서 2번째 위치에 그래프를 그림
ax3 = fig.add_subplot(212)                  # 2 x 1 에서 2번째 위치에 그래프를 그림
```
이런식으로 코드를 작성하게 되면 ax1 과 ax2는 앞의 예시와 같이 (1,1)과 (1,2)의 위치에 그림이 들어가게 된다.   
하지만 ax3 의 경우에는 2 x 1의 공간으로 할당되어 (2,1)과 (2,2)의 공간을 합하여 그래프가 나타내지게 된다.

## 4. plt.subplots(Making Fig and Axes Simultaneously)
앞에서 배운것에 따르면 figure와 ax를 따로따로 선언하여서 그래프를 그리는 방식을 배웠다. 이를 한꺼번에 선언할 수 있는 함수가 바로 **subplots** 이다.
```py
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(nrows = 2, ncols = 1)          # figure와 2 x 1 의 axes 를 만드는 함수
fig, axes = plt.subplots(2, 1)                          # 위와 같은 표현이다.(생략 가능)
fig, (ax1, ax2) = plt.subplots(2,1)                     # 언패킹을 통해 이러한 표현으로 ax1과 ax2로 미리 할당이 가능하다
```
subplots 를 이용하면 한번에 figure 와 2행(nrows = 2), 1열(ncols = 1)의 axes를 만들 수 있다. 이렇게 만들어진 axes에 그래프를 출력하는 방법은 다음과 같다.
```py
axes[0].plot([2, 5, 10])                                # axes의 1번째 위치에 2, 5, 10을 출력
axes[1].plot([3, 9, 4])                                 # axes의 2번째 위치에 3, 9, 4를 출력
```
이는 python에서 array를 다루는 방식과 유사하다.   
또한 plt.subplots를 이용해서 2D figure와 axes를 출력할 수 있는데 
```py
fig, axes = plt.subplots(2, 2, figsize=(7, 7), facecolor='linen')       # figure에 2 x 2 의 axes를 만듬
print(axes[0])                                                          # figure의 첫번째 줄의 axes를 모두 출력
print(axes[0, 1])                                                       # figure의 첫번째 줄의 2번째 axes를 출력
```
이러한 방식을 이용하면 for 문을 돌리기 힘들어지기 때문에 아래와 같은 방식을 이용하여서 2D figure를 만들어 본다.
```py
# case 1
test_np = np.array([[1, 2], [3,4]])            # axes가 numpy의 array의 형식과 같기 때문에 test_np를 axes라 가정

for val in test_np:
    print(val)                                 # 일반적으로는 [1, 2], [3, 4] 가 출력됨

for val in test_np.flat:                       # flat 을 쓰게 되면 각 row의 원소들을 차례로 접근하게 되어 1, 2, 3, 4로 출력
    print(val)                                 # 또한 각 row의 구분이 없어져 하나의 줄로 (1D array)로 바뀌게 된다.

-----------------------------------------------------------------------------------------------------------------------
# case 2
idx = 0
test_list = [10, 11, 12, 13]

for val in test_list:                           # index값이 필요하지만 idx += 1과 같은 코드가 필요
    print(idx, val)
    idx += 1

for idx, val in enumerate(test_list):           # enumerate를 이용하면 자동으로 idx값이 증가하게 된다.
    print(idx, val)

-----------------------------------------------------------------------------------------------------------------------
# case 3 (case1 과 case2의 응용)
fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize=(7, 7), facecolor='linen')

for ax_idx, ax in enumerate(axes.flat):
    print(ax_idx, ax)                           # index와 각각의 axes를 출력 또는 활용할 수 있게 된다.
```
plt.subplots를 이용하면 axes의 접근이 용이하지만 add_subplot에서 처럼 다양한 형태와 크기의 axes를 그리는 것은 힘들다.   

## 5. plt.subplot2grid(More Complex Arrangement)
위에서 배운것처럼 plt.subplot은 axes의 접근은 용이한 대신 다양한 형태와 크기의 axes를 그리는 데에는 한계가 있다는 것이 분명했다.   
이러한 단점을 극복하기 위해서 우리가 쓰게되는 것이 **plt.subplot2grid**이다.
```
matplotlib.pyplot.subplot2grid(shape, loc, rowspan=1, colspan=1, fig=None, **kwargs)   
=> Create a subplot at a specific location inside a regular grid
* Parameters   
1. shape(int, int) : Number of rows and of columns of the grid in which to place axis.   
2. loc(int, int) : Row number and column number of the axis location within the grid.   
3. rowspanint, default = 1 : Number of rows for the axis to span downwards.   
4. colspanint, default = 1 : Number of columns for the axis to span to the right.   
5. figFigure, optional : Figure to place the subplot in. Defaults to the current figure.   
6. **kwargs : Additional keyword arguments are handed to add_subplot.   
```
plt.subplot2grid의 parameter는 위와 같이 나타내지며 이를 활용하는 방법은 아래와 같다.
```py
# parameter들을 사용하지 않은 일반적인 예시
import matplolib.pyplot as plt
import numpy as np

fig = plt.figure(figsige = (7,7), facecolor='linen')

ax1 = plt.subplot2grid((2, 1), (0, 0), fig = fig)           # fig 안에 2 x 1 크기에 (0, 0)의 위치에 ax1을 할당
ax1 = plt.subplot2grid((2, 1), (1, 0), fig = fig)           # fig 안에 2 x 1 크기에 (1, 0)의 위치에 ax2를 할당
                                                            # 일반적으로 쓰이는 add_subplot이나 plt.subplot과 비슷하다.
------------------------------------------------------------------------------------------------------------------------
# parameter들을 사용했을 때의 예시, case1
import matplolib.pyplot as plt
import numpy as np

fig = plt.figure(figsige = (7,7), facecolor='linen')

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, fig = fig)    
# 3 x 3 의 공간에서 (0, 0)의 위치에서 시작하여 col방향으로 2개의 공간을 할당 : 즉 (0, 0) 과 (0, 1)이 합쳐진 공간
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=3, fig = fig)    
# 3 x 3 의 공간에서 (1, 0)의 위치에서 시작하여 col방향으로 3개의 공간을 할당 : 즉 (1, 0) ~ (1, 2)이 합쳐진 공간
------------------------------------------------------------------------------------------------------------------------
# parameter들을 사용했을 때의 예시, case1
import matplolib.pyplot as plt
import numpy as np

fig = plt.figure(figsige = (7,7), facecolor='linen')

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, fig = fig)    
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, fig = fig)
ax3 = plt.subplot2grid((3, 3), (2, 0), colspan=2, fig = fig)
ax4 = plt.subplot2grid((3, 3), (0, 2), rowspan=3, fig = fig)
# 3 x 3 의 공간에서 (0, 2)의 위치에서 시작하여 row방향으로 3개의 공간을 할당 : 즉 (0, 2) ~ (2, 2)이 합쳐진 공간
```

## 6. [Practice](https://github.com/Hojeong827/TIL/blob/main/Python/matplolib/code/exercise1-01.py)

## 7. fig.add_axes(Arbitrary Locations and Sizes of Axes)
이 함수는 각각의 axes의 위치및 크기를 지정하는 함수이다. 이 함수를 이용하면 ax안에 또다른 ax를 집어 넣거나 겹치게 하는 등 자유자재로 위치를 지정할 수 있다.
```
add_axes(rect, projection=None, polar=False, **kwargs)
Parameters
1. rect (sequence of float) 
: The dimensions [left, bottom, width, height] of the new Axes. All quantities are in fractions of figure width and height.

2. projection {None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str}, optional 
: The projection type of the Axes. str is the name of a custom projection, see projections. The default None results in a 'rectilinear' projection.

3. polar (bool, default: False) 
: If True, equivalent to projection='polar'.

4. axes_class (subclass type of Axes, optional) 
: The axes.Axes subclass that is instantiated. This parameter is incompatible with projection and polar. See axisartist for examples.

5. sharex, sharey (Axes, optional) 
: Share the x or y axis with sharex and/or sharey. The axis will have the same limits, ticks, and scale as the axis of the shared axes.

6. label (str) : A label for the returned Axes.
```
fig.add_axes의 parameter는 위와 같다. rect parameter의 left, bottom이 (0, 0)이면 기본적으로 왼쪽의 아래, 즉 figure의 왼쪽 아래의 모서리를 의미한다. (0.1, 0.1) 이면 왼쪽에서부터 0.1, 아래쪽에서부터 0.1을 의미한다. width와 height는 ax의 가로 세로 길이를 의미한다. 이를 활용하는 방법은 아래와 같다.
```py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 7), facecolor='linen')

ax1 = fig.add_axes([0.1, 0.1, 0.5, 0.5])
ax2 = fig.add_axes([0.7, 0.1, 0.2, 0.5])
ax3 = fig.add_axes([0.1, 0.7, 0.8, 0.2])

또는

rect1 = [0.1, 0.1, 0.5, 0.5]
rect2 = [0.7, 0.1, 0.2, 0.5]
rect3 = [0.1, 0.7, 0.8, 0.2]

ax1 = fig.add_axes(rect1)
ax2 = fig.add_axes(rect2)
ax3 = fig.add_axes(rect3)
```