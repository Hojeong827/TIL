predictions = [0, 1, 0, 2, 1, 2, 0]
labels = [1, 1, 0, 0, 1, 2, 1]

n_data=len(predictions)
n_correct=0

for pred_idx in range(n_data):
    pred=predictions[pred_idx];
    label=labels[pred_idx]
    if pred == label:
        n_correct +=1

accuracy=n_correct / n_data
print("accuracy[%]: ", accuracy*100, '%')