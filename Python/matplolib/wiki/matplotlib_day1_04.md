# Matplotlib

## Lecture 1-04 : Ticks and Ticklabels

## 1. ax.tick_params
ax안의 그래프들의 눈금(tick)에 대한 명령으로 x, y축에 있는 눈금들의 길이 두께를 조절할 수 있고, 그 눈금들의 label들의 크기도 또한 설정해줄 수 있다.
```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20)            # x, y축 눈금의 label의 크기를 조절 , axis argument설정을 하지 않아서 x, y축 모두 적용
ax.tick_params(axis='x', labelsize=20)  # x축만 적용
ax.tick_params(axis='y', labelsize=20)  # y축만 적용
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
x, y축의 눈금의 label의 범위와 개수를 설정하기 위해서 쓰는 명령으로 반복문을 이용하여 설정하는 것이 편하다.   
ax.set_xlim과는 다른점은 범위를 설정하는 것은 같지만 label의 개수를 원하는대로 설정할 수 있는 것이 다르다.
```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))

xticks = [i for i in range(10)]             # 0~9까지의 범위를 list에 넣음
ax.set_xticks(xticks)                       # 0~9까지의 범위를 label로 설정

ax.tick_params(labelsize=20)
```
또한 label이 달린 주 눈금을 설정을 했으면 lable이 달리지 않은 작은 눈금도 또한 설정할 수 있다.   
Argument인 major와 minor를 이용하는 것인데, major가 기본적으로 default값이고 이는 주 눈금을 설정하는 argument이면 minor는 작은 눈금을 그리기 위해서 쓰인다.
```py
import matplotlib.pylot as plt

fig, ax = plt.subplots(figsize=(14, 7))

major_xticks = [i for i in range(0, 101, 20)]      # 0~100까지 20의 단위로 주 눈금 범위 설정
minor_xticks = [i for i in range(0, 101, 5)]       # 0~100까지 5의 단위로 작은 눈금 범위 설정

ax.set_xticks(major_xticks)                        # major는 default값이=
ax.set_xticks(minor_xticks, minor = True)          # minor는 True를 이용해 설정, 작은 눈금 표현

ax.tick_params(axis='x', labelsize=20, lenght=10, width=3, rotation=30)
ax.tick_params(axis='x', which='minor', lenght=5, width=2)      # 작은 눈금 설정
```

## 3. ax.set_xticklabels
x, y축의 눈금의 label을 설정해주는 명령어로써 주의점으로는 위의 ax.set_xticks의 설정들을 마치고 난 뒤 설정해주는 것이 권장사항이다.
```py
import matplotlib.pyplot as plt

xticks = [i for in range(10)]
xtick_labels = ['Class ' + str(i) for i in xticks]

yticks = [i for in range(0, 101, 20)]
ytick_labels = [str(i)+'%' for i in yticks]

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels)
ax.tick_params(labelsize=20, rotation=60)

ax.set_yticks(yticks)
ax.set_yticklabels(ytick_labels)
ax.tick_params(axis='y', labelsize=20)

fig.subplots_adjust(bottom=0.2, left=0.15)
```

## 4. Ticks and Ticklabels Practice