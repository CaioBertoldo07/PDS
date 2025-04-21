import numpy as np
import matplotlib.pyplot as plt

# Eixo n
n = np.arange(-10, 11)

# Sinais delta
delta_n = np.where(n == 0, 1, 0)
delta_n_minus_2 = np.where(n == 2, 1, 0)
delta_n_plus_3 = np.where(n == -3, 1, 0)

# Plot
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.stem(n, delta_n)
plt.title(r'$\delta[n]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(1, 3, 2)
plt.stem(n, delta_n_minus_2)
plt.title(r'$\delta[n - 2]$')
plt.xlabel('n')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.stem(n, delta_n_plus_3)
plt.title(r'$\delta[n + 3]$')
plt.xlabel('n')
plt.grid(True)

plt.tight_layout()
plt.show()
