v1, v2 = [1,2,3], [3,4,5]

diff_square_sum = 0
for dim_idx in range(len(v1)):
    diff_square_sum+=(v1[dim_idx]-v2[dim_idx])**2
e_distance = diff_square_sum**0.5
print("Euclidean distance between v1 and v2: ", e_distance)