import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,7), facecolor='linen')
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)

ax1.plot([2, 5, 10])
ax2.plot([3, 9, 4])
ax3.plot([1, 3, 7])
plt.show()