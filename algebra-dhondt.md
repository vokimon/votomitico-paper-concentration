# Marco algebraico para D'Hondt

Para facilitar el tratamiento algebraico del sistema D'Hondt
y superar las limitaciones analíticas de la visión procedural,
hemos propuesto una visión diferente de este método de reparto,
que permite relacionar los parámetros involucrados y
comprender las dinámicas entre ellos,
sin ejecutar el algoritmo.

El algoritmo de reparto consta de dos partes:
La **generación de cocientes**
y la posterior **selección ordenada**
de los coeficientes[^coeficientes_entrelazados].

[^coeficientes_entrelazados]:
    Separamos estas dos partes para facilitar la conceptualización,
    pero, el algoritmo en su versión típica las entrelaza
    para minimizar el número de operaciones a realizar.

    No se calcula un determinado cociente
    hasta que no se ha seleccionado el anterior de la misma candidatura,
    aprovechando que:

    $$
    { V_i \over j } > { V_i \over j + 1}
    $$

    Son optimizaciones que tenían mucho sentido
    cuando las divisiones se hacían a mano.
    Consideramos que esta versión, menos óptima pero más simple,
    deja más claro el propósito del algoritmo.

La **generación de cocientes** calcula,
para cada candidatura $i$, los cocientes:

$$
    C^j_i = {V_i \over j}
    \quad , \quad \forall{ j \in [1..E] } \quad \forall{ i \in [1..K] }
$$

Donde:

- $E$ es el número de escaños disponibles
- $K$ es el número de candidaturas
- $V_i$ son los votos que obtuvo la candidatura $i$

La **selección ordenada** ordena los coeficientes
y escoge, de mayor a menor, tantos como escaños disponibles $E$.
Una candidatura obtendrá tantos escaños
como cocientes derivados de sus votos se hayan escogido.

¿Qué significan estos coeficientes?
Pensemos el reparto como un intercambio de escaños por votos.
Estableceríamos un precio en votos por cada escaño.
Con esa perspectiva, se puede entender el coeficiente $V_i / j$
como el precio máximo con el cual
la candidatura $i$ podría conseguir $j$ escaños,
como ilustra la figura \ref{seat-costs}.


![Interpretando el significado de los coeficientes:
Con _Vi_ votos, si el precio fuera _Vi/3_,
la candidatura _i_ podria comprar 3 escaños.
Si el precio fuera algo superior,
no tendriá votos suficientes para un tercero
y se quedaría con 2.
](figures/seat-costs.pdf){#seat-costs}

Cuando seleccionamos estos coeficientes, de mayor a menor,
lo que estamos haciendo es bajar el precio de forma controlada,
permitiendo un escaño más con cada coeficiente,
hasta que todos los escaños disponibles se han repartido.
Podemos considerarlo como una **subasta a la baja**.

El último cociente escogido, fija **precio de corte** ($P_c$).
Este parámetro es clave
porque condensa el resultado del algoritmo en un solo valor.
Permite calcular, sin volver a ejecutar el algoritmo,
el resultado, es decir, los escaños de cada candidatura ($E_i$).

$$
Ei = \left\lfloor{ Vi \over Pc } \right\rfloor   \quad , \quad \forall{i}
$$

O expresado de otra manera:

$$ V_i = E_i \cdot P_c + R_i   \quad , \quad \forall{i} $$ 

![
Relación entre votos, escaños y restos tras aplicar el precio de corte.
_Vi = Ei  · Pc + Ri_](figures/seats-and-remainder.pdf){#seat-and-remainder}

Donde aparece un nuevo e importante parámetro interno:
los **restos** $Ri$,
que son los votos de la candidatura $i$ que podrían haber
ido a la abstención sin alterar el resultado.
Esto pone una distinción muy sólida de lo que significa voto útil o inútil.
Y tenemos que,
por construcción,
los restos de cada candidatura
están acotados por el precio de corte:

$$ 0 <= R_i < P_c    \quad , \quad \forall{i} $$


El **primer cociente no escogido**, $P_d$, también es especial,
cualquier precio $P$ tal que $P_c >= P > P_d$, conseguiría también un reparto exacto.
$P_d$ es por definición, el siguiente, cociente menor que $P_c$
mientras el precio no supere $P_d$, ningún otro cociente entrará en el reparto.


En resumen, manipular $P_c$ como una variable algebraica, sin concretar su valor,
nos abstrae del algoritmo y facilita el estudio,
aprovechando la relación que tiene con el resto de parámetros.

