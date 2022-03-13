vectors = [[1,11], [2,12], [3,13], [4,14]]
e_distance=0
for dim_data in vectors:
    diff = dim_data[0] - dim_data[1]
    diff_square = diff**2
    e_distance += diff_square

e_distance **= 0.5
print("Euclidean distance: ", e_distance)