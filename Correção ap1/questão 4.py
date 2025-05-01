import numpy as np
import matplotlib.pyplot as plt

# Frequências e amplitudes
frequencies_A = [1, 2, 3]  # Frequências em kHz (1kHz, 2kHz, 3kHz - 3kHz é alias de 7kHz)
amplitudes_A = [1, 1, 1]   # Amplitudes arbitrárias

frequencies_B = [1, 2]     # Frequências em kHz (1kHz, 2kHz)
amplitudes_B = [1, 1]

# Gráfico A - Sem filtro anti-aliasing
plt.figure(figsize=(6, 4))
plt.stem(frequencies_A, amplitudes_A, basefmt=" ")
plt.xlabel('Frequência (kHz)')
plt.ylabel('Amplitude')
plt.title('A) Sem Filtro Anti-Aliasing')
plt.grid(True)
plt.ylim(0, 1.2)
plt.xlim(0, 5)
plt.show()

# Gráfico B - Com filtro anti-aliasing
plt.figure(figsize=(6, 4))
plt.stem(frequencies_B, amplitudes_B, basefmt=" ")
plt.xlabel('Frequência (kHz)')
plt.ylabel('Amplitude')
plt.title('B) Com Filtro Anti-Aliasing')
plt.grid(True)
plt.ylim(0, 1.2)
plt.xlim(0, 5)
plt.show()
