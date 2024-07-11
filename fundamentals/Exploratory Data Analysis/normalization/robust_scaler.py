from sklearn.preprocessing import RobustScaler
import numpy as np


data = np.array([[10], [20], [30], [40], [50]])

scaler = RobustScaler()

normalized_data = scaler.fit_transform(data)

print(normalized_data)