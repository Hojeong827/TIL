scores=[20, 50, 10, 60, 70]
cutoff=50

for score in scores:
    if score > cutoff:
        print("Pass!")
    else:
        print("Try Again!")