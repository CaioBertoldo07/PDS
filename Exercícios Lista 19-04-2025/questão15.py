import numpy as np
import matplotlib.pyplot as plt

# Definindo intervalo de n
n = np.arange(-1, 5)

# Definindo a sequêcnia 
x = np.array([-1, 9, 7, 3, 8, 6])

# Gráfico do impulso
plt.stem(n, x, basefmt=" ")
plt.title('x[n] representado com impulsos unitários')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()