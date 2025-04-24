import numpy as np
import matplotlib.pyplot as plt

# Simulación Monte Carlo
np.random.seed(32)
num_simulaciones = 1_000

# Parámetros básicos
total_votos = 6_000
num_partidos = 6
num_escanos = 10

# Reparto medio de voto por partido
peso_medio = np.array([0.30, 0.25, 0.15, 0.12, 0.10, 0.08])
peso_medio /= peso_medio.sum()

# Simulaciones de votos
votos_simulados = np.random.multinomial(total_votos, peso_medio, size=num_simulaciones)

# Función de cálculo D'Hondt y restos
def calcular_restos_y_cocientes(votos_fila, num_escanos):
    partidos_con_escanos = []
    cocientes = [
        (votos / (j + 1), i)
        for j in range(num_escanos)
        for i, votos in enumerate(votos_fila)
    ]


    cocientes.sort(reverse=True)
    escaños = [0] * len(votos_fila)
    for _, i in cocientes[:num_escanos]:
        escaños[i] += 1

    umbral = cocientes[num_escanos - 1][0]  # último cociente que entra

    restos_pct = []
    for i, e in enumerate(escaños):
        if e <= 0:
            continue
        cociente_actual = votos_fila[i] / e
        resto = votos_fila[i] - (e * umbral)
        resto_pct = resto / umbral
        if resto == 0:
            continue
        restos_pct.append(resto_pct)
    return restos_pct

# Ejecutar simulación
restos_percentuales = []
for votos_fila in votos_simulados:
    restos = calcular_restos_y_cocientes(votos_fila, num_escanos)
    restos_percentuales.extend(restos)

# Convertir a %
restos_percentuales = np.array(restos_percentuales) * 100

# Gráfica
plt.figure(figsize=(10, 6))
plt.hist(restos_percentuales, bins=100, color='skyblue', edgecolor='k', density=True)
plt.title('Distribución de porcentajes de resto sobre el cociente de corte\n(para candidaturas con escaño)')
plt.xlabel('Resto (%) respecto al cociente de corte')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.tight_layout()
plt.show()
