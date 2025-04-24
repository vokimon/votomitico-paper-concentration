import numpy as np
import matplotlib.pyplot as plt

# Parámetros
np.random.seed(42)
num_simulaciones = 100000
total_votos = 500_000
num_partidos = 6
num_escanos = 20

media_porcentajes = np.array([0.30, 0.25, 0.24, 0.15, 0.12, 0.10, 0.08])
media_porcentajes /= media_porcentajes.sum()
concentracion_total = 200
alpha = media_porcentajes * concentracion_total

restos_grandes_filtrados = []
restos_pequenos_filtrados = []

def calcular_restos_filtrados(votos_fila, num_escanos):
    cocientes = []
    for i, votos in enumerate(votos_fila):
        cocientes += [(votos / (j + 1), i) for j in range(num_escanos)]
    cocientes.sort(reverse=True)

    escaños = [0] * len(votos_fila)
    for _, i in cocientes[:num_escanos]:
        escaños[i] += 1

    umbral = cocientes[num_escanos - 1][0]
    total_votos_lista = np.sum(votos_fila)
    porcentajes = votos_fila / total_votos_lista
    grandes_indices = np.argsort(porcentajes)[-3:]

    for i, e in enumerate(escaños):
        if e >= 2:
            resto = votos_fila[i] - (e * umbral)
            if not resto: continue
            resto_pct = resto / umbral
            if i in grandes_indices:
                restos_grandes_filtrados.append(resto_pct * 100)
            else:
                restos_pequenos_filtrados.append(resto_pct * 100)

# Ejecutar simulaciones
for _ in range(num_simulaciones):
    proporciones = np.random.dirichlet(alpha)
    votos_fila = np.random.multinomial(total_votos, proporciones)
    calcular_restos_filtrados(votos_fila, num_escanos)

# Graficar resultados
plt.figure(figsize=(12, 6))
plt.hist(restos_grandes_filtrados, bins=100, color='royalblue', alpha=0.6, label='Grandes (≥2 escaños, sin bin 0)', density=True)
plt.hist(restos_pequenos_filtrados, bins=100, color='tomato', alpha=0.6, label='Pequeños (≥2 escaños, sin bin 0)', density=True)
plt.title('Distribución de restos (% respecto al cociente de corte)\nSolo partidos con ≥2 escaños, excluyendo restos = 0')
plt.xlabel('Resto (%)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
