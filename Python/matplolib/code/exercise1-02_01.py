import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10,10))
"""
xaxis = ax.get_xaxis()              # 이 코드를 아래와 같이 간략하게 정리 가능
yaxis = ax.get_yaxis()

xaxis.set_visilbe(False)
yaxis.set_visible(Flase)
"""
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()