import numpy as np
from sklearn.decomposition import KernelPCA
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt


X, y = make_moons(n_samples=100, noise=0.1)

kpca = KernelPCA(n_components=2, kernel='rbf', gamma=15)

X_kpca = kpca.fit_transform(X)

plt.figure(figsize=(8, 4))

plt.subplot(1,2,1)
plt.scatter(X[:,0], X[:,1], c=y, cmap='viridis')
plt.title('Original Data')


plt.subplot(1,2,2)
plt.scatter(X_kpca[:,0], X_kpca[:,1], c=y, cmap='viridis')
plt.title('Data after kPCA')


plt.show()