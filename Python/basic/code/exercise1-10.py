score1=10
score2=20
score3=30
n_student=3
score_mean=(score1+score2+score3)/n_student

score1-=score_mean
score2-=score_mean
score3-=score_mean

score_mean=(score1+score2+score3)/n_student
print(score_mean)