
# Análisis con un modelo simplificado

## Objetivo

El objetivo de esta fase es desarrollar un modelo
que permita explicar las observaciones empíricas de la fase 1,
y hacer predicciones generales de como se altera resultado conjunto
despues de un trasvase de votos entre dos candidaturas.

Para simplificar la obtención de este modelo,
vamos a suponer que los trasvases de voto no alteran el precio de corte.
Esto nos permite abstraernos de las redes complejas de dependencias
entre los votos de las distintas candidaturas y sus resultados.

En la fase anterior, vimos que, en muchos trasvases, el precio de corte se mantiene:
cuando traspasamos tantos votos como el precio de corte,
o cuando traspasamos restos sin que estos superen el precio de corte
en la candidatura destino.
En cambio, en los casos empíricos se constata que,
en ciertos tramos entre escaño y escaño transferido,
el precio de corte oscila entre dos precios, normalmente, cercanos.

Más tarde, se evaluarán los casos en que esta suposición no se da
y los efectos que puede tener en los resultados obtenidos.

## Análisis de caja blanca

Según el método de variación controlada se plantea:
¿Cuál es el efecto de añadir o quitar N votos a una candidatura?

Dividiremos el trasvase en dos trasvases,
uno que trasvasa la parte divisible por $P_c$,
y otro que trasvasa la parte fraccional.

Por el teorema de resultados repetidos,
cada $P_c$ votos trasvasados de A a B,
se traspasa un escaño, y tanto los restos como el precio de corte se mantienen.
Esto resuelve la parte divisible por $P_c$.

Quedaría por saber qué pasa con un trasvase de una fracción del precio de escaño
$0 <= N < P_c$.
Para eso, la clave es en qué parte de los restos se encuentra
cada candidatura en el escenario inicial.
La candidatura receptora, conseguira un escaño más
si sus restos estan a N o menos de sumar $P_c$.
Al mismo tiempo, la candidatura emisora, perderá un escaño
si tiene menos de N votos de restos.

Este tipo de análisis lo podemos observar a posteriori,
pero, en un análisis preelectoral no podemos saber, solo estimar,
cuáles son los restos de cada formación.
Para eso, es necesario realizar un análisis probabilístico.

## Ditribución probabilística de los restos

La mejor información de la que disponemos sobre un resultado electoral
que aún no se ha producido son las encuestas preelectorales [@alaminos2023metodos].
Las encuesta modelan el voto a cada candidatura como una distribución normal.





**OUTLINE**

- Suposición de precio fijo
    - Las candidaturas van completando sus escaños
    - En la situacion inicial quedan a un número de restos
    - Un in/exflujo de escaños implica movimiento en el resultado por contraste
- Caja blanca
    - A precio fijo si cubrimos lo que falta para el escaño lo obtenemos
        - en realidad, para quitarle el escaño tendriamos que subirle el precio
    - A precio fijo si perdemos los restos perdemos un escaño.
        - en realidad, estaríamos bajando el precio, hasta que otro cociente entre y se lleve el escaño
    - Cuando un trasvase de N gana el escaño: cuando me faltan N o menos
    - Cuando un trasvase de N pierde el escaño: cuando tengo N restos o menos
- Caja gris
    - Probabilidad que mis restos valgan x? Queremos una distribución
    - Estimaciones electorales como una normal
    - Del voto a los restos con un modulo
    - Normal doblada -> Uniforme
    - Simil de la ruleta
        - Vueltas -> Escaños, Numero -> Restos, Fuerza -> Encuestas
        - Incerteza proporcional a la fuerza
        - Con poca fuerza es más probable acertar
    - Probabilidad perdiendo N votos, perder un escaño
    - Probabilidad ganando N votos, ganar un escaño
    - Probabilidad cruzada entre emisor y receptor
    - La mitad de la zona es de no cambio
    - Las zonas de perdida son iguales
- Emulación de los resultados empíricos
    - Escenario inicial como punto en el cuadro de restos combinados
    - Trasvase como movimiento diagonal +-(+N,-N)
    - Bordes circulares, cuando los cruzamos cambia el reparto
    - Reproducción del escenario sin pérdida
    - Reproducción del escenario cíclico
- Realismo o no de precio fijo
    - El precio se mantiene
        - Con múltiplos de P
        - Mientras movamos restos
    - Cuando no se cumple
        - Si cedemos mas que restos, no perdemos el escaño
          sinó que empezamos a bajar el precio hasta que otro cociente entra y lo perdemos.
        - Si subimos restos mas alla del precio el nuevo cociente marcará el precio
          y el último cociente anterior caera.
    - Normalmente los cocientes suelen estar juntos
    - En esos rincones se podría estar ocultando la pretendida ventaja.
    - En todo caso en el próximo análisis lo cubre


**LO QUE QUEDA DE ESTE APARTADO ES BORRADOR A REESCRIBIR PORQUE SE MOVIERON COSAS FUERA**



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



El objetivo final sería evaluar la transferencia de votos entre candidaturas,
pero en un primer nivel transferencias contra la abstención.
Eso implica que solo la candidatura considerada modifica sus votos,
manteniendo el resto de candidaturas los suyos.

Haremos también la suposición para toda la fase 2,
de que el trasvase de votos que vamos a simular
no implica cambios en el precio, 
es decir, supondremos que el precio de corte no se ve alterado con el cambio.
Sabemos que eso no es cierto, por lo que hemos observado empíricamente.



## Probabilidad de cambios en la representación

Dada una situación inicial de referencia desconocida,
planteemos que cambiamos los votos de una candidatura en N votos.
¿Qué cambios son posibles y con qué probabilidades se pueden
producir en su repesentación en escaños?

Si no conocemos la representación de una candidatura o incluso
si la conocemos con una cierta incerteza siguiendo una distribución normal,
podemos decir por el Theorema de 



## Alcance de la suposición de precio fijo

> TODO:
> Aquí entramos en un nivel de análisis que justamente estamos diciendo no querer entrar.
> Considerar señalar simplemente que se ha observado el cambio de precio empíricamente.
> Mover la casuística a un punto donde sepamos más del tema.
> Candidatos: las conclusiones de esta fase o de la siguiente o la intro de la siguiente.

Sin embargo aún hay muchos otros casos en que
un trasvase de escaños implica un cambio en el precio de corte:

Cuando un trasvase consume más allá de los restos de una candidatura,
no tiene porque perder el escaño en ese momento.
Justamente el precio se adapta reduciéndose,
hasta que franquea un cociente menor y
su candidatura se queda con el escaño.

Cuando un trasvase suma restos a una candidatura por encima del precio de corte,
esta la candidatura obtiene un escaño de la que fijaba el precio hasta ese momento
y pasa a fijarlo la que ha crecido.

Cuando la candidatura que recibe votos es la que fija el precio de corte,
el precio estará augmentando, y, en algún momento,
alguno de los coeficientes mayores pasarán a ser menor
y cederle el escaño.

> TODO: Hemos demostrado que eso no pasará antes de trasvasar $P_d$ votos?



