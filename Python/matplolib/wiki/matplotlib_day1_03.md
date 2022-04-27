# Matplotlib

## Lecture 1-03 : Titles, Labels and Font Dict

## 1. fig.suptitle & ax.set_title
위의 명령어들은 figure와 ax에 title을 달아주는 간단한 명령어이다. Argument들을 이용하여서 title의 이름, 사이즈, 글씨체, 색상, 투명도 등을 설정할 수 있다.    
```py
import matplotlib.pyplot as plt

figsize = (7, 7)
fig, ax = plt.subplots(figsize=figsize)
fig.subtitle("Title of a Figure", fontsize = 30, fontfamily = 'monospace')
ax.set_title("Title of a Ax", fontsize = 30, fontfamily = 'monospace')

# Title의 이름, 사이즈, 글씨체, 색상 등을 설정할 수 있다.
# 또한 for문을 이용하여서 여러개의 ax에 이름을 붙일 수 있다.

import matplotlib.pyplot as plt

figsize = (7, 7)
ax_title_list = ['title ' + str(i) for i in range(4)]

fig. axes = plt.subplots(2, 2, figsize = figsize)
fig .suptitle("Title of a Figure", fontsize = 30, fontfamily = 'monospace')

for ax_idx , ax in enumerate(axes.flat):            # 4개의 ax에 이름을 붙이는 반복문
    ax.set_title(ax_title_list[ax_idx], fontsize = 20, fontfamily = 'serif')

fig.subplots_adjust(bottom=0.05, top=0.8, hspace=0.3)   # fig와 ax들의 title이 겹치는 것을 방지하기 위함.
```
주의해야할 점으로 figure와 axes들의 title을 설정했을 때 figure와 axes들의 title이 겹치는 문제가 발생한다.   
이를 해결하기 위해서 fig.tight_layout() 명령어를 썼음에도 불구하고 **fig.subtitle은 fig.tight_layout()의 명령어에 영향을 받지 않는다.**   
따라서 이를 해결하기 위해서는 **fig.subplots_adjust** 를 이용하여 간격을 조절해 주어야 한다.

## 2. ax.set_xlabl & ax.set_ylabel
위의 명령어들은 ax안의 x축과 y축에 label을 달아주는 간단한 명령어이다. Argument들을 이용하여서 label의 이름, 사이즈, 글씨체, 색상, 투명도 등을 설정할 수 있다.
```py
import matplotlib.pyplot as plt

figsize = (7, 7)
fig, ax = plt.subplots(figsize = figsize)
ax.set_xlabel("X label", fontsize = 20, color = 'darkblue', alpha = 0.7)    # alpha는 투명도의 argument
ax.set_ylabel("Y label", fontsize = 20, color = 'darkblue', alpha = 0.7)    # alpha값이 높을 수록 선명하다.
```

## 3. Text Alignment
우선 이 내용을 다루기 전에 **ax.text** 라는 명령어를 먼저 다뤄보기로 한다.   
**ax.text()** 명령어는 ax안에 원하는 위치에 text를 집어넣는 명령어이다.
```py
import matplotlib.pyplot as plt

figsize = (7, 7)
fig, ax = plt.subplots(figsize = figsize)

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.grid()
ax.tick_params(axis='both', labelsize=15)

ax.text(x=0, y=0, s="Hello", fontsize=30)           # x, y가 (0, 0)인 위치에 Hello라는 글자를 삽입
                                                    # 글자의 left, bottom을 기준으로 글자가 삽입
ax.text(x=0.5, y=0, s="Hello2", fontsize=30)        # x, y가 (0.5, 0)인 위치에 Hello2라는 글자를 삽입
ax.text(x=0.5, y=-0.5, s="Hello3", fontsize=30)     # x, y가 (0.5, -0.5)인 위치에 Hello3라는 글자를 삽입
```
![1](https://github.com/Hojeong827/TIL/blob/main/Python/matplolib/image/1.png)

이 **ax.text()** 명령어를 이용하여 text alignment, 즉 text의 위치를 조정을 할 수가 있다.   
바로 text명령어 안의 argument인 horizontal alignment와 vertical alignment를 사용하는 것이다.   
각각 horizontal alignment는 left, center, right, 그리고 vertical alignment는 top, center, bottom의 위치로 설정할 수 있다.   
또한 horizontal alignment는 줄여서 'ha', 그리고 vertical alignment는 줄여서 'va'로 쓸 수 가 있다.
```py
# 위의 예제를 이어서 설명
ax.text(x=0, y=0, va='center', ha='left', s="Hello", fontsize=30)
# x와 y는 현재 -1에서 1까지 범위가 설정되어있다.
# text의 위치는 x, y의 좌표가(0, 0)인 위치에 설정
# 글자가 나타나는 기준점은 글자의 왼쪽 아래인 점이 기준으로 (0, 0)인 지점과 기준점이 일치한다.
# 여기서 va='center'이고 ha='left' 라고 명령되면 글자가 (0, 0)에서 나타나지만
# 글자의 세로축에서 중앙, 가로축에서 왼쪽으로 설정되었기 때문에 나타나는 위치가 바뀌게 된다.
```
![2](https://github.com/Hojeong827/TIL/blob/main/Python/matplolib/image/2.png)

## 4. Title Alignment
3번 항목에서 다룬 것과 같이 fig 와 ax의 title에서도 ha와 va를 이용하여서 위치를 조정할 수 있다. 이를 예제를 이용하여서 다루어 보겠다.
```py
import matplotlib.pyplot as plt

figsize = (7, 7)
fig, ax = plt.subplots(figsize = ifgsize)

title_bottom = 0.9
fig.suptitle("Title", fontsize = 30, y = title_bottom, va = 'bottom')   
# title_bottom=0.9인 위치에 Title이라는 글자의 아래를 기준으로 글자가 생성

ax.set_title("Ax Title", fontsize=20)

fig.subplots_adjust(top=title_bottom)
# fig title이 생성된위치 바로 아래에 그래프가 그려지도록 명령

fig.subplots_adjust(top=title_bottom-0.1)
# ax title이 fig title과 겹치지 않게 조정
-------------------------------------------------------------------------------------------------------------------
# 이와 별개로 fig.subtitle과 ax.set_title 명령어를 쓸 때 x와 y의 위치가 음수가 될 수 있다.

ax.set_title("Ax Title", fontsize = 20, y=-0.1)
# 그래프의 아래에 title이 생성이 되게 된다.
```
## 5. Text Properties

## 6. Font Dictionary

## 7. Title Exercise