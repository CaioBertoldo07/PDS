import numpy as np
import matplotlib.pyplot as plt

# Eixo n
n = np.arange(-10, 11)

# Sinais degrau
u_n = np.where(n >= 0, 1, 0)
u_n_minus_1 = np.where(n >= 1, 1, 0)

# Plot
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.stem(n, u_n)
plt.title(r'$u[n]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(n, u_n_minus_1)
plt.title(r'$u[n - 1]$')
plt.xlabel('n')
plt.grid(True)

plt.tight_layout()
plt.show()
