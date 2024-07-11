import numpy as np

data = np.array([[1], [10], [100], [1000], [10000]])

log_transformed_data = np.log1p(data)


print(log_transformed_data)