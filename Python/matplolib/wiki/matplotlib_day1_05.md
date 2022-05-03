# Matplotlib

## Lecture 1-05 : Grid

## 1. ax.grid
Grid(격자)를 그리기 위한 명령어로서 x, y축 모두 격자를 그릴지, x 축에만 격자를 그릴지, y축에만 격자를 그릴지 또는 격자의 두께, 색깔, line style을 설정할 수 있다.
```py
import matplotlib.pyplot as plt

fig, ax = plt.subplolts(figsize=(7, 7))
ax.grid()                       # x, y축에 격자를 모두 그림
ax.grid(axis='x')               # x 축만 그림
ax.grid(axis='y')               # y 축만 그림

ax.grid(linewidth=2, linestyle=':', color='r')  # 격자 두께, 색깔 및 line style 조절
```

## 2. Ticks and Grid
Tick과 Grid의 활용법을 알아보자.
```py
import matplotlib.pylot as plt

fig, ax = plt.subplots(figsize=(7, 7))

major_xticks = [i for i in range(0, 101, 20)]
minor_xticks = [i for in range(0, 101, 5)]

ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor=True)

ax.tick_params(labelsize=20)
ax.grid(axis='x', which='major', linewidth=1.5)             # major 축에 grid 생성
ax.grid(axis='x', which='minor', linestyle=':')             # minor 축에 grid 생성
```
## 3. Grid Exercise