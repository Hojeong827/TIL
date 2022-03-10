scores = [-20, 60, 40, 70, 120]

# method.1
M, m = scores[0], scores[0]
for score in scores:
    if score>M:
        M=score
    if score<m:
        m=score
print("Max value: ", M)
print("Min value: ", m)

# method.2
M, m = None, None
for score in scores:
    if M==None or score>M:
        M=score
    if m==None or score<m:
        m=score
print("Max value: ", M)
print("Min value: ", m)