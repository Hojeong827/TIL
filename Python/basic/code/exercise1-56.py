v1, v2 = [1,2,3], [3,4,5]

dot_prod=0
for dim_idx in range(len(v1)):
    dot_prod+=v1[dim_idx]*v2[dim_idx]
print("dot product of v1 and v2: ", dot_prod)