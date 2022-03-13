labels = [0, 1, 2, 1, 0 ,3]

n_label = len(labels)
n_class = 0
for label in labels:
    if label > n_class:
        n_class = label
n_class+=1
one_hot_mat = list()
for label in labels:
    one_hot_vec=list()
    for _ in range(n_class):
        one_hot_vec.append(0)
    one_hot_vec[label]=1
    one_hot_mat.append(one_hot_vec)
print(one_hot_mat)