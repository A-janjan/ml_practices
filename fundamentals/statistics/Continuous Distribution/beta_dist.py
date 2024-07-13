import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

alpha_values = [0.5, 1, 2, 2, 5]
beta_values = [0.5, 1, 2, 5, 2]


x = np.linspace(0,1,1000)

plt.figure(figsize=(12, 8))


for alpha, beta_param in zip(alpha_values, beta_values):
    y = beta.pdf(x, alpha, beta_param)
    plt.plot(x, y, label=f'α={alpha}, β={beta_param}')
    
    
plt.title('Beta Distribution PDFs')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.show()