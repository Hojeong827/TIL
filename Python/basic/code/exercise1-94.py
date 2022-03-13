scores = [[10, 40, 20], [50, 20, 60], [70, 40, 30], [30, 80, 40]]
n_student = len(scores)
n_class = len(scores[0])

M_classes = scores[0]
M_idx_classes = list()
for _ in range(n_class):
    M_idx_classes.append(0)

for student_idx in range(n_student):
    student_scores = scores[student_idx]
    for class_idx in range(n_class):
        score = student_scores[class_idx]
        if score > M_classes[class_idx]:
            M_classes[class_idx] = score
            M_idx_classes[class_idx] = student_idx
            
print("Max scores: ", M_classes)
print("Max score indices: ", M_idx_classes)