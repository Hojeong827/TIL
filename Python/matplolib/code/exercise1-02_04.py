import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (20, 10))

n_row, n_col = 3, 4
axes = np.empty(shape = (0, n_col))

xlabel_list = ['Iteration 01', 'Iteration 11', 'Iteration 21', 'Iteration 31']
ylabel_list = ['Log-Likehood', 'Negative Grad.', 'Probability']

for r_idx in range(n_row):
    axes_row = np.empty(shape=(0, ))
    if r_idx == 0:
        for c_idx in range(n_col):
            if c_idx == 0:
                ax = fig.add_subplot(n_row, n_col, n_col * r_idx + c_idx + 1)
            else:
                ax = fig.add_subplot(n_row, n_col, n_col * r_idx + c_idx +1, sharey=axes_row[0])
            axes_row = np.append(axes_row, ax)
    else:
        for c_idx in range(n_col):
            if c_idx == 0:
                ax = fig.add_subplot(n_row, n_col, n_col * r_idx + c_idx + 1, sharex=axes[0, c_idx])
            else:
                ax = fig.add_subplot(n_row, n_col, n_col * r_idx + c_idx +1, sharey=axes_row[0], sharex=axes[0, c_idx])
            axes_row = np.append(axes_row, ax)
    axes = np.vstack((axes, axes_row))


axes[0, 0].set_ylim([1.5, 2.0])
axes[1, 0].set_ylim([-0.7, 0.7])
axes[2, 0].set_ylim([0, 0.14])
axes[0, 0].set_xlim([0, 100])
axes[0, 1].set_xlim([0, 200])
axes[0, 2].set_xlim([0, 300])

# set xy labels
for ax_idx, ax in enumerate(axes.flat):
    if ax_idx % n_col == 0:
        ax.set_ylabel(ylabel_list[ax_idx // n_col], fontsize=20)
    if ax_idx >= 2*n_col:
        ax.set_xlabel(xlabel_list[ax_idx - 2*n_col], fontsize=20)
    if ax_idx % n_col != 0:
        ax.get_yaxis().set_visible(False)
    if ax_idx <=n_col * 2 -1:
        ax.get_xaxis().set_visible(False)

axes[2, 1].plot([], color='b', marker='|', label='regression')
axes[2, 1].plot([], color='r', marker='o', label='cross entropy')
axes[2, 1].plot([], color='g', marker='v', label='target')
axes[2, 1].legend(loc='upper center', bbox_to_anchor=(1, -0.25), fontsize=20, ncol=3)
fig.tight_layout()
fig.subplots_adjust(hspace=0.2, wspace=0.01)
plt.show()