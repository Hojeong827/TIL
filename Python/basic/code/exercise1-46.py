scores = [10, 20, 30]

score_sum=0
for score_idx in range(len(scores)):
    score_sum += scores[score_idx]
score_mean = score_sum / len(scores)

# method.1
score_ms=list()
for score in scores:
    score_ms.append(score-score_mean)
print(score_ms)

# method.2
for score_idx in range(len(scores)):
    scores[score_idx] -= score_mean
print(scores)