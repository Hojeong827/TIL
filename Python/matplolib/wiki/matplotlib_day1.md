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

## 4. plt.subplots(Making Fig and Axes Simultaneously)

## 5. plt.subplot2grid(More Complex Arrangement)

## 6. Practice

## 7. fig.add_axes(Arbitrary Locations and Sizes of Axes)