mat = [[1,2,3], [4,5,6], [7,8,9]]
n_row = len(mat)
n_col = len(mat[0])

mat_t = list()
for col_idx in range(n_col):
    column = list()
    for row_idx in range(n_row):
        column.append(mat[row_idx][col_idx])
    mat_t.append(column)
print("transpose of mat:\n", mat_t)