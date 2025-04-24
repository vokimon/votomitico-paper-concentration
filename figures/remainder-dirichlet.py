import numpy as np
import matplotlib.pyplot as plt

# Simulación Monte Carlo con Dirichlet-Multinomial
np.random.seed(42)
num_simulaciones = 100000

# Parámetros
total_votos = 500_000
num_partidos = 6
num_escanos = 10

# Porcentajes medios de voto (base esperada)
media_porcentajes = np.array([0.30, 0.25, 0.15, 0.12, 0.10, 0.08])
media_porcentajes /= media_porcentajes.sum()

# Parámetro de concentración para la Dirichlet
# Cuanto menor sea, más dispersión (más variación entre simulaciones)
concentracion_total = 200  # puedes probar con 50 para más volatilidad
alpha = media_porcentajes * concentracion_total

# Función para calcular los restos para formaciones con escaño
def calcular_restos_y_cocientes(votos_fila, num_escanos):
    cocientes = []
    for i, votos in enumerate(votos_fila):
        cocientes += [(votos / (j + 1), i) for j in range(num_escanos)]

    cocientes.sort(reverse=True)
    escaños = [0] * len(votos_fila)
    for _, i in cocientes[:num_escanos]:
        escaños[i] += 1

    umbral = cocientes[num_escanos - 1][0]  # último cociente que entra

    restos_pct = []
    for i, e in enumerate(escaños):
        if e > 0:
            cociente_actual = votos_fila[i] / e
            resto = votos_fila[i] - (e * umbral)
            resto_pct = resto / umbral
            restos_pct.append(resto_pct)
    return restos_pct

# Ejecutar simulaciones
restos_percentuales = []
for _ in range(num_simulaciones):
    proporciones = np.random.dirichlet(alpha)
    votos_fila = np.random.multinomial(total_votos, proporciones)
    restos = calcular_restos_y_cocientes(votos_fila, num_escanos)
    restos_percentuales.extend(restos)

# Convertir a porcentaje
restos_percentuales = np.array(restos_percentuales) * 100

# Graficar la distribución
plt.figure(figsize=(10, 6))
plt.hist(restos_percentuales, bins=100, color='skyblue', edgecolor='k', density=True)
plt.title('Distribución de porcentajes de resto sobre el cociente de corte\n(para candidaturas con escaño, con voto variable)')
plt.xlabel('Resto (%) respecto al cociente de corte')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Suponiendo que 'restos_percentuales' ya ha sido generado como en simulaciones anteriores

# Filtrar restos para eliminar el bin de 0
restos_no_cero = restos_percentuales[restos_percentuales != 0]

# Calcular estadísticas
media_restos = np.mean(restos_no_cero)
mediana_restos = np.median(restos_no_cero)
asimetria_restos = (np.mean(restos_no_cero**3)) / (np.std(restos_no_cero)**3)

# Graficar sin el bin de 0
plt.figure(figsize=(10, 6))
plt.hist(restos_no_cero, bins=100, color='skyblue', edgecolor='k', density=True)
plt.title('Distribución de porcentajes de resto sobre el cociente de corte\n(para candidaturas con escaño, excluyendo resto 0)')
plt.xlabel('Resto (%) respecto al cociente de corte')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.tight_layout()
plt.show()

# Mostrar estadísticas
print(f"Media de restos: {media_restos}")
print(f"Mediana de restos: {mediana_restos}")
print(f"Asimetría de los restos: {asimetria_restos}")
