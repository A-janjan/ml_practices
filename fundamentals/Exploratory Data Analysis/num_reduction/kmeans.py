import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = np.array([[170, 70], [165, 65], [180, 80], [175, 75], [160, 60]])

kmeans = KMeans(n_clusters=3)

kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_


plt.scatter(X[:, 0], X[:,1], c=labels, cmap='viridis')
plt.scatter(centroids[:,0], centroids[:,1], c='red', marker='X')

plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('K-Means Clustering')
plt.show()