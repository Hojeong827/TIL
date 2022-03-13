mat = [[1,2,3], [4,5,6], [7,8,9]]
vec = [10, 20, 30]

n_row = len(mat)
n_col = len(mat[0])

mat_vec_mul = list()
for row_idx in range(n_row):
    mat_vec = mat[row_idx]
    dot_prod = 0
    for col_idx in range(n_col):
        dot_prod += mat_vec[col_idx]*vec[col_idx]
    mat_vec_mul.append(dot_prod)
print("multiplication of mat and vec:\n", mat_vec_mul)