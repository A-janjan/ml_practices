from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# Sample corpus
corpus = [
    "The cat sat on the mat.",
    "The dog sat on the mat.",
    "The fox jumped over the fence."
]

# Step 1: Convert the documents into a TF-IDF matrix
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Step 2: Apply TruncatedSVD (LSA) with 2 components (for simplicity)
lsa = TruncatedSVD(n_components=2)
X_reduced = lsa.fit_transform(X)

# Step 3: Display the reduced matrix
print("Reduced Feature Matrix:\n", X_reduced)

# Display the components (topics)
print("Topics (terms contributing to each latent dimension):\n", lsa.components_)
