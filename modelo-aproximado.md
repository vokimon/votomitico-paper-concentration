
# Análisis con un modelo simplificado

## Objetivo

El objetivo de esta fase es desarrollar un modelo matemático  
que permita explicar las observaciones empíricas de la fase 1.  
A partir del modelo, se extraerán conclusiones sobre qué predicciones  
se pueden hacer sobre el efecto de un trasvase entre dos partidos  
en el resultado conjunto de ambos.

## Procedimiento

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


También se observa intuitivamente que restos de varios partidos
podrían agregarse para llegar a un escaño extra.
Esto es evidente en un análisis a posteriori,
lo cual refuerza un cierto sesgo cognitivo,
pero también es verdad que si trasvasamos más de la cuenta
podría pasar que la candidatura emisora no llegue a sumar su último escaño.
Y, a priori no conocemos los restos que puede transferir sin tener perdidas.


## Transferencia entre una candidatura y la abstención

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



## Probabilidad de cambios en la representación

Dada una situación inicial de referencia desconocida,
planteemos que cambiamos los votos de una candidatura en N votos.
¿Qué cambios son posibles y con qué probabilidades se pueden
producir en su repesentación en escaños?

Si no conocemos la representación de una candidatura o incluso si la conocemos con una cierta incerteza siguiendo una distribución normal,
podemos decir por el Theorema de 




### Desarrollo del Modelo de Probabilidades

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

### Ciclicidad y Patrones de Cambio

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

