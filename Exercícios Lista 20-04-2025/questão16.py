import numpy as np
import matplotlib.pyplot as plt

# Sinal x[n]
x = np.array([2, 2, 1, 1])
xN = np.arange(0, 4)

# Sinal h[n] com h[0] = 3
h = np.array([0, 3, -2, 1, 0])
hN = np.arange(-1, 4)

# Convolução
y = np.convolve(x, h)
yN = np.arange(xN[0] + hN[0], xN[-1] + hN[-1] + 1)

# Plot
plt.stem(yN, y)
plt.title("Convolução y[n] = x[n] * h[n]")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)
plt.tight_layout()
plt.show()
