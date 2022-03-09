predictions = [10, 20, 30]
labels = [10, 25, 40]

n_data = len(predictions)
diff_square_sum=0

for data_idx in range(n_data):
    diff_square_sum+=(predictions[data_idx]-labels[data_idx])**2
mse=diff_square_sum/n_data
print("MSE: ", mse)