import numpy as np
import matplotlib.pyplot as plt

# intervalo de n
n = np.arange(-2, 10)

# Função degrau unitário
def u(n):
    return np.where(n >= 0, 1, 0)

# Sinal original x[n] = u[n - 1] - u[n - 5]
x = u(n - 1) - u(n - 5)

# a) x[n - 1]
xA = u(n - 2) - u(n - 6) # Atraso de 1 unidade
plt.stem(n, xA, basefmt="k")
plt.title("a) x[n - 1]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# b) x[n + 2]
xB = u(n + 1) - u(n - 3) # Avanço de 2 unidades
plt.stem(n, xB, basefmt="k")
plt.title("b) x[n + 2]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# c) x[2 - n]
xC = u(1 - n) - u(-3 - n) # Reflexão e avanço
plt.stem(n, xC, basefmt="k")
plt.title("c) x[2 - n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# d) x[n] * u[2 - n]
xD = x * u(2 - n) # Multiplicação com janela até n = 2
plt.stem(n, xD, basefmt="k")
plt.title("d) x[n] * u[2 - n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
