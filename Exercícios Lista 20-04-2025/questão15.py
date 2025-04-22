import numpy as np
import matplotlib.pyplot as plt

# Sinal x[n]
x = np.array([1, 2, 3])
xIndexes = np.arange(0, 3)

# Sinal h[n], com posição zero no valor 3
h = np.array([1, 3, 1])
hIndexes = np.arange(-1, 2)

# Convolução
y = np.convolve(x, h)

# Índices do resultado
yStart = xIndexes[0] + hIndexes[0]
yEnd = xIndexes[-1] + hIndexes[-1]
yIndexes = np.arange(yStart, yEnd + 1)

#Plot
plt.stem(yIndexes, y)
plt.title("y[n] = x[n] * h[n]")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)
plt.show()
