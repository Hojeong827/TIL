# Matplotlib

## Lecture 1-02

## 1.fig.tight_layout(Axes Layout Adjustment)
Figrue 안의 Axes의 title과 label을 설정했을 때 서로 겹치는 문제를 해결하기 위함과 figure와 axes간의 간격 조절이 필요할 때 쓰는 명령어이다.    
즉 figure내부의 모습을 보기 좋게 만들기 위함이다. 우선 axes의 title과 label을 설정하는 명령어에 대해서 먼저 알아보자.   
1. ax.set_title : ax의 title을 정하는 명령어   
2. ax.set_xlabel : ax의 x축의 label 을 정하는 명령어   
3. ax.set_ylabel : ax의 y축의 label 을 정하는 명령어   
```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7,7))

ax.set_title('Title!', fontsize=20)         # Title을 'Title!'로 설정
ax.set_xlabel('X Label!', fontsize=15)      # X축의 label을 'X Label!'로 설정
ax.set_ylabel('Y Label!', fontsize=15)      # Y축의 label을 'X Label!'로 설정
---------------------------------------------------------------------------------------------------------------------------
title_list = ['Ax' +str(i) for i in range(4)]            # for 문을 이용하면 여러개의 title과 label을 list에 넣을 수 있다.
xlabel_list = ['X label ' +str(i) for i in range(4)]
ylabel_list = ['Y label ' +str(i) for i in range(4)]

print(title_list)               # ['Ax0', 'Ax1', 'Ax2', 'Ax3']
print(xlabel_list)              # ['X label 0', 'X label 1', 'X label 2', 'X label 3']
print(ylabel_list)              # ['Y label 0', 'Y label 1', 'Y label 2', 'Y label 3']

fig. axes = plt.subplots(2, 2, figsize=(10,10))

for ax_idx, ax in enumerate(axes.flat):
    ax.set_title(title_list[ax_idx], fontsize=30)       # enumerate 와 flat을 이용하여 title 및 label을 정해줄 수 있다.
    ax.set_xlabel(xlabel_list[ax_idx], fontsize=20)
    ax.set_ylabel(ylabel_list[ax_idx], fontsize=20)
```
위와 같은 예제로 for문과 enumerate, flat을 이용하여서 title, x_label, y_label을 지정해 줄 수 있었다.   
하지만 여기서 발생하는 문제점이 바로 axes의 title과 label들이 서로 겹치게 되는 문제가 발생할 수 있다.   
이를 해결해 주는 명령어가 바로 **fig.tight_layout()** 이다. 사용법은 매우 간단하게 아래와 같은 코드를 코드의 위 코드의 맨 마지막에 넣어주기만 하면 된다.
```py
fig.tight_layout()
```
이 명령어를 쓰는데 주의할 점은 figure안의 ax들은 title과 label들이 함께 묶어져 있다고 생각해야한다.    
만일 figure와 axes들의 간격 또는 axes들 사이의 간격을 조절하고 싶은 때 argument인 **pad (default = 0.5)** 를 쓸 수 있는데,   
pad를 이용하여 간격을 조절하면 ax, title, label이 모두 묶여서 하나로 조절되기 때문이다.    
pad의 크기가 클수록 간격이 넓어지게 되는데 간격이 넓어질수록 ax, title, label의 크기도 작아지게 된다. 이를 유의하여야 한다.   

