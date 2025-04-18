import numpy as np
import matplotlib.pyplot as plt

# Parte A - Sinal original
n1 = np.arange(0, 50)
A1 = 3
f1 = 0.08
x1 = A1 * np.cos(np.pi * f1 * n1)

# Parte B - Sinal modificado
n2 = np.arange(0, 80)
A2 = 1.5
f2 = 0.5
x2 = A2 * np.cos(np.pi * f2 * n2)

# Parte C - Visualização dos dois sinais com stem, plot e stairs
def plot_signal(n, x, title):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    
    axs[0].stem(n, x, basefmt=" ")
    axs[0].set_title(f'{title} - Função stem')
    axs[0].grid(True)
    
    axs[1].plot(n, x, color='orange')
    axs[1].set_title(f'{title} - Função plot')
    axs[1].grid(True)
    
    axs[2].stairs(x, color='green')
    axs[2].set_title(f'{title} - Função stairs')
    axs[2].grid(True)
    
    plt.tight_layout()
    plt.show()

# Parte A - sinal original
plot_signal(n1, x1, "Sinal original")

# Parte C - sinal modificado
plot_signal(n2, x2, "Sinal modificado")
