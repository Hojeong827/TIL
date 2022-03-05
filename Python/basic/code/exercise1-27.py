scores = [10, 20, 30]
n_student = len(scores)
mean = (scores[0] + scores[1] + scores[2])/n_student
square_of_mean=mean**2 #평균의 제곰
mean_of_square = (scores[0]**2 + scores[1]**2 + scores[2]**2)/n_student # 제곱의 평균

variance = mean_of_square - square_of_mean # MOS - SOM
std = variance**0.5 # square root of the variance

print("score mean: ", mean)
print("score standard deviation: ", std)

scores[0] = (scores[0] - mean)/std
scores[1] = (scores[1] - mean)/std
scores[2] = (scores[2] - mean)/std

mean = (scores[0] + scores[1] + scores[2])/n_student
square_of_mean=mean**2 #평균의 제곰
mean_of_square = (scores[0]**2 + scores[1]**2 + scores[2]**2)/n_student # 제곱의 평균

variance = mean_of_square - square_of_mean # MOS - SOM
std = variance**0.5 # square root of the variance

print("score mean: ", mean)
print("score standard deviation: ", std)