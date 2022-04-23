import matplotlib.pyplot as plt
import numpy as np
'''
fig = plt.figure(figsize=(12, 13))
axes_g1 = np.empty(shape=(0,))
main = plt.subplot2grid((5, 4), (0, 0), 2, 2, fig=fig)

axes_g1 = np.append(axes_g1, main)

for r_idx in range(2, 2+3):
    for c_idx in range(2):
        ax = plt.subplot2grid((5, 4), (r_idx, c_idx), fig=fig)
        axes_g1 = np.append(axes_g1, ax)
        
axes_g1 = axes_g1.reshape(1, -1)
print(axes_g1.shape)

axes_g2 = np.empty(shape=(0,))
main = plt.subplot2grid((5, 4), (0, 2), 2, 2, fig=fig)
axes_g2 = np.append(axes_g2, main)
for r_idx in range(2, 2+3):
    for c_idx in range(2, 2+2):
        ax = plt.subplot2grid((5, 4), (r_idx, c_idx), fig=fig)
        axes_g2 = np.append(axes_g2, ax)

axes_g2 = axes_g2.reshape(1, -1)
print(axes_g2.shape)

axes = np.vstack((axes_g1, axes_g2))
print(axes.shape)
plt.show()
'''

fig = plt.figure(figsize=(12,13))

axes = np.empty(shape=(0, 7))
for g_idx in range(2):
    axes_g = np.empty(shape=(0, ))
    main = plt.subplot2grid((5, 4), (0, 2*g_idx), 2, 2, fig=fig)
    axes_g = np.append(axes_g, main)
    
    for r_idx in range(2, 2+3):
        for c_idx in range(2):
            ax = plt.subplot2grid((5,4), (r_idx, c_idx+2*g_idx), fig=fig)
            axes_g = np.append(axes_g, ax)
    
    axes_g = axes_g.reshape(1, -1)
    axes = np.vstack((axes, axes_g))
    
for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
fig.subplots_adjust(bottom=0.03, top=0.97, left=0.03, right=0.97, hspace=0, wspace=0)
plt.show()