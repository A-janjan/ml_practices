# Import required libraries
import pandas as pd
from sklearn.datasets import load_iris
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt


df = pd.read_csv("bfi.csv")

df.drop(['gender', 'education', 'age'], axis=1, inplace=True)

df.dropna(inplace=True)


# can we found the factors in the dataset?
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

chi_square_value, p_value = calculate_bartlett_sphericity(df)
print(chi_square_value)
print(p_value)

# Kaiser-Meyer-Olkin (KMO) Test measures the suitability of data for factor analysis.
from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all, kmo_model = calculate_kmo(df)

## Value of KMO less than 0.6 is considered inadequate.
print(kmo_model)

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer(n_factors=25, rotation=None)
fa.fit(df)

# check eigenvalues
ev, v = fa.get_eigenvalues()

print("$$$$", ev)

##### we need eigenvalues which are greater than 1

# Get variance of each factors
fa.get_factor_variance()

# Create scree plot using matplotlib
plt.scatter(range(1,df.shape[1]+1),ev)
plt.plot(range(1,df.shape[1]+1),ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()