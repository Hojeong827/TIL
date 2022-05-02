import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xscale('log')
ax.set_yscale('log')

ax.tick_params(labelsize=20)

major_xticks = [10**i for i in range(5)]
major_yticks = [1E-10, 1E-5, 1E0]
minor_yticks = [10**i for i in range(-10, 4)]

ax.set_xticks(major_xticks)
ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)

ax.tick_params(which = 'major', direction='in', length=8, labelsize=20)
ax.tick_params(which = 'minor', direction='in', length=5, labelsize=0)

ax.grid(which='major', color='silver')
ax.grid(which='minor', linestyle=':', color='silver')
plt.show()