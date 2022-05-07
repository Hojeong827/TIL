# Matplotlib

## Lecture 1-06 : Spines

## 1. Spines
Spine이란 ax안의 그래프를 보면 사각형 공간을 둘러싸는 4개의 축을 확인할 수 있는데 이를 Spine이라고 한다. 또는 데이터 영역의 경계를 나타내는 선으로도 정의된다.
```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (10, 10))
print(type(ax.spines))
```
## 2. spine.set_visible

## 3. spine.set_position(Basic Usage)

## 4. spine.set_position(Tuple Argument)