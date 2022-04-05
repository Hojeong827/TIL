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
```
subplots 를 이용하면 한번에 figure 와 2행(nrows = 2), 1열(ncols = 1)의 axes를 만들 수 있다. 이렇게 만들어진 axes에 그래프를 출력하는 방법은 다음과 같다.
```py
axes[0].plot([2, 5, 10])                                # axes의 1번째 위치에 2, 5, 10을 출력
axes[1].plot([3, 9, 4])                                 # axes의 2번째 위치에 3, 9, 4를 출력
```
이는 python에서 array를 다루는 방식과 유사하다. 

## 5. plt.subplot2grid(More Complex Arrangement)

## 6. Practice

## 7. fig.add_axes(Arbitrary Locations and Sizes of Axes)