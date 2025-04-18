import numpy as np
import matplotlib.pyplot as plt

# Sinal x
x = np.concatenate([np.zeros(5), np.ones(5), np.zeros(5)])
y = np.arange(15)

# Convoluções
w = np.convolve(x, x)
z = np.convolve(x, y)

# Eixo para w e z
n_wz = np.arange(1, len(w) + 1)

# Criação dos subplots
plt.figure(figsize=(10, 8))  # aumenta o tamanho da figura

# x[n]
plt.subplot(3, 1, 1)
plt.stem(y, x)
plt.title('x[n]')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)

# w[n] = x * x
plt.subplot(3, 1, 2)
plt.stem(n_wz, w)
plt.title('w[n] = x[n] * x[n]')
plt.xlabel('Tempo')
plt.ylabel('w[n]')
plt.grid(True)

# z[n] = x * y
plt.subplot(3, 1, 3)
plt.stem(n_wz, z)
plt.title('z[n] = x[n] * y[n]')
plt.xlabel('Tempo')
plt.ylabel('z[n]')
plt.grid(True)

# Título geral e ajuste de layout
plt.suptitle('Convoluções envolvendo x[n]', fontsize=14)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # reserva espaço pro suptitle

plt.show()

print("Tamanhos: z =", len(z), ", w =", len(w))
