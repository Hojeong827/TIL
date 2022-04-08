import matplotlib.pyplot as plt
import numpy as np

"""
fig = plt.figure(figsize=(7,7), facecolor='linen')
ax1 = fig.add_subplot(221, facecolor='r')
ax2 = fig.add_subplot(222, facecolor='g')
ax3 = fig.add_subplot(212, facecolor='b')

ax1.plot([2, 5, 10])
ax2.plot([3, 9, 4])
ax3.plot([1, 3, 7])
plt.show()
"""

"""
fig = plt.figure(figsize=(25, 20))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(222, projection='3d')
ax2 = fig.add_subplot(224, projection='3d')
plt.show()
"""

"""
fig = plt.figure(figsize=(20,20))
ax1 = plt.subplot2grid((5, 4), (0, 0), rowspan=2, colspan=2, fig=fig)
ax2 = plt.subplot2grid((5, 4), (0, 2), rowspan=2, colspan=2, fig=fig)

ax3 = plt.subplot2grid((5, 4), (2, 0))
ax4 = plt.subplot2grid((5, 4), (2, 1))
ax5 = plt.subplot2grid((5, 4), (2, 2))
ax6 = plt.subplot2grid((5, 4), (2, 3))

ax7 = plt.subplot2grid((5, 4), (3, 0))
ax8 = plt.subplot2grid((5, 4), (3, 1))
ax9 = plt.subplot2grid((5, 4), (3, 2))
ax10 = plt.subplot2grid((5, 4), (3, 3))

ax11 = plt.subplot2grid((5, 4), (4, 0))
ax12 = plt.subplot2grid((5, 4), (4, 1))
ax13 = plt.subplot2grid((5, 4), (4, 2))
ax14 = plt.subplot2grid((5, 4), (4, 3))
plt.show()
"""

"""
fig = plt.figure(figsize=(20,20))
axes = np.empty(shape=(0,))                         # axes 를 np.array로 만들어서 계속해서 추가하는 방식을 통해 반복되는 코드를 줄일 수 있다.
axes = np.append(axes, plt.subplot2grid((5, 4), (0, 0), rowspan=2, colspan=2, fig=fig))
axes = np.append(axes, plt.subplot2grid((5, 4), (0, 2), rowspan=2, colspan=2, fig=fig))

for r_idx in range(2, 5):
    for c_idx in range(4):
        axes = np.append(axes, plt.subplot2grid((5, 4), (r_idx, c_idx)))
plt.show()
"""

left, bottom = 0.1, 0.1
spacing = 0.005

width1, height1 = 0.65, 0.65
width2 = 1 - (2 * left + width1 + spacing)
height2 = 1 - (2 * bottom + height1 + spacing)

rect1 = [left, bottom, width1, height1]
rect2 = [left, bottom+height1+spacing, width1, height2]
rect3 = [left+width1+spacing, bottom, width2, height1]

fig = plt.figure(figsize=(7,7))
ax1 = fig.add_axes(rect1)
ax2 = fig.add_axes(rect2)
ax3 = fig.add_axes(rect3)
plt.show()