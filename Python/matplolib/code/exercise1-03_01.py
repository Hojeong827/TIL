import matplotlib.pyplot as plt
import numpy as np

ax_title_list =['(a) CE - clean', '(b) CE - noisy', '(c) LSR - noisy', '(d) SL - noisy']
title_bottom = 0.9

figsize = (10, 10)
fig, axes = plt.subplots(2, 2, figsize = figsize)

fig.suptitle("Symmetric Cross Entropy", fontsize = 30, y = title_bottom + 0.03, va = 'bottom')

for ax_idx, ax in enumerate(axes.flat):
    ax.set_title(ax_title_list[ax_idx], fontsize = 20, y = -0.25)
    ax.set_xlabel("Number of Epochs", fontsize = 15)
    ax.set_ylabel("Class-wise Test Accuracy", fontsize = 15)

fig.subplots_adjust(top = title_bottom, bottom = 0.1, hspace = 0.3, wspace = 0.3)

plt.show()