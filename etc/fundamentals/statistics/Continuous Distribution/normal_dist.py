import numpy as np
import matplotlib.pyplot as plt


sigma = 1
mu = 0


x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)


y = (1/(np.sqrt(2*np.pi)*sigma)) * np.exp(-0.5 * (x-mu)**2 / sigma**2)


plt.plot(x, y)

plt.title('Normal Distribution (mean=0, std=1)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.show()