pred1, pred2, pred3 = 10, 20, 30
y1, y2, y3 = 10, 25, 40
n_data=3

squared_error1=(pred1-y1)**2
squared_error2=(pred2-y2)**2
squared_error3=(pred3-y3)**2

mean_squared_error=(squared_error1+squared_error2+squared_error3)/n_data
print(mean_squared_error)