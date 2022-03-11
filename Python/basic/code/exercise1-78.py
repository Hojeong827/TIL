predictions = [0, 1, 0, 2, 1, 2, 0]
labels = [1, 1, 0, 0, 1, 2, 1]

M_class = None
for label in labels:
    if M_class==None or label> M_class:
        M_class = label
M_class+=1

class_cnts, correct_cnts, confusion_vec = list(), list(), list()
for _ in range(M_class):
    class_cnts.append(0)
    correct_cnts.append(0)
    confusion_vec.append(None)
    
for pred_idx in range(len(predictions)):
    pred=predictions[pred_idx]
    label=labels[pred_idx]
    
    class_cnts[label]+=1
    if pred == label:
        correct_cnts[label]+=1
        
for class_idx in range(M_class):
    confusion_vec[class_idx] = correct_cnts[class_idx]/class_cnts[class_idx]
print("confusion vector: ", confusion_vec)