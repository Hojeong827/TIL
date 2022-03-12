scores=[[10, 15, 20], [20, 25, 30], [30, 35, 40], [40, 45, 50]]
n_class = len(scores[0])
student_score_means = list()

for student_scores in scores:
    student_score_sum=0
    for score in student_scores:
        student_score_sum += score
    student_score_means.append(student_score_sum/n_class)
    
print("mean of students' socress: ", student_score_means)