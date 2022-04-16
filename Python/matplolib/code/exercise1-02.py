import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10,10))

"""
xaxis = ax.get_xaxis()
yaxis = ax.get_yaxis()

xaxis.set_visilbe(False)
yaxis.set_visible(Flase)
"""
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()