mat1 = [[1,2,3], [4,5,6], [7,8,9]]
mat2 = [[11,12,13], [14,15,16],[17,18,19]]

n_row=len(mat1)
n_col=len(mat1[0])

mat_add=list()
for row_idx in range(n_row):
    row_add=list()
    for col_idx in range(n_col):
        element1 = mat1[row_idx][col_idx]
        element2 = mat2[row_idx][col_idx]
        row_add.append(element1+element2)
    mat_add.append(row_add)
print("Addition of mat1 and mat2: \n", mat_add)