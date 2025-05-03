# Marco algebraico para D'Hondt {#sec:modelo-algebraico}

## Objetivo

El objetivo de esta fase es
proporcionar una formulación algebraica del sistema D'Hondt
que facilite su análisis,
superando las limitaciones analíticas de la visión procedural.
Para ello, se propone una perspectiva diferente de este método de reparto,
que permite relacionar los parámetros involucrados y
comprender las dinámicas entre ellos,
sin ejecutar el algoritmo.

## Derivación algebraica

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
    Consideramos que esta versión, menos óptima,
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

O, expresado de otra manera:

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

Otro parámetro significativo es el **primer cociente no escogido**, $P_d$.
Por definición, es el siguiente cociente menor que $P_c$.
Eso quiere decir que cualquier precio $P$ tal que $P_d < P <= P_c$,
no incorporaría ningún escaño más al resultado,
y, por lo tanto, repartiría los mismos escaños que $P_c$.

De forma general, un reparto por $P$ es exacto si
Se reparten justo los escaños disponibles,
y nadie tiene restos para un escaño de más.
Formalmente:

$$
    E = \sum_i{E_i} \quad \and \quad 0 <= R_i < P \forall i
$$

El precio de corte $P_c$ es de estos, el mayor y el que asegura, además,
que haya al menos una candidatura sin restos.
Formalmente, sabemos que un precio exacto es tambien el de corte si:

$$
    \exists R_i  |  R_i = 0
$$


## Interpretación

A continuación, se detallan una serie de conclusiones,
que el formalismo anterior permite extraer,
en una primera mirada.

### Teorema de la inutilidad de los restos

**Teorema:**
Dado un escenario inicial,
donde para una formación $i$,
$V_i = E_i P_c + R_i$,
obtendremos el mismo reparto de escaños,
si modificamos sus votos tal que 

$$
-R_i <= \Delta V_i < P_c - R_i
$$


**Demostración**

Para obtener el mismo resultado,
si expresamos los nuevos votos como,
$$
V_i' = E_i P_c + R_i'
$$

Se tendría que cumplir la restricción sobre los restos
que requiere un reparto exacto:
$$
0 <= R_i' < P_c
$$

Tenemos que:
$$
\Delta V_i = V_i' - V_i = R_i' - R_i \\
$$
$$
-R_i <= \Delta V_i = R_i' - R_i < P_c - R_i \\
$$
$$
0 <= R_i' < P_c  \quad q.e.d.
$$

**Observaciones**

Esto no quiere decir que $P_c$ siga siendo el precio de corte.
Normalmente, sí lo será,
pero si añadimos restos a la candidatura que marca el precio de corte,
y por tanto $R_i=0$,
la condición para ser precio de corte dejará de ser cierta,
y simplemente $P_c$ será ahora un precio de reparto exacto.

**Discusión:**

Una intuición que podemos extraer de aquí es que
los restos, o votos inútiles, funcionan de forma
muy parecida, en formaciones grandes y pequeñas.
Todas pueden acomular hasta $P_c$ votos
sin que haya cambio en la respresentación.

Es importante tener en cuenta que
la operación de modificar los restos
tiene sentido para entender como se comporta el sistema
o para hacer análisis a posteriori,
puesto que a priori no conocemos el valor exacto de $R_i$,
para poder acotar como variamos los votos.

### Teorema de repetición de resultados

**Teorema:**
Dado un escenario inicial de referencia,
con un precio de corte $P_c$,
trasvasar un número de votos igual a $P_c$ entre dos candidaturas,
emisora (A) y receptora (B),
resulta en un escenario con:

- el mismo precio de corte,
- los mismos restos para todas las candidaturas,
- un escaño trasvasado de A a B, manteniendo el resultado conjunto
- los mismos escaños para el resto de candidaturas.

**Demostración:**

$$
V_a' = V_a - P_c = P_c E_a + R_a - P_c = P_c (E_a-1) + R_a \Rightarrow E_a' = E_a-1
$$
$$
V_b' = V_b + P_c = P_c E_b + R_b + P_c = P_c (E_b+1) + R_b \Rightarrow E_b' = E_b+1
$$

