scores = [40, 20, 30, 10, 50]
sorted_scores = list()

for _ in range(len(scores)):
    M, M_idx = scores[0], 0
    
    for score_idx in range(len(scores)):
        if scores[score_idx]>M:
            M=scores[score_idx]
            M_idx=score_idx
    
    temp_scores=list()
    for score_idx in range(len(scores)):
        if score_idx == M_idx:
            sorted_scores.append(scores[score_idx])
        else:
            temp_scores.append(scores[score_idx])
    scores=temp_scores
    print("reamining scores: ", scores)
    print("sorted scores: ", sorted_scores, '\n')