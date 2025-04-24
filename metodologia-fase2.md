
### Fase 2: Desarrollo de un modelo simplificado

### Objetivo

El objetivo de esta fase es desarrollar un modelo matemático  
que permita explicar las observaciones empíricas de la fase 1.  
A partir del modelo, se extraerán conclusiones sobre qué predicciones  
se pueden hacer sobre el efecto de un trasvase entre dos partidos  
en el resultado conjunto de ambos.

### Procedimiento

1. **Establecimiento de un marco algebraico para D'Hondt**
    Para superar las limitaciones de la perspectiva procedural de D'Hondt,
    se propuso un marco algebràico,
    con el _precio de corte_ como parámetro clave.
    El _precio de corte_ condensa en un único valor el resultado del algoritmo,
    permitiendo derivar los valores de salida,
    a partir de las entradas con una relación algebraica simple.
    
    En este primer modelo,
    también se consideró que el _precio de corte_ no cambiaba
    como resultado de un trasvase entre dos candidaturas.
    Esta suposición no es cierta pero simplificó el modelo
    suficiente como para facilitar su abordaje.


2. **Cálculo probabilístico de los cambios en la representación** 

    Se identificó el parámetro relevante en el modelo
    que determina cuando se produce un cambio de representación de una candidatura.
    Dada la incertidumbre a priori sobre el valor de este parámetro
    en una situación inicial de referencia arbitraria,
    se planteó un modelo probabilístico.
    Este modelo permitió estimar la probabilidad de un cambio en los escaños,
    cuando se alteran los votos a la candidatura en una cantidad determinada.

3. **Probabilidad combinada de emisor y receptor**
    Se planteó un escenario de trasvase,
    en el que los cambios de votos en el emisor y receptor
    se realizaban a la vez, pero con signo inverso.
    Es decir, si uno ganaba escaños, el otro los perdía en la misma proporción.
    Se combinaron las probabilidades
    de ganancia y pérdida de escaños para cada candidatura,
    con el objetivo de calcular la probabilidad de que se produzca un cierto cambio en signo y magnitud
    en la representación conjunta de ambas candidaturas.

4. **Contraste del modelo y las observaciones empíricas**
    Finalmente, se analizó el impacto de un trasvase progresivo de votos en el modelo,
    para comprobar si el cambio en los resultados del reparto
    coincidía con las observaciones empíricas obtenidas del simulador.


### Marco algebraico para D'Hondt

Para facilitar el tratamiento algebraico del sistema D'Hondt
y superar las limitaciones analíticas de la vision procedural,
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

### Tipos de análisis


### Observaciones preliminares

Según la perspectiva de que en el recuento
los votos se dividen en votos transformados y restos,
podemos observar los siguientes invariantes:

- El resultado de una situación inicial dada no cambiará si
    - si eliminamos total o parcialmente restos.
    - o si añadimos restos sin llegar al precio de corte
- En ambos casos el reparto y el precio de corte seguirá siendo el mismo.

- El precio de corte y los restos se mantendrán si
    - transferimos tantos votos como el precio de corte entre candidaturas
    - tambien se mantendrá la suma de escaños entre las candidaturas 

También se observa intuitivamente que restos de varios partidos
podrían agregarse para llegar a un escaño extra.
Esto es evidente en un análisis a posteriori,
lo cual refuerza un cierto sesgo cognitivo,
pero también es verdad que si trasvasamos más de la cuenta
podría pasar que la candidatura emisora no llegue a sumar su último escaño.
Y, a priori no conocemos los restos que puede transferir sin tener perdidas.


### Transferencia entre una candidatura y la abstención

Como paso intermedio a entender la transferencia de votos entre candidaturas,
en este apartado, abordamos un caso más sencillo:
trasferencia entre una candidatura y la abstención.
Esto es, que, respecto a un escenario de referencia,
solo cambian los votos de la candidatura bajo estudio,
en positivo o en negativo,
pero se mantienen los del resto de candidaturas.

Primero vamos a evaluar un caso de **caja blanca**,
en el que miramos cuál es el efecto
dependiendo de la situación inicial
y la cantidad concreta de votos que se mueven.

Despues pasaremos a un análisis de **caja gris**,
en el que la situación inicial en el que partimos de una situación incierta,
con un cierto 

El análisis de caja gris equivaldría al que haríamos ante los datos de una encuesta
para decidir un voto estratégico.
Mientras que el análisis de caja blanca equivaldría al que haríamos a posteriori,
postelectoralmente.



