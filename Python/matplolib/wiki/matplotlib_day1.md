# Matplotlib

## Lecture 1-01

## 1. Figures & Axes
Figure : 그래프를 그리기 위한 창을 의미한다. Figure안에서 여러개의 Axes를 그릴 수 있다.
Axes : Axes 는 figure 내에서 축을 가지는 하나의 좌표평면과 같은 개념. 실제로 데이터가 그려지는 곳은 Axes 이다.   
    - 하나의 그래프를 **ax** 라고 부르며 **ax**가 여러개 모인 것을 **axes** 라고 한다.   

## 2. plt.figure(Making Figures)
Figure를 만들기 위해서는 우선 **matplotlib** 라이브러리를 불러와야한다.   
```py
import matplotlib.pyplot as plt
import numpy as np
```

```py
fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
```

## 3. fig.add_subplot(Adding Subplots)

## 4. plt.subplots(Making Fig and Axes Simultaneously)

## 5. plt.subplot2grid(More Complex Arrangement)

## 6. Practice

## 7. fig.add_axes(Arbitrary Locations and Sizes of Axes)