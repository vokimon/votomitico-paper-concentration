from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from svgtools import parse_scenario

def compute_mean_reminder(candidatures):
    """
        Given that V = E P + Fi K
        where Fi is the mean remainde at price P,
        compute Fi por Pmin and Pmax
    """
    V = sum(p["votos"] for p in candidatures)
    E = sum(p["diputados"] for p in candidatures)
    K = len([p for p in candidatures if p["votos"] > 0])

    cocientes = list(sorted((
        p["votos"] / j
        for p in candidatures
        for j in range(1, E + 1)
    ), reverse=True))

    if len(cocientes) < E + 1: return

    Pmax = cocientes[E - 1]
    Pmin = cocientes[E]

    if K == 0: return
    if E == 0: return

    fmax = (V - Pmax * E) / (Pmax * K)
    fmin = (V - Pmin * E) / (Pmin * K)

    return E, fmax, fmin

directory = Path("data")

values_fmax = []
values_fmin = []
values_e = []

for filepath in directory.glob("*.tsv"):
    _, candidatures = parse_scenario(filepath)
    e, fmax, fmin = compute_mean_reminder(candidatures)
    values_fmax.append(fmax)
    values_fmin.append(fmin)
    values_e.append(e)

bin_width = 0.004
max_e = 21

bins = np.arange(0.0, 1.0 + bin_width, bin_width)
hist = np.zeros((max_e, len(bins) - 1))

for fpmax, fpmin, e in zip(values_fmax, values_fmin, values_e):
    # Obtener índices de bins que caen dentro del intervalo
    i_start = int(fpmax / bin_width)
    i_end = int(fpmin / bin_width)

    # Sumar +1 en todos los bins en el intervalo
    hist[min(e-1, max_e-1), i_start:i_end + 1] += 1

# Graficar
bin_centers = (bins[:-1] + bins[1:]) / 2

plt.figure(figsize=(10, 5))
colors = plt.cm.viridis(np.linspace(0, 1, max_e))  # Colores distintos para cada `e`

bottom = np.zeros(len(bins)-1)
for idx, (layer, color) in enumerate(zip(hist, colors)):
    if sum(layer) == 0: continue
    plt.bar(
        bin_centers,
        layer,
        bottom=bottom,
        width=bin_width,
        label=f'E = {idx + 1}' if idx < 20 else "E >= 20",
        #color=color,
        alpha=0.8,
    )
    bottom += layer

plt.xlabel("f en P = V / (E + fK)")
plt.ylabel("Frecuencia acumulada")
plt.title("Densidad acumulada de intervalos f válidos")
plt.legend(title='Escaños a repartir')
plt.grid(True)

plt.savefig("realdata-fhistogram.svg", format="svg")
plt.savefig("realdata-fhistogram.png", dpi=300)
plt.savefig("realdata-fhistogram.pdf", format="pdf")

plt.show()

