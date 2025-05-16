from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

def parse_tsv(filepath):
    candidatures = []
    especiales = {}
    print(f"=== Processing {filepath}")
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split('\t')
            if parts[0].lower() == "siglas":
                continue  # saltar cabecera
            key = parts[0]
            if key.lower() in ["censo", "participacion", "abstencion", "nulos", "blancos"]:
                especiales[key.lower()] = int(parts[1])
                continue
            votos = int(parts[1])
            diputados = int(parts[2]) if len(parts) > 2 else 0
            nombre = parts[3] if len(parts) > 3 else ""
            candidatures.append({
                "siglas": key,
                "votos": votos,
                "diputados": diputados,
                "nombre": nombre
            })
    return especiales, candidatures

def calcular_precios_y_f(candidatures):
    V = sum(p["votos"] for p in candidatures)
    E = sum(p["diputados"] for p in candidatures)
    K = len([p for p in candidatures if p["votos"] > 0])

    cocientes = []
    for p in candidatures:
        for j in range(1, E + 1):
            cocientes.append(p["votos"] / j)

    cocientes.sort(reverse=True)

    if len(cocientes) < E + 1: return
    if K == 0: return
    if E == 0: return

    Pmax = cocientes[E - 1]
    Pmin = cocientes[E]
    fmax = (V - Pmax * E) / (Pmax * K)
    fmin = (V - Pmin * E) / (Pmin * K)

    return E, fmax, fmin

directory = Path("data")

values_fmax = []
values_fmin = []

for filepath in directory.glob("*.tsv"):
    _, candidatures = parse_tsv(filepath)
    e, fmax, fmin = calcular_precios_y_f(candidatures)
    values_fmax.append(fmax)
    values_fmin.append(fmin)

bin_width = 0.004

bins = np.arange(0.0, 1.0 + bin_width, bin_width)
hist = np.zeros(len(bins) - 1)

for fpmax, fpmin in zip(values_fmax, values_fmin):
    # Obtener índices de bins que caen dentro del intervalo
    i_start = int(fpmax / bin_width)
    i_end = int(fpmin / bin_width)

    # Sumar +1 en todos los bins en el intervalo
    hist[i_start:i_end + 1] += 1

# Graficar
bin_centers = (bins[:-1] + bins[1:]) / 2
plt.figure(figsize=(10, 5))
plt.bar(bin_centers, hist, width=bin_width, color="steelblue", alpha=0.7)
plt.xlabel("f en P = V / (E + fK)")
plt.ylabel("Frecuencia acumulada")
plt.title("Densidad acumulada de intervalos f válidos")
plt.grid(True)

plt.savefig("realdata-fhistogram.svg", format="svg")
plt.savefig("realdata-fhistogram.png", dpi=300)
plt.savefig("realdata-fhistogram.pdf", format="pdf")

plt.show()
