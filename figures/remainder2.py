import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros del modelo
mu = 100_000       # media de votos esperados
sigma = 4000       # desviación típica de votos
k_plus_1 = 6       # siguiente escaño
C = 20_000         # cociente por escaño
threshold = C * k_plus_1

# El resto es: R = threshold - V
# Distribución: R ~ N(threshold - mu, sigma)
rest_mu = threshold - mu

# Eje X = votos de resto (es decir, distancia al siguiente escaño)
x = np.linspace(rest_mu - 4*sigma, rest_mu + 4*sigma, 1000)
pdf = norm.pdf(x, loc=rest_mu, scale=sigma)

# Graficamos
plt.figure(figsize=(10, 5))
plt.plot(x, pdf, color='purple', label='Densidad puntual del resto')
plt.axvline(0, color='red', linestyle='--', label='Umbral exacto del siguiente escaño')
plt.title('Distribución de probabilidad del resto electoral')
plt.xlabel('Resto (votos necesarios para alcanzar el siguiente escaño)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
