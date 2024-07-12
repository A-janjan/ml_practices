import numpy as np
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Generate some sparse data
np.random.seed(42)
X = np.random.randn(100, 1) * 20
y = (X > 10).astype(int).ravel()

# Binning the data
binning = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')

X_binned = binning.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_binned, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")

# Check the bin edges
print(f"Bin edges: {binning.bin_edges_}")