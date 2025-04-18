import numpy as np
import matplotlib.pyplot as plt

# a) Geração do sinal original e adição de ruído
t = np.arange(0, 50)
x = 2 * t * (0.9 ** t)
ruido = np.random.randn(len(t))  # Ruído gaussiano
x_ruidoso = x + ruido

# b) Aplicação do filtro de média móvel de 3 pontos (não causal para comparação)
# Média móvel simples: [-1, 0, +1] pontos (centro na amostra atual)
janela = np.ones(3) / 3
x_filtrado = np.convolve(x_ruidoso, janela, mode='same')  # usa pontos anteriores e posteriores

# c) Visualização
plt.figure(figsize=(12, 6))
plt.plot(t, x, label='Sinal original', linewidth=2)
plt.plot(t, x_ruidoso, label='Sinal com ruído', alpha=0.6)
plt.plot(t, x_filtrado, label='Sinal filtrado (média móvel)', linewidth=2)
plt.title('Sinal original, ruidoso e filtrado')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# d) Verificação de causalidade
print("🔎 O filtro aplicado é causal?")
print("❌ Não. O filtro de média móvel aplicado (com 'mode=same') usa amostras passadas e futuras.\n"
      "Para ser causal, o filtro só pode depender do presente e do passado.")
