
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
Lo que da lugar a 4 posibles casos:

- Caso estable: ninguna candidatura está en zona critica; el trasvase no tiene efecto alguno.
- Caso de ganancia neta: solo la receptora está en su zona crítica; el trasvase implica un incremento en un escaño en el resultado conjunto.
- Caso de pérdida neta: solo la emisora está en la zona crítica; el trasvase generará un empeoramiento de un escaño en resultado conjunto.
- Caso de transferencia: ambas están en zona crítica; aunque un escaño pase de una a otra, el resultado conjunto queda igual.

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

TODO: considerar incorporar el analisis de datos historicos

TODO: considerar aterrizar números con enquestas reales


## Probabilidad combinada de receptor y emisor

En el apartado anterior se estableció la suposición
de que, con excepciones, la distribución de los restos es uniforme.
Es decir, fijado un precio de escaño,
los votos de una candidatura pueden estar en cualquier
punto entre un escaño y el siguiente con igual probabilidad.
Y, por tanto, los restos que no han servido para sumar
escaño, estarán en un punto en el intervalo $[0,P)$.

Si hay una transferencia de emisor a receptor de $N < P$ votos,
y bajo la suposición de que las transferencias no alteran el precio,
el emisor perderá un escaño si $N > R_e$, como establecimos antes.
Dada la distribución uniforme de los restos,
la probabilidad de que el emisor esté en esa zona crítica es de $N/P$.
Al mismo tiempo, la probabilidad de que el receptor este en su zona critica
también es de $N/P$.

Ambos eventos se pueden dar o no de forma independiente.
Esto da lugar a las siguientes probabilidades para cada caso combinado:

- Caso estable $(P-N)^2/P^2$
- Caso de trasnferencia $N^2/P^2$
- Caso de perdida neta $N(P-N)/P^2$
- Caso de ganancia neta $N(P-N)/P^2$

Esto se puede visualizar en la figura \ref{fig:transfer-probability-square},
donde el cuadrado representa todas las combinaciones posibles de restos
entre emisor y receptor, y las áreas ilustran
la probabilidad relativa de cada caso.

En resumen, una transferencia de $N < P$ votos puede tener tres efectos posibles en el resultado conjunto:

- una **ganancia neta de +1 escaño**,
- una **pérdida neta de -1 escaño**,
- o **ningún cambio en el total de escaños**.

Los dos primeros tienen la **misma probabilidad**,
que alcanza su máximo cuando $N = P/2$, y **nunca supera el 25 %** cada uno.

Los casos sin impacto en el resultado conjunto
—es decir, el caso estable y el de transferencia entre candidaturas— tienen,
en total, una **probabilidad mínima del 50 %**, que se da precisamente cuando $N = P/2$.

Dado que los únicos casos que alteran el resultado conjunto tienen efectos opuestos con igual probabilidad,
la **esperanza matemática** de ganancia o pérdida es **cero**:
el efecto medio de realizar una transferencia es neutro.


## Contraste con los resultados empíricos


En la fase de análisis empírico con simulador,
se estudiaron trasvases progresivos de votos entre candidaturas,
observando cómo variaban los resultados en escaños y otros parámetros internos.

En esa fase obteníamos dos patrones diferenciados:

- Un patrón más común donde el escaño perdido por el emisor
  pasaba primero a una tercera candidatura antes de llegar al receptor.
- Otro patron más raro que se daba sobre todo en casos sintéticos,
  donde el traspaso del escaño era directo entre emisor y receptor.

Desde el marco geométrico actual,
cada situación inicial puede representarse como un punto aleatorio
en el cuadrado $[0, P) \times [0, P)$,
donde cada eje indica los restos iniciales
de la candidatura emisora y receptora, respectivamente.

Una transferencia progresiva de $N$ votos
se modela como una línea diagonal de pendiente -1
que atraviesa el cuadrado pasando por el punto inicial.

Cuando esta línea cruza los bordes del cuadrado,
se producen cambios en el reparto de escaños:
- Cruzar el borde inferior implica que el emisor pierde un escaño.
- Cruzar el borde derecho implica que el receptor gana un escaño.

El traspaso directo ocurre cuando la diagonal pasa por el vértice superior izquierdo del cuadrado,
es decir, cuando el emisor y receptor están simultáneamente en su zona crítica,
permitiendo la transferencia directa del escaño sin cambios intermedios.

En los demás casos,
el proceso se da en dos etapas separadas,
con pérdida de escaño primero en el emisor y posterior ganancia en el receptor,
permitiendo que el escaño pase temporalmente por una tercera candidatura.

