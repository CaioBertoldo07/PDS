import numpy as np
import matplotlib.pyplot as plt

# Eixo n
n = np.arange(-5, 6, 1)  # De -5 até 5

# Definindo os sinais
delta_n = np.where(n == 0, 1, 0)
delta_n_minus_2 = np.where(n == 2, 1, 0)
delta_n_plus_3 = np.where(n == -3, 1, 0)

# Criar uma figura com 3 subplots (um para cada impulso)
plt.figure(figsize=(8, 8))

# Primeiro gráfico: δ[n]
plt.subplot(3, 1, 1)
plt.stem(n, delta_n, linefmt='b-', markerfmt='bo', basefmt=" ")
plt.title('δ[n]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(0, 1.5)

# Segundo gráfico: δ[n-2]
plt.subplot(3, 1, 2)
plt.stem(n, delta_n_minus_2, linefmt='g-', markerfmt='go', basefmt=" ")
plt.title('δ[n-2]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(0, 1.5)

# Terceiro gráfico: δ[n+3]
plt.subplot(3, 1, 3)
plt.stem(n, delta_n_plus_3, linefmt='r-', markerfmt='ro', basefmt=" ")
plt.title('δ[n+3]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(0, 1.5)

plt.tight_layout()
plt.show()
