import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros
mu = 100_000       # media de votos esperados del partido
sigma = 4000       # desviación típica de los votos
k_plus_1 = 6       # siguiente cociente (escaño que se quiere ganar)
C = 20_000         # cociente umbral de otro partido a superar
threshold = C * k_plus_1  # votos necesarios para obtener el siguiente escaño

# Resto: cuánto le falta al partido para alcanzar el siguiente cociente
# R = threshold - V, y V ~ N(mu, sigma)
# Por tanto, R ~ N(threshold - mu, sigma)

rest_mu = threshold - mu
x = np.linspace(rest_mu - 4*sigma, rest_mu + 4*sigma, 1000)
pdf = norm.pdf(x, loc=rest_mu, scale=sigma)

# Graficamos
plt.figure(figsize=(10, 5))
plt.plot(x, pdf, label='Distribución del resto (R)', color='blue')
plt.axvline(0, color='red', linestyle='--', label='Umbral exacto del escaño')
plt.fill_between(x, 0, pdf, where=(x > 0) & (x < 0.05 * threshold), color='green', alpha=0.3,
                 label='Probabilidad de estar a <5% del umbral')
plt.title('Distribución de los "restos" para el siguiente escaño')
plt.xlabel('Resto (votos necesarios para alcanzar el siguiente escaño)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Probabilidad de estar a menos del 5% del cociente del siguiente escaño
epsilon = 0.05 * threshold
p_near = norm.cdf(epsilon, loc=rest_mu, scale=sigma) - norm.cdf(0, loc=rest_mu, scale=sigma)
print(f"Probabilidad de estar a menos del 5% del siguiente escaño: {p_near:.2%}")
