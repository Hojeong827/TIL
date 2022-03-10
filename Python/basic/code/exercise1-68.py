scores=[20, 50, 10, 60, 90]
grades = list()
for score in scores:
    if score>80:
        grades.append('A')
    elif score>60:
        grades.append('B')
    elif score>40:
        grades.append('C')
    else:
        grades.append('F')
print(grades)