Este análisis aporta una interpretación geométrica que explica
los patrones observados en la fase empírica con simulador.


## Revisión de las suposiciones del modelo simplificado

El _modelo simplificado_ explicado en este capítulo
se basa en dos suposiciones clave:
Un precio de escaño fijo
y una distribución de restos uniforme.
Estas suposiciones permitieron simplificar el modelo y deribar conclusiones útiles,
pero merecen ser revisadas para entender el alcance real de los resultados obtenidos.


La **suposición del precio fijo**
considera que el precio del escaño no se ve alterado por el trasvase.
Es una simplificación útil porque cuando cambia el precio
hay que recalcular todas las asignaciones de escaños,
y eso complica el análisis,
pero, si consideramos que el precio no cambia,
las terceras candidaturas implicadas en el trasvase de votos
tendrían exactamente el mismo reparto.

Como vimos en la formulación algebráica,
esta suposición es cierta para ciertos casos:
Para trasvases del escaños enteros (múltiplos del precio),
y para trasvases que se limiten a restos en el emisor
y se queden como restos en el receptor sin que sumen el precio.
Estos dos casos o una combinación de ellos cubren la mayoría de casos
pero no los más interesantes.

¿Cuándo no se cumple esta suposición?

Justamente, el precio se adapta
para que se repartan exactamente los escaños disponibles.
Si no ajustamos el precio, cuando la emisora
pierda pero no gane la emisora, repartiremos un escaño de menos.
Y al revés, cuando la receptora gane pero no pierda la emisora,
repartiremos un escaño de más.

Sin intentar hacer un análisis sistemático,
analicemos estos dos casos:

Cuando agotamos los restos del emisor,
en el modelo simplificado,
el emisor pierde el escaño,
pero no explica a donde va a parar ni porqué.
Lo que pasa en realidad es que el precio de corte
se ajusta al precio que requiere el emisor para mantener el escaño
y lo hace mientras que dicho precio no franquee el primer cociente excluido.
Cuando se franquea ese cociente, el emisor pierde finalmente el escaño
y lo toma la candidatura a la que pertenece dicho cociente.
En resumen, la perdida de escaño es posterior
y lo gana la candidatura con el primer cociente excluido en la situación de partida.

El otro caso es cuando el trasvase hace que los restos del receptor superen el precio actual.
En el modelo simplificado, significa que gana un escaño,
pero no explica de quien lo gana.
Lo que pasa en realidad, es que,
cuando los restos del receptor superan el precio de corte,
el receptor pasa a marcar dicho precio subiéndolo,
y haciendo que la candidatura que marcaba el precio pierda su último escaño.
Hemos visto que dicha candidatura sera, la que lo marcaba orignalmente,
o, al perder votos la emisora, esta, o bien,
la del primer cociente excluido.

En resumen,
la suposición de precio fijo
modela correctamente las zonas de _status quo_.
No predice exactamente donde se gana o pierde el escaño,
adelantando la perdida de escaños de la emisora y retrasando la ganancia de la receptora.
Tampoco justifica intercambios con terceros, por lo que reparte escaños de más o de menos.
Normalmente vemos que la tercera candidatura es la del primer cociente excluido
pero no tenemos elementos para asegurar que es una regla general.

La suposición de **distribución uniforme de restos**,
considera que la probabilidad de los restos de una candidatura
se distribuyen uniformemente en el intérvalo $[0, P)$.
Es útil para simplificar el modelo probabilístico de escenarios de caja gris
y se cumple cuando la incertidumbre de los resultados es suficentemente alta.

No se cumple en varios supuestos:

- Cuando las encuestas son más precisas de lo normal en la circunscripción de interés.
- Cuando se reparten pocos escaños
- Para candidaturas extraparlamentarias
- Cuando hay pocas candidaturas con opciones de representación

En estos casos, el actual análisis probabilístico no es aplicable.
Eso no quiere decir que no podamos hacer predicciones,
más bien al contrario.
En estos casos tenemos más información que en el caso supuesto,
y esa informacíon sí que es explotable para hacer voto estratégico
como se trata más adelante.


En resumen, estas dos simplificaciones han habilitado una primera aproximación analítica al problema
y, aunque no se ajusten del todo a la realidad, proporcionan
un primer marco explicativo para los fenómenos observados.
Además proporciona una intuición geométrica con mucho potencial divulgativo.

El análisis de sus limitaciónes también nos revela los factores relevantes
para tenerlos en cuenta para construir un modelo general en la siguiente fase.
En vez de simplificar a base de suposiciones,
simplificaremos escogiendo muy selectivamente los escenarios posibles
y los factores implicados.


