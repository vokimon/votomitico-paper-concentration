
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

Se puede partir un trasvase de un número arbitrario de N votos,
en dos trasvases sucesivos,
uno de la parte exactamente divisible por $P_{max}$,
y otro trasvase del resto.

Por el teorema de resultados repetidos,
el trasvase de la parte divisible por $P_{max}$
nos lleva a una situación donde
el mismo precio genera los mismos restos,
los mismos escaños para terceras candidaturas,
y un trasvase de escaños de A a B
que conserva el resultado conjunto.

Quedaría por saber qué pasa con un trasvase de N votos
donde N sea una fracción del precio de escaño
$0 <= N < P_{max}$.

Lo que pase va a depender de qué restos tengan las candidaturas emisora y receptora
en el escenario de partida.
Si la emisora tiene restos menores que $N$, perderá un escaño.
Si la receptora tiene restos mayores que $P_{max} - R$ ganará un escaño.

![
Zonas en los restos en las que un cambio de votos menor que P,
pueden producir cambios en el resultado de una candidatura.
](figures/critical-zones.pdf)

El tamaño del trasvase N define lo extenso de esas zonas críticas de restos.
Los restos de ambas candidaturas pueden estar o no, de forma independiente,
en su zona crítica.
Lo que da 4 posibles combinaciones:
Si ninguna candidatura está en zona critica, el trasvase no tiene efecto alguno.
Si solo la receptora está en su zona crítica, el trasvase implica un incremento en un escaño en el resultado conjunto.
Si solo la emisora está en la zona crítica, el trasvase generará un empeoramiento de un escaño del resultado conjunto.
Finalmente, si ambas están en zona crítica, aunque un escaño pase de una a otra, el resultado conjunto queda igual.

Sin embargo, solo podemos saber
donde de los restos está una candidatura,
en un análisis a posteriori.
Es decir, en un análisis de caja blanca.
Si estamos en una situación de caja gris,
necesitaremos derivar la probabilidad
de que una candidatura este en cierta zona de restos.


## Distribución probabilística de los restos

Necesitamos saber,
antes de que se produzca un resultado electoral,
cual es la probabilidad de que una candidatura
esté en una de las zonas críticas de restos.
Tenemos dos posibles fuentes de información:
los resultados de convocatorias anteriores
y las encuestas electorales [@alaminos2023metodos].

Las encuestas nos permiten modelar el voto recibido por un partido
como una distribución de probabilidad normal con una esperanza
y una dispersión determinada por el margen de error [@agresti_statistical_2018].

Dado un precio de reparto arbitrario $P$,
los restos se obtienen al aplicar el módulo con base $P$ a los votos recibidos.
Aplicar el módulo a una variable de distribución normal
da lugar a una distribución normal cíclica [@fisher_wrapped_1995],
donde la base del módulo, el precio $P$, define el periodo.

Cuando la varianza de la distribución original es baja,
la probabilidad de la cíclica se concentra en torno a una moda,
$\hat{V_i} \bmod P$.
En este caso diremos que la distribución tiene un perfil _sesgado_.

Sin embargo, a medida que aumenta la varianza de la distribución original,
esa concentración se diluye progresivamente,
aproximándose cada vez más a una distribución uniforme.
En este caso diremos que la distribucion tiene un perfil _uniforme_.

En la práctica,
se considera que una distribución normal cíclica
es equivalente a una uniforme cuando:

$$
\sigma \gtrsim \frac{P}{\sqrt{2\pi}}
$$

$$
P \lesssim \sqrt{2\pi} \cdot \sigma \approx 2.5 \cdot \sigma
$$

Combinando esta relación con la del precio en función de los escaños,
y la fórmula del error muestral[^error-muestral],
obtenemos la siguiente desigualdad, equivalente a la anterior:

[^error-muestral]:
    La fórmula para el error muestral se calcula como:

    $$
    SE = \sqrt{\frac{q (1-q)}{n}}
    $$


$$
n \lesssim q (1 - q) \cdot \left[ 2.5 (E + fK) \right]^2
$$

donde 
$E$ el número de escaños a repartir en la circunscripción,
$K$ el número de candidaturas,
$f$ el promedio de restos por candidatura como factor de $P$,
$n$ el tamaño muestral para esa circunscripción,
y $q$ la proporción estimada de voto para una candidatura concreta en la circunscripción.

Esta desigualdad recoge cómo distintos factores,
en un escenario de análisis concreto,
inclinan la distribución de restos
hacia un perfil sesgado o uniforme.

En concreto, las siguientes situaciones favorecen un perfil sesgado:

- **$n$** alto: muestra amplia en la circunscripción.
- **$E$** bajo: la circunscripción reparte pocos escaños
- **$K$** o **$f$** bajos: pocas candidaturas con opción a escaño en la circunscripción
- **$q$** bajo: candidatura muy pequeña, con una proporción estimada cercana a 0[^q-alto]

[^q-alto]:
    Técnicamente, también se daría con $q$ cercano a 1,
    pero representaría una situación inusual de concentración
    casi total del voto en una sola candidatura.

Las situaciones con perfil sesgado,
son análogas a las situaciones
de caja blanca pero introduciendo
cierta incertidumbre.
Por ello es posible cierto voto estratégico
que comentaremos más adelante.

En lo que queda de este análisis
consideraremos que los restos se aproximan
a una distribución uniforme,
obviando estos casos.




Outline:

- [x] Segun las referencias, las encuestas tienen ciertos parametros
- [x] Esos parametros son ¿globales?, si dividimos por partido y circunscripción, la muestra es menor y el error sera mayor
- [x] Sirva pues el error global como cota inferior
- [ ] Pasos para convertir los datos tecnicos de la encuesta en una distribucion de probabilidad
- [ ] De distribucion de probabilidad de voto a probabilidad de restos
- [ ] Cuando podemos considerar la probabilidad de restos uniforme
- [ ] Contrastar con los valores de encuestas reales
- [ ] Recordar que se acentuara si nos concentramos en provincias y partidos concretos
- [ ] Conclusion: distribucion uniforme
- [ ] Enumerar las salvedades












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
- Comparación con los resultados empíricos
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
alguno de los cocientes mayores pasarán a ser menor
y cederle el escaño.

> TODO: Hemos demostrado que eso no pasará antes de trasvasar $P_d$ votos?



