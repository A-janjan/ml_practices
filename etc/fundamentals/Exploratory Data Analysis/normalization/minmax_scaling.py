import numpy as np
from sklearn.preprocessing import MinMaxScaler


data = np.array([[10], [20], [30], [40], [50]])
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

print(normalized_data)