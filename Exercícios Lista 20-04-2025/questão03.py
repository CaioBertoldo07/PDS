import numpy as np
import matplotlib.pyplot as plt

# Eixo n
n = np.arange(-5, 6)

# Sinal x[n] = u[n - 1] - u[n - 2]
x = np.where(n >= 1, 1, 0) - np.where(n >= 2, 1, 0)

# Plot
plt.figure(figsize=(6, 4))
plt.stem(n, x)
plt.title(r'$x[n] = u[n - 1] - u[n - 2]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()
