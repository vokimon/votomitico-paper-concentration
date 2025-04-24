import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros base
np.random.seed(42)
num_simulaciones = 100_000
total_votos = 500_000
num_partidos = 6
concentracion_total = 200
media_porcentajes = np.array([0.30, 0.25, 0.15, 0.12, 0.10, 0.08])
media_porcentajes /= media_porcentajes.sum()
alpha = media_porcentajes * concentracion_total

# Rango de escaños para animación
escanos_range = list(range(5, 21))
bins = np.linspace(-100, 100, 100)

# Almacenamiento por número de escaños
data_grandes = []
data_pequenos = []

for num_escanos in escanos_range:
    umbral_minimo = 0.5 / num_escanos

    restos_grandes = []
    restos_pequenos = []

    for _ in range(num_simulaciones):
        proporciones = np.random.dirichlet(alpha)
        votos_fila = np.random.multinomial(total_votos, proporciones)

        cocientes = []
        for i, votos in enumerate(votos_fila):
            cocientes += [(votos / (j + 1), i) for j in range(num_escanos)]
        cocientes.sort(reverse=True)

        escaños = [0] * len(votos_fila)
        for _, i in cocientes[:num_escanos]:
            escaños[i] += 1

        umbral = cocientes[num_escanos - 1][0]

        indices_validos = [i for i, p in enumerate(proporciones) if p >= umbral_minimo]
        proporciones_validas = [proporciones[i] for i in indices_validos]
        grandes_indices = np.argsort(proporciones_validas)[-3:] if len(proporciones_validas) >= 3 else []

        for i in indices_validos:
            idx_local = indices_validos.index(i)
            if escaños[i] > 0:
                resto = votos_fila[i] - (escaños[i] * umbral)
                resto_pct = resto / umbral
                if np.isclose(resto_pct, 0, atol=1e-6):
                    continue
                if idx_local in grandes_indices:
                    restos_grandes.append(resto_pct * 100)
                else:
                    restos_pequenos.append(resto_pct * 100)

    data_grandes.append(restos_grandes)
    data_pequenos.append(restos_pequenos)

# Crear animación
fig, ax = plt.subplots(figsize=(10, 5))

def update(frame):
    ax.clear()
    ax.hist(data_grandes[frame], bins=bins, alpha=0.6, color='royalblue', label='Grandes', density=True)
    ax.hist(data_pequenos[frame], bins=bins, alpha=0.6, color='tomato', label='Pequeños', density=True)
    ax.set_xlim(-100, 100)
    ax.set_ylim(0, 0.035)
    ax.set_xlabel('Resto (% respecto al cociente de corte)')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_title(f'Distribución de restos – {escanos_range[frame]} escaños')
    ax.legend()

ani = animation.FuncAnimation(fig, update, frames=len(escanos_range), repeat=False)

plt.show()
# Para mostrar en Jupyter/Colab
#from IPython.display import HTML
#HTML(ani.to_jshtml())
