from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np


iris = load_iris()
X = iris.data
y = iris.target


scalar = StandardScaler()
X_std = scalar.fit_transform(X)

pca = PCA(n_components=2)
x_pca = pca.fit_transform(X_std)


plt.figure(figsize=(8, 6))

for target in np.unique(y):
    plt.scatter(x_pca[y==target,0], x_pca[y==target, 1], label=iris.target_names[target])
    plt.scatter(X[y==target,0], X[y==target, 1], label=iris.target_names[target]+" orginal")

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Iris Dataset')
plt.legend()
plt.show()