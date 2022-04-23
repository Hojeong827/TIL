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

## 5.Axis Sharing(Practice)

## 6.ax.twinx(Different Y Values)

## 7.ax.set_yscale(Axis Scale)