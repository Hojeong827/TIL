scores = [20, 50, 10, 60, 90]
cutoff = 50

p_score_sum, n_p = 0, 0
np_score_sum, n_np = 0, 0

for score in scores:
    if score>cutoff:
        p_score_sum+=score
        n_p+=1
    else:
        np_score_sum+=score
        n_np+=1

p_score_mean=p_score_sum/n_p
np_score_mean=np_score_sum/n_np
print("mean of passed scores: ", p_score_mean)
print("mean of no passed scores: ", np_score_mean)