scores = [-20, 60, 40, 70, 120]

M, m = scores[0], scores[0]
for score in scores:
    if score>M:
        M=score
    if score<m:
        m=score
print("Max value: ", M)
print("Min value: ", m)

for score_idx in range(len(scores)):
    scores[score_idx] = (scores[score_idx]-m)/(M-m)

print("scores after normalization:\n", scores)

M, m = scores[0], scores[0]
for score in scores:
    if score>M:
        M=score
    if score<m:
        m=score
print("Max value: ", M)
print("Min value: ", m)