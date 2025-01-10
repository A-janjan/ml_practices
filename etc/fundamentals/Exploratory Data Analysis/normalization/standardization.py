from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[10], [20], [30], [40], [50]])

scaler = StandardScaler()

standardized_data = scaler.fit_transform(data)

print(standardized_data)