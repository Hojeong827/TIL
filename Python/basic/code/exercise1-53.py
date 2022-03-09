v1=[1,2,3,4,5]
v2=[10,20,30,40,50]

# method.1
v3=list()
for dim_idx in range(len(v1)):
    v3.append(v1[dim_idx] * v2[dim_idx])
print(v3)

# method.2
v3=list()
for _ in range(len(v1)):
    v3.append(0)

for dim_idx in range(len(v1)):
    v3[dim_idx]=v1[dim_idx]*v2[dim_idx]
print(v3)