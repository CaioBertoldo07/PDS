import numpy as np
import matplotlib.pyplot as plt

# Parâmetros iniciais
n = np.arange(0, 30)
A = 0.5

# Casos com diferentes valores de d
d_values = [0.8, 0.2, -0.2]
labels = ['d = 0.8', 'd = 0.2', 'd = -0.2']
colors = ['blue', 'green', 'red']

plt.figure(figsize=(10, 6))
for d, label, color in zip(d_values, labels, colors):
    x = A * np.exp(d * n)
    plt.plot(n, x, label=label, color=color)

plt.title('Sinais x = A * exp(d * n) para diferentes valores de d')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.legend()
plt.grid(True)
plt.show()
