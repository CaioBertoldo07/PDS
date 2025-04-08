import numpy as np
import matplotlib.pyplot as plt

#  Função degrau unitário (u[n])
def u(n):
    return np.where(n >= 0, 1, 0)

# Domínio do sinal
n = np.arange(0, 20)

# Sinal h[n] = u[n] - u[n - 10]
h = u(n) - u(n - 10)

# Sinal x[n] = u[n - 2] - u[n - 7]
x = u(n - 2) - u(n - 7)

# Convolução de x[n] * h[n]
y = np.convolve(x, h)

# Novo eixo n para o sinal de saída y[n]
n_y = np.arange(2 * n[0], 2 * n[-1] + 1)

# Gráfico
plt.figure(figsize=(6,6))

plt.subplot(3, 1, 1)
plt.stem(n, h)
plt.title('h(n) = u[n] - u[n - 10]')
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(n, x)
plt.title('x[n] = u[n - 2] - u[n - 7]')
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(n_y, y)
plt.title('y[n] = x[n] * h[n]')
plt.grid()

plt.tight_layout()
plt.show()