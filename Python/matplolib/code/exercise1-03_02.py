import matplotlib.pyplot as plt
import numpy as np

title_list = ['Training Image', '2 scales', '4sclaes', '5scales', '6 scales', '8 scales']
title_font_dict = {'fontsize': 20, 'fontweight': 'bold'}

fig, axes = plt.subplots(2, 3, figsize = (20, 10))

for ax_idx, ax in enumerate(axes.flat):
    ax.set_title(title_list[ax_idx], fontdict = title_font_dict)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

fig.tight_layout()
plt.show()