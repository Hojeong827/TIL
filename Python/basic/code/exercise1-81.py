v1 = [1, 3, 5, 2, 1, 5, 2]
v2 = [2, 3, 1, 5, 2, 1, 3]

m_distance = 0
for dim_idx in range(len(v1)):
    sub = v1[dim_idx]-v2[dim_idx]
    if sub<0:
        m_distance += -sub
    else:
        m_distance += sub
print("Manhattan distance: ", m_distance)