## 2.fig.subplots_adjust(More Customized Layout)
위와 같은 명령어를 쓰면 위의 fig.tight_layout에서 처럼 모든 간격이 일정한 것이 아닌 자신이 원하는 구간의 간격을 원하는 대로 조절할 수 있다는 장점이 있다.   
Usage와 parameters는 다음과 같다.   
* Usage : **fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)**   
* Parameters   
1. positional argument   
leftfloat, optional : The position of the left edge of the subplots, as a fraction of the figure width.   
rightfloat, optional : The position of the right edge of the subplots, as a fraction of the figure width.   
bottomfloat, optional : The position of the bottom edge of the subplots, as a fraction of the figure height.   
topfloat, optional : The position of the top edge of the subplots, as a fraction of the figure height.   
2. spacing argument   
wspacefloat, optional : The width of the padding between subplots, as a fraction of the average Axes width.   
hspacefloat, optional : The height of the padding between subplots, as a fraction of the average Axes height.   
```py
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)           # x축의 눈금을 없앰
    ax.get_yaxis().set_visible(False)           # y축의 눈금을 없앰

# axes와 figure 사이의 위, 아래, 왼쪽, 오른쪽의 간격을 설정
fig.subplots_adjust(bottom=0.05, top=0.9, left=0.05, right=0.8)
# axex간 위아래 사이의 간격을 설정 (height)
fig.subplots_adjust(hspace=0.05)
# axex간 좌우 사이의 간격을 설정 (width))
fig.subplots_adjust(wspace=0.05)
```
## 3.fig.subplots_adjuust(Practice)
[exercise1-02_02](https://github.com/Hojeong827/TIL/blob/main/Python/matplolib/code/exercise1-02_02.py)

## 4.Axis Sharing
앞에서 배운 내용을 이용하면 내가 원하는 크기와 위치, 그리고 모양을 설정하여서 axes를 그리는 방법에 대하여 배워보았다.    
그러나 내가 원하는 모양으로 axes를 그려도 x축과 y축이 불필요하게 반복되어서 이를 간단하게 그리는 방법에 대해서 배워본다.   
* ax.set_xlim & ax.set_ylim   
이 명령어는 x축과 y축의 기준점을 잡는 간단한 명령어로서 **ax.set_xlim([-10, 10])** 이라고 명령하면 x축은 -10부터 10까지 나타나게 되고 y축도 마찬가지로 **ax.set_ylim([-10, 10])**이라고 명령하면 -10부터 10까지 나타내지게 된다. 여러 axes들중 하나를 선택해서 설정하고 싶다면 **axes[0,0].set_xlim([-10, 10])**으로 명령하면 된다.

기본적으로 Axis Sharing에는 4가지 방법이 있는데 하나부터 알아보자.
### Method 1. (Using subplots)
첫번째 방법으로는 subplots에 있는 argument중 sharex와 sharey를 이용하는 방법이 있다.
```py
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(7, 7))          # 기본적으로 subplots를 이요하면 2 x 2크기의 axes를 생성

fig, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)     # 4개의 axes 모두가 x축을 공유하게 된다.
fig, axes = plt.subplots(2, 2, figsize=(7, 7), sharey=True)     # 4개의 axes 모두가 y축을 공유하게 된다.
fig, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True, sharey=True)   # 4개의 axes 모두가 x,y축을 공유하게 된다.
```
이 방법의 장점이자 단점으로는 모든 axes들의 x축과 y축이 공유되기 때문에 한꺼번에 지정하기에는 편하지만 내가 원하는 부분만 공유하기에는, 즉 구체적으로 설정하기에는 적합하지 않다. 또한 맨 바같의 축(눈금)을 제외한 공유된 축(눈금)은 사라지게 된다.   
그러나 sharex와 sharey를 썼을 때 첫번째 ax의 x축과 y축의 범위를 설정해주기만 하면 모든 axes들의 x축과 y축의 범위가 같이 설정되는 것 또한 장점이다.

### Method 2. (Using fig.add_subplot)
두번째 방법으로는 fig.add_subplot에 있는 sharex와 share를 이용하는 방법이다.
```py
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 7))            # fig를 만들고
ax1 = fig.add_subplot(211)                  # ax1을 만든뒤
ax2 = fig.add_subplot(212, sharex=ax1)      # ax2를 만들어 ax1의 x축을 공유하게 한다. (틱레이블(눈금) 은 사라지지 않음)
ax2.set_xlim([0, 100])
```
이 방법은 method 1과 달리 자유도가 매우 높다는 것이 장점이다. 하지만 하나하나 다 설정해줘야하기 때문에 코드의 길이가 길어질 수 밖에 없고 틱 레이블(눈금)이 사라지지 않는다는 것이 단점이다.   
이를 반복문을 이용하여 나타내는 예제는 아래와 같다.
```py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,10))

n_row, n_col = 3, 3
axes = np.empty(shape=(0,3))
for r_idx in range(n_row):
    axes_row = np.empty(shape=(0,))
    if r_idx == 0:
        for c_idx in range(n_col):
            if c_idx == 0:
                ax = fig.add_subplot(n_row, n_col, r_idx*n_row + c_idx + 1)
            else:
                ax = fig.add_subplot(n_row, n_col, r_idx*n_row + c_idx +1, sharey=axes_row[0])
            axes_row = np.append(axes_row, ax)
        axes = np.vstack((axes, axes_row)).reshape(1, -1)
    else:
        for c_idx in range(n_col):
            if c_idx == 0:
                ax = fig.add_subplot(n_row, n_col, r_idx*n_row + c_idx + 1, sharex=axes[0, c_idx])
            else:
                ax = fig.add_subplot(n_row, n_col, r_idx*n_row + c_idx +1, sharey=axes_row[0], sharex=axes[0, c_idx]   )
            axes_row = np.append(axes_row, ax)
        axes = np.vstack((axes, axes_row)).reshape(1, -1)
fig.tight_layout()

axes[0, 0].set_ylim([0, 100])
axes[1, 0].set_ylim([0, 200])
axes[2, 0].set_ylim([0, 300])
axes[0, 0].set_xlim([0, 100])
axes[0, 1].set_xlim([0, 200])
axes[0, 2].set_xlim([0, 300])
```
### Method 3.
### Method 4.

## 5.Axis Sharing(Practice)

## 6.ax.twinx(Different Y Values)

## 7.ax.set_yscale(Axis Scale)