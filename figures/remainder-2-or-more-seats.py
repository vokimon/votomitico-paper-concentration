import numpy as np
import matplotlib.pyplot as plt

# Parámetros
np.random.seed(42)
num_simulaciones = 100000
total_votos = 500_000
num_partidos = 6
num_escanos = 10

media_porcentajes = np.array([0.30, 0.25, 0.15, 0.12, 0.10, 0.08])
media_porcentajes /= media_porcentajes.sum()
concentracion_total = 200
alpha = media_porcentajes * concentracion_total

# Almacén de restos de partidos con al menos 2 escaños
restos_dos_o_mas = []

# Función para calcular restos, pero solo para formaciones con al menos 2 escaños
def calcular_restos_dos_o_mas(votos_fila, num_escanos):
    cocientes = []
    for i, votos in enumerate(votos_fila):
        cocientes += [(votos / (j + 1), i) for j in range(num_escanos)]
    cocientes.sort(reverse=True)

    escaños = [0] * len(votos_fila)
    for _, i in cocientes[:num_escanos]:
        escaños[i] += 1

    umbral = cocientes[num_escanos - 1][0]

    for i, e in enumerate(escaños):
        if e < 2: continue
        cociente_actual = votos_fila[i] / e
        resto = votos_fila[i] - (e * umbral)
        if resto == 0: continue
        resto_pct = resto / umbral
        restos_dos_o_mas.append(resto_pct * 100)

# Ejecutar simulaciones
for _ in range(num_simulaciones):
    proporciones = np.random.dirichlet(alpha)
    votos_fila = np.random.multinomial(total_votos, proporciones)
    calcular_restos_dos_o_mas(votos_fila, num_escanos)

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.hist(restos_dos_o_mas, bins=100, color='mediumseagreen', edgecolor='k', density=True)
plt.title('Distribución de restos (% respecto al cociente de corte)\nSolo partidos que obtienen al menos 2 escaños')
plt.xlabel('Resto (%)')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.tight_layout()
plt.show()
