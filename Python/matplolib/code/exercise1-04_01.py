import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))

ax.tick_params(axis='y', labelsize=20, colors='gray')
ax.tick_params(axis='x', labelsize=20, rotation=40, colors='gray')
ax.set_ylabel("mAP: Unseen Scenes", fontsize=20, color='gray')
plt.show()