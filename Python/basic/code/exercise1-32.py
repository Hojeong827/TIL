v1 = [1, 2, 3]
norm=(v1[0]**2+v1[1]**2+v1[2]**2)**0.5
print(norm)

v1 = [v1[0]/norm, v1[1]/norm, v1[2]/norm]

'''
method.2
v1[0]=v1[0]/norm
v1[1]=v1[1]/norm
v1[2]=v1[2]/norm
'''

'''
method.3
norm_vectotr=list()
norm_vector.append(v1[0]/norm)
norm_vector.append(v1[1]/norm)
norm_vector.append(v1[2]/norm)
norm=(norm_vector[0]**2+norm_vecotr[1]**2+norm_vector[2]**2)**0.5
print(norm)
'''

norm=(v1[0]**2+v1[1]**2+v1[2]**2)**0.5
print(norm)