scores = [50, 20, 30, 40, 10, 50, 70, 80, 90, 20, 30]
cutoffs = [0, 20, 40, 60, 80]
histogram = [0, 0, 0, 0, 0]

for score in scores:
    if score > cutoffs[4]:
        histogram[4] += 1
    elif score > cutoffs[3]:
        histogram[3] += 1
    elif score > cutoffs[2]:
        histogram[2] += 1
    elif score > cutoffs[1]:
        histogram[1] += 1
    elif score > cutoffs[0]:
        histogram[0] += 1
    else: 
        pass
print("histogram of the scores: ", histogram)