import matplotlib.pyplot as plt
import numpy as np

title_list = ['Blurry image', 'Ours', 'Mohan et al.']
fig = plt.figure(figsize=(24, 10))

axes = np.empty((0, 4))
n_g, n_col, n_row = 3, 4, 5

for g_idx in range(n_g):
    axes_row = np.empty((0, ))
    axes_row = np.append(axes_row, plt.subplot2grid((5, 12), (0, g_idx*n_col), colspan = 4, rowspan = 3, fig=fig))
    axes_row = np.append(axes_row, plt.subplot2grid((5, 12), (3, g_idx*n_col), colspan = 3, rowspan = 2, fig=fig))
    axes_row = np.append(axes_row, plt.subplot2grid((5, 12), (3, 3 + g_idx*n_col), fig=fig))
    axes_row = np.append(axes_row, plt.subplot2grid((5, 12), (4, 3 + g_idx*n_col), fig=fig))

    for ax in axes_row:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    axes = np.vstack((axes, axes_row))
    axes_row[0].set_title(title_list[g_idx], fontsize = 30, y = -0.83)

fig.subplots_adjust(bottom = 0.1, top = 0.95, left = 0.05, right = 0.95, hspace = 0.05, wspace = 0.05)
plt.show()