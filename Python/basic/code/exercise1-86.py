scores=[[10, 15, 20], [20, 25, 30], [30, 35, 40], [40, 45, 50]]
n_student = len(scores)
n_class = len(scores[0])

class_score_sums = list()
class_score_means = list()

# set the sum of class scores as 0
for _ in range(n_class):
    class_score_sums.append(0)

# calculate the sum of class scores
for student_scores in scores:
    for class_idx in range(n_class):
        class_score_sums[class_idx] += student_scores[class_idx]

# calculate the mean of class scores
for class_idx in range(n_class):
    class_score_means.append(class_score_sums[class_idx]/n_student)
print("mean of classes' scores: ", class_score_means)

for student_idx in range(n_student):
    for class_idx in range(n_class):
        scores[student_idx][class_idx] -= class_score_means[class_idx]
        
class_score_sums = list()
class_score_means = list()

# set the sum of class scores as 0
for _ in range(n_class):
    class_score_sums.append(0)

# calculate the sum of class scores
for student_scores in scores:
    for class_idx in range(n_class):
        class_score_sums[class_idx] += student_scores[class_idx]

# calculate the mean of class scores
for class_idx in range(n_class):
    class_score_means.append(class_score_sums[class_idx]/n_student)
print("mean of classes' scores: ", class_score_means)