import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_yscale('log')
ax.set_xscale('log')

ax.set_ylim([10**-10, 10**3])
ax.set_xlim([10**0, 10**4])

major_yticks = [10**i for i in [-10, -5, 0]]
minor_yticks = [10**i for i in range(-10, 4)]
major_xticks = [10**i for i in range(0, 5)]

ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)
ax.set_xticks(major_xticks)

ax.tick_params(which='major', direction='in', length=10, labelsize=15)
ax.tick_params(which='minor', direction='in', length=5, labelsize=0)

ax.grid(which='major', color='silver')
ax.grid(which='minor', linestyle=':', color='silver')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_title("Rosenbrock-U[0, 1]", fontsize=30)
ax.set_xlabel("Num. Iterations", fontsize=20)
ax.set_ylabel("Loss", fontsize=20)
plt.show()