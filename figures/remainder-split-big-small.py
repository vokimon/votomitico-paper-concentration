import numpy as np
import matplotlib.pyplot as plt

# Parámetros de simulación
np.random.seed(42)
num_simulaciones = 100000
total_votos = 500_000
num_partidos = 6
num_escanos = 10

# Porcentajes medios de voto
media_porcentajes = np.array([0.30, 0.25, 0.15, 0.12, 0.10, 0.08])
media_porcentajes /= media_porcentajes.sum()

# Parámetro de concentración de la Dirichlet
concentracion_total = 200
alpha = media_porcentajes * concentracion_total

# Almacenamiento de restos
restos_grandes = []
restos_pequenos = []

# Función para clasificar los restos por tamaño de partido
def calcular_restos_por_tamano(votos_fila, num_escanos):
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

    # Partidos grandes: los 3 con más porcentaje
    grandes_indices = np.argsort(porcentajes)[-3:]

    for i, e in enumerate(escaños):
        if e > 0:
            cociente_actual = votos_fila[i] / e
            resto = votos_fila[i] - (e * umbral)
            resto_pct = resto / umbral
            if i in grandes_indices:
                restos_grandes.append(resto_pct * 100)
            else:
                restos_pequenos.append(resto_pct * 100)

# Simulación Monte Carlo
for _ in range(num_simulaciones):
    proporciones = np.random.dirichlet(alpha)
    votos_fila = np.random.multinomial(total_votos, proporciones)
    calcular_restos_por_tamano(votos_fila, num_escanos)

# Graficar resultados
plt.figure(figsize=(12, 6))
plt.hist(restos_grandes, bins=100, color='steelblue', alpha=0.6, label='Partidos grandes (con escaño)', density=True)
plt.hist(restos_pequenos, bins=100, color='darkorange', alpha=0.6, label='Partidos pequeños (con escaño)', density=True)
plt.title('Distribución de porcentajes de resto respecto al cociente de corte\nComparación entre partidos grandes y pequeños (ambos con escaños)')
plt.xlabel('Resto (%)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
