# Matplotlib

## Lecture 1-04 : Ticks and Ticklabels

## 1. ax.tick_params
ax안의 그래프들의 눈금(tick)에 대한 명령으로 x, y축에 있는 눈금들의 길이 두께를 조절할 수 있고, 그 눈금들의 label들의 크기도 또한 설정해줄 수 있다.
```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20)            # x, y축 눈금의 label의 크기를 조절 (,x, y축 따로 설정도 가능)
ax.tick_params(length=10)               # x, y축 눈금의 길이를 조절
ax.tick_params(width=3)                 # x, y축 눈금의 두께를 조절

ax.tick_params(labelsize=20, length=10, width=3, bottom = False, labelbottom = False)
# bottom : tick, labelbottom : tick label
# x 축의 눈금과 label 표시 안함

ax.tick_params(labelsize=20, length=10, width=3, left = False, labelleft = False)
# left : y축의 tick, labelleft : y축의 tick label
# y 축의 눈금과 label 표시 안함
# left, bottom 뿐만아니라 top, right도 존재

ax.tick_params(labelsize=20, length=10, width=3, rotation = 30)     # label의 기울기 조절
```
## 2. ax.set_xticks

## 3. ax.set_xticklabels

## 4. Ticks and Ticklabels Practice