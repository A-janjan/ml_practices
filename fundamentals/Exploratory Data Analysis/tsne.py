from sklearn.datasets import load_iris
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data

tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000)

tsne_result = tsne.fit_transform(X)


plt.scatter(tsne_result[:, 0], tsne_result[:, 1], label='after tsne')
plt.scatter(X[:, 0], X[:, 1], label='original')
plt.title('t-SNE visualization')
plt.legend()
plt.show()