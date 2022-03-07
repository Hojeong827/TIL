v1, v2 = [1,2,3], [3,4,5]

# method.1
dot_prod = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
print(dot_prod)

# method.2
dot_prod = 0
dot_prod += v1[0]*v2[0]
dot_prod += v1[1]*v2[1]
dot_prod += v1[2]*v2[2]
print(dot_prod)