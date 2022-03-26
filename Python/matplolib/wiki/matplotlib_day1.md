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
figure를 그리는 가장 첫 명령어로는 ```plt.figure()```가 있는데 이를 임의의 변수 fig에 return해 줄 것이다.   
```py
fig = plt.figure()  # an empty figure with no Axes
```
그러면 fig라는 object 의 이름으로 plt.figure()의 리턴값을 받게 되는데 **instance**라고 부를 수 있게 된다.    
즉 fig를 이용해서 matplotlib에서 제공하는 다양한 method들을 이용할 수 있게 되는 것이다.   
또한 ```plt.figure()```에서 주로 쓰이는 함수로서 figure의 크기와 색깔을 정하는 함수를 이용해 원하는 설정으로 figure를 만들 수 있다.
```
fig = plt.figure(figsize=(7, 7))                        # figure 의 크기를 정하는 함수
fig = plt.figure(figsize=(7, 7), facecolor='linen')     # figure 의 색깔을 정하는 함수 ('linen'은 색깔의 한 종류)
```

## 3. fig.add_subplot(Adding Subplots)


## 4. plt.subplots(Making Fig and Axes Simultaneously)

## 5. plt.subplot2grid(More Complex Arrangement)

## 6. Practice

## 7. fig.add_axes(Arbitrary Locations and Sizes of Axes)