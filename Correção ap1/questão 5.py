import numpy as np
import matplotlib.pyplot as plt

# Valores de n
n = np.array([-1, 0, 1, 2, 3])

# Valores de y[n]
y = np.array([1, 5, 10, 11, 3])

# Plotando o gráfico de hastes
plt.figure(figsize=(6, 4))
plt.stem(n, y, basefmt=" ")
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Convolução de x[n] com h[n]')
plt.grid(True)
plt.ylim(0, 12)  # Deixar um espaço acima do maior valor para ficar bonito
plt.show()
