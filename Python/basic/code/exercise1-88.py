scores=[[10, 15, 20], [20, 25, 30], [30, 35, 40], [40, 45, 50]]

n_studnet = len(scores)
n_class = len(scores[0])

class_score_sums=list()
class_score_means = list()
class_score_square_sums = list()

class_score_variance = list()
class_socre_stds = list()

# set the sum of class socres as 0
for _ in range(n_class):
    class_score_sums.append(0)
    class_score_square_sums.append(0)

# classes' sums, squared sums
for student_scores in scores:
    for class_idx in range(n_class):
        class_score_sums[class_idx] += student_scores[class_idx]
        class_score_square_sums[class_idx] += student_scores[class_idx]**2
        
for class_idx in range(n_class):
    class_score_means.append(class_score_sums[class_idx]/n_studnet)

# classes' variances
for class_idx in range(n_class):
    mos = class_score_square_sums[class_idx]/n_studnet
    som = class_score_means[class_idx]**2
    
    variance = mos - som
    std = variance**0.5
    
    class_score_variance.append(variance)
    class_socre_stds.append(std)

# classes' standard deviations
print("standard deviations: ", class_socre_stds)

for student_idx in range(n_studnet):
    for class_idx in range(n_class):
        score=scores[student_idx][class_idx]
        mean = class_score_means[class_idx]
        std = class_socre_stds[class_idx]
        
        scores[student_idx][class_idx] = (score-mean)/std
        
class_score_sums=list()
class_score_means = list()
class_score_square_sums = list()

class_score_variance = list()
class_socre_stds = list()

# set the sum of class socres as 0
for _ in range(n_class):
    class_score_sums.append(0)
    class_score_square_sums.append(0)

# classes' sums, squared sums
for student_scores in scores:
    for class_idx in range(n_class):
        class_score_sums[class_idx] += student_scores[class_idx]
        class_score_square_sums[class_idx] += student_scores[class_idx]**2

for class_idx in range(n_class):
    class_score_means.append(class_score_sums[class_idx]/n_studnet)

# classes' variances
for class_idx in range(n_class):
    mos = class_score_square_sums[class_idx]/n_studnet
    som = class_score_means[class_idx]**2
    
    variance = mos - som
    std = variance**0.5
    
    class_score_variance.append(variance)
    class_socre_stds.append(std)

# classes' standard deviations
print("standard deviations: ", class_socre_stds)
