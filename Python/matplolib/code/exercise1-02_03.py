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
    else:
        for c_idx in range(n_col):
            if c_idx == 0:
                ax = fig.add_subplot(n_row, n_col, r_idx*n_row + c_idx + 1, sharex=axes[0, c_idx])
            else:
                ax = fig.add_subplot(n_row, n_col, r_idx*n_row + c_idx +1, sharey=axes_row[0], sharex=axes[0, c_idx]   )
            axes_row = np.append(axes_row, ax)
    axes = np.vstack((axes, axes_row))
fig.tight_layout()

axes[0, 0].set_ylim([0, 100])
axes[1, 0].set_ylim([0, 200])
axes[2, 0].set_ylim([0, 300])
axes[0, 0].set_xlim([0, 100])
axes[0, 1].set_xlim([0, 200])
axes[0, 2].set_xlim([0, 300])

plt.show()