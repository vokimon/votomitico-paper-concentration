import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuración
np.random.seed(42)
num_simulaciones = 100_000
total_votos = 500_000
num_partidos = 6
concentracion_total = 200
escanos_range = list(range(5, 21))
bins = np.linspace(-100, 100, 100)

# Distribución esperada de voto
media_porcentajes = np.array([0.30, 0.25, 0.15, 0.12, 0.10, 0.08])
media_porcentajes /= media_porcentajes.sum()
alpha = media_porcentajes * concentracion_total

# Almacenamiento
data_grandes_dict = {n: [] for n in escanos_range}
data_pequenos_dict = {n: [] for n in escanos_range}

# Simulaciones base: se usan para todos los tamaños de escaños
for _ in range(num_simulaciones):
    proporciones = np.random.dirichlet(alpha)
    votos_fila = np.random.multinomial(total_votos, proporciones)

    for num_escanos in escanos_range:
        umbral_minimo = 0.5 / num_escanos

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
                    data_grandes_dict[num_escanos].append(resto_pct * 100)
                else:
                    data_pequenos_dict[num_escanos].append(resto_pct * 100)

# Crear animación
fig, ax = plt.subplots(figsize=(10, 5))

def update(frame):
    e = escanos_range[frame]
    ax.clear()
    ax.hist(data_grandes_dict[e], bins=bins, alpha=0.6, color='royalblue', label='Grandes', density=True)
    ax.hist(data_pequenos_dict[e], bins=bins, alpha=0.6, color='tomato', label='Pequeños', density=True)
    ax.set_xlim(-100, 100)
    ax.set_ylim(0, 0.035)
    ax.set_xlabel('Resto (% respecto al cociente de corte)')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_title(f'Distribución de restos – {e} escaños')
    ax.legend()

ani = animation.FuncAnimation(fig, update, frames=len(escanos_range), repeat=False)

ani.save("lala.webp")
plt.show()


from scipy.stats import beta
from scipy.optimize import minimize
import numpy as np
import pandas as pd

# Suponemos que data_grandes_dict ya contiene los restos por número de escaños
# y que escanos_range = list(range(5, 21))

# Función para ajustar distribución Beta a una muestra (reescalada a [0, 1])
def ajustar_beta(restos_pct):
    data = (np.array(restos_pct) + 100) / 200  # escalar de [-100, 100] a [0, 1]
    data = data[(data > 0) & (data < 1)]       # eliminar extremos exactos
    
    def loss(params):
        a, b = params
        if a <= 0 or b <= 0:
            return np.inf
        return -np.sum(beta.logpdf(data, a, b))  # log-verosimilitud negativa

    result = minimize(loss, x0=[2, 2], bounds=[(0.1, None), (0.1, None)])
    if result.success:
        return result.x
    else:
        return None, None

# Ajuste por número de escaños
ajustes_beta = []

for n in range(5, 21):
    restos_n = data_grandes_dict[n]
    if len(restos_n) > 100:
        a, b = ajustar_beta(restos_n)
        if a is not None:
            ajustes_beta.append((n, a, b))

# Guardar en DataFrame
df_beta = pd.DataFrame(ajustes_beta, columns=["escaños", "alpha", "beta"])
df_beta

