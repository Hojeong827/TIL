scores=[60, 40, 70, 20, 30]
M, m = 0, 100

for score in scores:
    if score>M:
        M=score
    if score<m:
        m=score
        
print("Max value: ", M)
print("min value: ", m)