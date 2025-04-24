import numpy as np
import matplotlib.pyplot as plt

# Parámetros base
np.random.seed(42)
num_simulaciones = 100000
total_votos = 500_000
num_partidos = 6
num_escanos = 15  # Ahora usamos 20 escaños

# Distribución esperada de votos
media_porcentajes = np.array([0.30, 0.25, 0.15, 0.12, 0.10, 0.08])
media_porcentajes /= media_porcentajes.sum()
concentracion_total = 200
alpha = media_porcentajes * concentracion_total

# Nuevo umbral más inclusivo
umbral_minimo = 0.5 / num_escanos  # e.g. 0.025 = 2.5%

restos_grandes = []
restos_pequenos = []

def calcular_restos(votos_fila, proporciones, num_escanos):
    indices_validos = [i for i, p in enumerate(proporciones) if p >= umbral_minimo]
    if len(indices_validos) < 2:
        return

    votos_validos = [votos_fila[i] for i in indices_validos]
    cocientes = []
    for i, votos in enumerate(votos_validos):
        cocientes += [(votos / (j + 1), i) for j in range(num_escanos)]
    cocientes.sort(reverse=True)

    escaños = [0] * len(votos_validos)
    for _, i in cocientes[:num_escanos]:
        escaños[i] += 1

    umbral = cocientes[num_escanos - 1][0]
    proporciones_validas = [proporciones[i] for i in indices_validos]
    grandes_indices = np.argsort(proporciones_validas)[-3:]

    for i, e in enumerate(escaños):
        resto = votos_validos[i] - (e * umbral)
        if not resto: continue
        resto_pct = resto / umbral
        if i in grandes_indices:
            restos_grandes.append(resto_pct * 100)
        else:
            restos_pequenos.append(resto_pct * 100)

# Ejecutar simulaciones
for _ in range(num_simulaciones):
    proporciones = np.random.dirichlet(alpha)
    votos_fila = np.random.multinomial(total_votos, proporciones)
    calcular_restos(votos_fila, proporciones, num_escanos)

# Graficar resultados
plt.figure(figsize=(12, 6))
plt.hist(restos_grandes, bins=100, color='royalblue', alpha=0.6, label='Grandes (pasan umbral mínimo)', density=True)
plt.hist(restos_pequenos, bins=100, color='tomato', alpha=0.6, label='Pequeños (pasan umbral mínimo)', density=True)
plt.title(f'Distribución de restos (% respecto al cociente de corte)\n{num_escanos} escaños, umbral 0.5/escaños')
plt.xlabel('Resto (%)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de que esta función esté definida
def restos_a_angulos(restos_pct):
    theta = 2 * np.pi * ((np.array(restos_pct) + 100) / 200)
    return theta[(theta > 0) & (theta < 2 * np.pi)]

# Calcular el ángulo más frecuente (pico del histograma)
def calcular_pico(restos_pct):
    angulos = restos_a_angulos(restos_pct)
    hist, edges = np.histogram(angulos, bins=100, range=(0, 2 * np.pi))
    idx_max = np.argmax(hist)
    centro_bin = (edges[idx_max] + edges[idx_max + 1]) / 2
    return centro_bin

# Suponemos que tienes data_grandes_dict y data_pequenos_dict con los restos por número de escaños
escanos_range = list(range(5, 21))
picos_grandes = []
picos_pequenos = []

for n in escanos_range:
    if len(data_grandes_dict[n]) > 100:
        pico_g = calcular_pico(data_grandes_dict[n])
        picos_grandes.append((n, pico_g))
    if len(data_pequenos_dict[n]) > 100:
        pico_p = calcular_pico(data_pequenos_dict[n])
        picos_pequenos.append((n, pico_p))

df_picos_grandes = pd.DataFrame(picos_grandes, columns=["escaños", "pico_angular"])
df_picos_pequenos = pd.DataFrame(picos_pequenos, columns=["escaños", "pico_angular"])

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(df_picos_grandes["escaños"], df_picos_grandes["pico_angular"], marker='o', label="Grandes", color="royalblue")
plt.plot(df_picos_pequenos["escaños"], df_picos_pequenos["pico_angular"], marker='s', label="Pequeños", color="tomato")
plt.xlabel("Número de escaños")
plt.ylabel("Ángulo del pico (radianes)")
plt.title("Evolución de la posición del pico en la distribución de restos")
plt.ylim(0, 2 * np.pi)
plt.yticks(np.linspace(0, 2*np.pi, 5), labels=["0", "π/2", "π", "3π/2", "2π"])
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
