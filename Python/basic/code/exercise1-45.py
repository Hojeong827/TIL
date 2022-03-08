scores = [10, 20, 30]

# method. 1
score_sum = 0
n_student = 0
for score in scores:
    score_sum += score
    n_student += 1
score_mean = score_sum / n_student
print("score_mean: ", score_mean)

# method. 2
score_sum=0
for score_idx in range(len(scores)):
    score_sum += scores[score_idx]
score_mean = score_sum / len(scores)
print("score mean: ", score_mean)