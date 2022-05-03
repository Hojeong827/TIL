import matplotlib.pyplot as plt
import numpy as np

m_exp, M_exp = 0, 5
n_inter_yticks = 4

n_major_yticks = M_exp - m_exp + 1
n_minor_yticks = (n_major_yticks-1)*(n_inter_yticks+1)+1

major_yticks = np.logspace(m_exp, M_exp, n_major_yticks)
minor_yticks = np.logspace(m_exp, M_exp, n_minor_yticks)

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_yscale('log')
ax.set_ylim([10**m_exp, 10**M_exp])

ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)

ax.tick_params(axis='y', which='major', length=10)
ax.tick_params(axis='y', which='minor', length=3)

ax.grid(axis='y', which='major', linewidth=1.5)
ax.grid(axis='y', which='minor', linestyle=':')

plt.show()