Al mantenerse los mismos restos y la suma de escaños,
$P_c$ sigue generando un reparto exacto.

**Colorario 1:**

Podemos aplicar la regla tantas veces como escaños tenga el emisor.

**Colorario 2:**

Si al concentrar el voto, obtenemos un resultado conjunto bueno,
podemos conseguir el mismo resultado en un escenario menos concentrado,
traspasando el precio al menor.
Es decir, no hay resultados mejores en situaciones con concentración
de votos que en situaciones de concentración baja.

Esto no descarta que las situaciones buenas sean más probables en concentración alta.
Pero si descarta que haya resultados que no se puedan conseguir con menos concentracion.

### Observación: Posibilidad de mejora sumando restos, con peros

Analizando un resultado concreto, es común observar que
si juntamos los restos de dos candidaturas,
se podría obtener un escaño adicional.
Eso es cierto, y sugiere que una redistribución
de los votos podría mejorar
el resultado conjunto.

Pero sería un sesgo retrospectivo
pensar que esta observacion se puede aplicar
más allá de un analisis a posteriori.
Si no conocemos la situación de partida,
no conocemos los restos disponibles.
Si se trasvasan menos votos,
que los que le faltan a los restos del receptor
para sumar un escaño, se podría no ganar el escaño adicional.
Si se trasvasan más votos
que los restos que dispone el emisor,
podría perder uno de los escaños de los que dispone.

### Cotas y estimación para el precio del escaño

Las relaciones entre los parámetros también
nos permiten acotar y estimar el precio de corte,
lo que puede ser muy útil para el análisis.

Considerando la suma de votos a candidaturas:

$$
    V = \sum_i V_i = P_c E + \sum_i R_i
$$

$$
    P_c = {V - \sum_i{R_i} \over E}
$$

Como $R_i$ está acotado, también lo está $P_c$:

$$
    {V \over E+K} < P_c <= {V \over E}
$$

Donde, recordemos, K es el número de candidaturas.

Si consideramos una esperanza para los restos,
podemos obtener una buena estimación del precio:

$$
\displaystyle \mathbb {E} [P_c] = {V \over E + K \mathbb{E}[R_i]}
$$

> TODO: Hacer esta estimación a partir de datos reales de diferentes convocatorias.

> TODO: Efectos del umbral fijo en los restos

> TODO: Cotas y estimaciones permiten descartar el efecto del umbral fijo
> Podemos descartar umbral del 3% si la suma de escaños y partidos supera 33.
> Podemos descartar umbral del 5% si la suma de escaños y partidos supera 50.

> TODO: Si el termino normal esta en el denominador,
> el precio una [distribución Gausiana inversa
> ](https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution)

## Conclusiones

En resumen,
al abstraer el precio de corte $P_c$ como resultado del algoritmo
y establecer relaciones entre este valor y el resto de parámetros,
se pueden obtener conclusiones generales sobre la aplicación de D'Hondt
sin tener que ejecutar el algoritmo para cada caso.

Los votos a una candidatura se dividen
en votos que consiguen escaños y restos que no intervienen en el reparto.
Los restos de toda candidatura estan limitados por el precio de corte.

También hemos detectado varios trasvases que
mantienen algunas condiciones del reparto.
Por ejemplo, reducir para una candidatura
tantos votos como restos tiene o
trasvasar entre dos candidaturas
tantos votos como el precio de corte.

Los efectos de este ultimo tipo de trasvase, además,
demuestran que, por concentración de voto,
no vamos a obtener un resultado conjunto
que no sea posible obtener con menos concentración.
Esto no nos permite descartar, sin embargo, que,
cuando hay más concentración, los resultados
mejores sean más probables que cuando no la hay.

Por eso debemos establecer un modelo probabilistico,
que considere la probabilidad de estar en cada escenario de partida,
y vincule esa probabilidad a los escenarios de destino,
según su bondad para el resultado conjunto.
Esto es lo que abordamos en la siguiente fase.


