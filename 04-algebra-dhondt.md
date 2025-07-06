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
de los cocientes[^cocientes_entrelazados].

[^cocientes_entrelazados]:
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

La **selección ordenada** ordena los cocientes
y escoge, de mayor a menor, tantos como escaños disponibles $E$.
Una candidatura obtendrá tantos escaños
como cocientes derivados de sus votos se hayan escogido.

¿Qué significan estos cocientes?
Pensemos el reparto como un intercambio de escaños por votos.
Estableceríamos un precio en votos por cada escaño.
Con esa perspectiva, se puede entender el cociente $V_i / j$
como el precio máximo con el cual
la candidatura $i$ podría conseguir $j$ escaños,
como ilustra la figura \ref{seat-costs}.


![Interpretando el significado de los cocientes:
Con _Vi_ votos, si el precio fuera _Vi/3_,
la candidatura _i_ podria comprar 3 escaños.
Si el precio fuera algo superior,
no tendriá votos suficientes para un tercero
y se quedaría con 2.
](figures/seat-costs.pdf){#seat-costs}

Cuando seleccionamos estos cocientes, de mayor a menor,
lo que estamos haciendo es bajar el precio de forma controlada,
permitiendo un escaño más con cada cociente,
hasta que todos los escaños disponibles se han repartido.
Podemos considerarlo como una **subasta a la baja**.

El último cociente escogido, fija **precio de corte** ($P_{max}$).
Este parámetro es clave
porque condensa el resultado del algoritmo en un solo valor.
Permite calcular, sin volver a ejecutar el algoritmo,
el resultado, es decir, los escaños de cada candidatura ($E_i$).

$$
Ei = \left\lfloor{ Vi \over P_{max} } \right\rfloor   \quad , \quad \forall{i}
$$

O, expresado de otra manera:

$$ V_i = E_i \cdot P_{max} + R_i   \quad , \quad \forall{i} $$ 

![
Relación entre votos, escaños y restos tras aplicar el precio de corte.
_Vi = Ei  · Pmax + Ri_](figures/seats-and-remainder.pdf){#seat-and-remainder}

Donde aparece un nuevo e importante parámetro interno:
los **restos** $Ri$,
que son los votos de la candidatura $i$ que podrían haber
ido a la abstención sin alterar el resultado.
Esto pone una distinción muy sólida de lo que significa voto útil o inútil.
Y tenemos que,
por construcción,
los restos de cada candidatura
están acotados por el precio de corte:

$$ 0 <= R_i < P_{max}    \quad , \quad \forall{i} $$

Otro parámetro significativo es el **primer cociente no escogido**, $P_{min}$.
Por definición, es el siguiente cociente menor que $P_{max}$.
Eso quiere decir que cualquier precio $P$ tal que $P_{min} < P <= P_{max}$,
no incorporaría ningún escaño más al resultado,
y, por lo tanto, repartiría los mismos escaños que $P_{max}$.

De forma general, un reparto por $P$ es exacto si
Se reparten justo los escaños disponibles,
y nadie tiene restos para un escaño de más.
Formalmente:

$$
    E = \sum_i{E_i} \quad \and \quad 0 <= R_i < P \forall i
$$

El precio de corte $P_{max}$ es de estos, el mayor y el que asegura, además,
que haya al menos una candidatura sin restos.
Formalmente, sabemos que un precio exacto es tambien el de corte si:

$$
    \exists R_i  |  R_i = 0
$$


## Interpretación

A continuación, se detallan una serie de conclusiones,
que el formalismo anterior permite extraer,
en una primera mirada.

### Cotas y estimación para el precio del escaño

Las relaciones entre los parámetros también
nos permiten acotar y estimar el precio de corte,
lo que puede ser muy útil para el análisis.

Considerando la suma de votos a candidaturas,

$$
    V = \sum_i V_i = P E + \sum_i R_i
$$

Donde P es un precio de reparto exacto.

$$
    P = {V - \sum_i{R_i} \over E}
$$

Como $R_i$ está acotado, también lo está $P$:

$$
    {V \over E+K} < P <= {V \over E}
$$

Donde, recordemos, K es el número de candidaturas.

Si consideramos una esperanza para los restos,
podemos obtener una buena estimación del precio:

$$
\displaystyle \mathbb {E} [P_{max}] = {V \over E + K \mathbb{E}[R_i]}
$$

La figura \ref{fig:realdata-normalizedprice} muestra
la distribución de precios exactos posibles para
casos reales en elecciones para el Congreso Español.

![
Este histograma, obtenido de 832 casos reales,
52 circunscripciones en 16 convocatorias al congreso
de 1977 a 2024,
representa la frecuencia de cada precio,
expresado de forma relativa entre _V/(E+K)_ y _V/E_,
es un precio exacto para el resultado.
](figures/realdata-normalizedprice.pdf){#fig:realdata-normalizedprice}

Si visualizamos lo mismo pero respecto a la esperanza de los restos,
vemos que la esperanza de los restos estaria en algún lugar cercano a $0.2$.
Aún así depende de los escaños a repartir,
cuando hay pocos escaños, los restos son mayores.

![
En este histograma se representan los mismos casos,
pero en este caso el histograma es sobre f
en la fórmula _P = V / (E + f·K)_.
_f_ representaría la distribución media de los restos.
Se observa que la moda está cerca de 0.2.
](figures/realdata-fhistogram.pdf){#fig:realdata-fhistogram}


> TODO: Hacer esta estimación a partir de datos reales de diferentes convocatorias.

> TODO: Efectos del umbral fijo en los restos

> TODO: Cotas y estimaciones permiten descartar el efecto del umbral fijo
> Podemos descartar umbral del 3% si la suma de escaños y partidos supera 33.
> Podemos descartar umbral del 5% si la suma de escaños y partidos supera 50.

> TODO: Si el termino normal esta en el denominador,
> el precio una [distribución Gausiana inversa
> ](https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution)

### Teorema de la inutilidad de los restos

**Teorema:**
Dado un escenario inicial,
donde para una formación $i$,
$V_i = E_i P_{max} + R_i$,
obtendremos el mismo reparto de escaños,
si modificamos sus votos tal que 

$$
-R_i <= \Delta V_i < P_{max} - R_i
$$


**Demostración**

Para obtener el mismo resultado,
si expresamos los nuevos votos como,
$$
V_i' = E_i P_{max} + R_i'
$$

Se tendría que cumplir la restricción sobre los restos
que requiere un reparto exacto:
$$
0 <= R_i' < P_{max}
$$

Tenemos que:
$$
\Delta V_i = V_i' - V_i = R_i' - R_i \\
$$
$$
-R_i <= \Delta V_i = R_i' - R_i < P_{max} - R_i \\
$$
$$
0 <= R_i' < P_{max}  \quad q.e.d.
$$

**Observaciones**

Esto no quiere decir que $P_{max}$ siga siendo el precio de corte tras el trasvase.
Normalmente, sí lo será.
Dejará de serlo si la candidatura que modificamos
es la única que, originalmente, tuviera $R_i=0$.
En ese caso, la modificación que podemos hacer es añadir restos,
pero dejarían de ser cero, y no se cumpliría la condición
para que el antiguo $P_{max}$ siguiera siendo el precio de corte.
Seguiría siendo un precio de reparto exacto
pero no el de corte.

**Discusión:**

Una intuición que podemos extraer de aquí es que
los restos, o votos inútiles, funcionan de forma
muy parecida, en formaciones grandes y pequeñas.
Todas pueden acumilar hasta $P_{max}$ votos
sin que haya cambio en la representación.

Es importante tener en cuenta que
la operación de modificar los restos
tiene sentido para entender como se comporta el sistema
o para hacer análisis a posteriori.
A priori no conocemos el valor exacto de $R_i$,
de cada candidatura
para poder acotar como variamos los votos.

### Teorema de repetición de resultados {#teorema-repeticion-resultados}

**Teorema:**
Dado un escenario inicial de referencia,
en el cual $P$ es precio exacto,
trasvasar un número de votos igual a $P$ entre dos candidaturas,
emisora (A) y receptora (B),
resulta en un escenario donde $P$:

- sigue siendo precio exacto
- generando los mismos restos para todas las candidaturas,
- un escaño es trasvasado de A a B, manteniendo el resultado conjunto
- reparte los mismos escaños para el resto de candidaturas.

**Demostración:**

$$
V_a' = V_a - P = P E_a + R_a - P = P (E_a-1) + R_a \Rightarrow E_a' = E_a-1
$$
$$
V_b' = V_b + P = P E_b + R_b + P = P (E_b+1) + R_b \Rightarrow E_b' = E_b+1
$$

Al mantenerse los mismos restos y la suma de escaños,
$P$ sigue generando un reparto exacto.

**Observaciones:**

No es necesario que $P$ sea $P_{max}$,
solo basta que sea un _precio de reparto exacto_.

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

## Conclusiones

En resumen,
al abstraer el precio de corte $P_{max}$ como resultado del algoritmo
y establecer relaciones entre este valor y el resto de parámetros,
se pueden obtener conclusiones generales sobre la aplicación de D'Hondt
sin tener que ejecutar el algoritmo para cada caso.

Los votos a una candidatura se dividen
en votos que consiguen escaños y restos que no intervienen en el reparto.
Los restos de toda candidatura están limitados por el precio de corte.

También hemos detectado varios trasvases que
mantienen algunas condiciones del reparto.
Por ejemplo, modificar los votos afectando solo a los restos,
o trasvasar justo el precio del escaño.

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


