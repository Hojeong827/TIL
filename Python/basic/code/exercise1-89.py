vectors = [[1, 11, 21], [2, 12, 22], [3, 13, 23], [4, 14, 24]]
h_prod = list()
for dim_data in vectors:
    dim_prod = 1
    for dim_val in dim_data:
        dim_prod *= dim_val
    h_prod.append(dim_prod)
print(h_prod)