El objetivo final sería evaluar la transferencia de votos entre candidaturas,
pero en un primer nivel transferencias contra la abstención.
Eso implica que solo la candidatura considerada modifica sus votos,
manteniendo el resto de candidaturas los suyos.

Haremos también la suposición para toda la fase 2,
de que el trasvase de votos que vamos a simular
no implica cambios en el precio, 
es decir, supondremos que el precio de corte no se ve alterado con el cambio.
Sabemos que eso no es cierto, por lo que hemos observado empíricamente.


- Modelo de caja blanca:
    - Sirve para entender como funciona pero también como análisi  a posterior
    - Sabemos cual es la situación actual
    - Considerar si un 
    - Si un trasvase de votos 

- Para evaluar el efecto de un cambio
    - Evaluamos 
    - Suponer una situacion desconocida pero concreta
    - Proponer un cambio
    - 
- Partimos de una situación concreta



### Probabilidad de cambios en la representación

Dada una situación inicial de referencia desconocida,
planteemos que cambiamos los votos de una candidatura en N votos.
¿Qué cambios son posibles y con qué probabilidades se pueden
producir en su repesentación en escaños?

Si no conocemos la representación de una candidatura o incluso si la conocemos con una cierta incerteza siguiendo una distribución normal,
podemos decir por el Theorema de 




#### Desarrollo del Modelo de Probabilidades

Una vez establecido el **precio de corte** ($$ P_c $$),
analizamos cómo los trasvases de votos entre partidos afectarían la distribución de escaños.
Para hacerlo, representamos cada posible situación de los restos de los partidos \( A \) y \( B \)
en un **cuadro de probabilidades**.
En este cuadro, cada punto dentro del cuadro representaba una combinación de los restos de \( A \) y \( B \)
al inicio del proceso, con los valores de los restos dentro del rango \( [0, P_c) \).

Este enfoque generaba un **espacio bidimensional** en el que las combinaciones de restos de los partidos se representaban gráficamente. 

El punto de partida de cada trasvase en el cuadro estaba determinado por los restos de \( A \) y \( B \), y el trasvase de votos a través de este cuadro se describía mediante un movimiento diagonal. A medida que los votos se transferían, el punto dentro del cuadro se desplazaba, y dependiendo de la zona en la que se moviera, se producían diferentes resultados:

- Si el punto alcanzaba uno de los bordes del cuadro, implicaba que uno de los partidos ganaba o perdía un escaño.
- Debido a la geometría **toroidal** de los restos (es decir, que los bordes del cuadro se conectan entre sí),
el punto que llegaba a un borde aparecía en el lado opuesto del cuadro, permitiendo que el proceso de trasvase continuara cíclicamente.

Este movimiento en el cuadro reflejaba cómo, dependiendo de la zona por la que transitara, los escaños de las candidaturas se verían afectados, siguiendo los patrones observados empíricamente.

#### Ciclicidad y Patrones de Cambio

El análisis del cuadro de probabilidades reveló dos tipos de patrones de escaños observados empíricamente en los trasvases de votos:

1. **Patrón con cambio de escaños:**
   - En este patrón, las transferencias de votos provocaban que un partido ganara un escaño a medida que el otro partido perdía.
   - Este patrón se repetía cíclicamente a medida que el punto se desplazaba por el cuadro.

2. **Patrón sin cambio de escaños:**
   - En este patrón, aunque los votos se trasladaban entre los partidos, no se observaba ningún cambio neto en el número de escaños de los partidos.
   - Este patrón también se repetía cíclicamente, y el cambio solo se manifestaba como una redistribución de los votos entre los partidos sin que uno ganara o perdiera escaños.

Ambos patrones se generaban a partir de la interacción de los restos de los partidos con los límites del cuadro de probabilidades, donde los bordes del cuadro determinaban el cambio de escaños. Estos resultados coincidían con las observaciones empíricas y nos permitieron hacer predicciones basadas en la zona en la que se encontrara el punto inicial y cómo éste interactuaba con los bordes del cuadro.


¡Por supuesto! A partir de ahora te paso las propuestas de fragmentos en el formato **Markdown** adecuado y estructurado como lo hemos comentado. 

Te paso ahora la **propuesta para la Fase 2** en ese formato, como dijiste que estábamos en borrador. Aquí tienes:

