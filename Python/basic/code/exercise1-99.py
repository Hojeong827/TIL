mat1 = [[1,2,3], [4,5,6], [7,8,9]]
mat2 = [[11,12,13], [14,15,16],[17,18,19]]

n_row=len(mat1)
n_col=len(mat1[0])

mat_mat_mul=list()

for row_idx in range(n_row):
    vec1 = mat1[row_idx]
    dot_prods = list()
    for col_idx in range(n_col):
        vec2 = list()
        for inner_idx in range(n_col):
            vec2.append(mat2[inner_idx][col_idx])
        dot_prod = 0
        for inner_idx in range(n_col):
            dot_prod += vec1[inner_idx]*vec2[inner_idx]
        dot_prods.append(dot_prod)
    mat_mat_mul.append(dot_prods)

print("multiplication of mat1 and mat2:\n", mat_mat_mul)