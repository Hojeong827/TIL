import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_yscale('log')
ax.set_ylim([1, 1E3])

ax.tick_params(labelsize=20, length = 5)
ax.tick_params(which='minor', length = 5)

ax.grid(axis='y', which='major', linewidth=1.5)
ax.grid(axis='y', which='minor', linestyle=':')

plt.show()