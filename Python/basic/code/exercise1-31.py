v1=[1,2,3]

# method.1
norm=(v1[0]**2+v1[1]**2+v1[2]**2)**0.5
print(norm)

# method.2
norm=0
norm+=v1[0]**2
norm+=v1[1]**2
norm+=v1[2]**2
norm**=0.5
print(norm)