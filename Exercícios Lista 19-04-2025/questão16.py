import numpy as np
import matplotlib.pyplot as plt

# Definindo o intervalo de n
n = np.arange(-2, 6)

# Definindo a sequência
x = np.array([2, 0, 3, 0, 0, -3, 0, 0])

# Gráfico de impulso
plt.stem(n, x, basefmt=" ")
plt.title('x[n] representado com impulsos unitários')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()
