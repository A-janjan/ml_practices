import numpy as np
import matplotlib.pyplot as plt

# parameters
a = 2
b = 5


# PDF
x = np.linspace(a-1, b+1, 1000)

pdf = np.where((x >= a) & (x <= b), 1/(b-a), 0)


# CDF
cdf = np.piecewise(x, [x<a, (x>=a) & (x<=b), x>b], [0,lambda x: (x-a)/(b-a), 1])


# Plot PDF
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, pdf, 'b', label='PDF')
plt.fill_between(x, pdf, 0, where=((x >= a) & (x <= b)), color='blue', alpha=0.3)
plt.title('Uniform Distribution PDF')
plt.xlabel('x')
plt.ylabel('f_X(x)')
plt.legend()

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf, 'r', label='CDF')
plt.title('Uniform Distribution CDF')
plt.xlabel('x')
plt.ylabel('F_X(x)')
plt.legend()

plt.show()