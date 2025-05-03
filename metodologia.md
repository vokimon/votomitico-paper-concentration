# Metodología de análisis

## Variación controlada

La **variación controlada** es una metodología
que usamos de forma transversal en esta investigación
para comprender cómo un cambio en el escenario electoral
afecta a los resultados.

Esta metodología se inspira en principios generales tomados de
la Teoría de Juegos [@Cheng2020],
simulación[@Tekin2004],
optimización [@Barton2002] y
teoría de sistemas [@Kleijnen2008].

La metodologia plantea estos tres pasos:

- **Situación inicial o de referencia**:
  Se supone un estado inicial del sistema.

- **Hipótesis de cambio**:
  Se plantea una modificación en la situación.

- **Evaluación de resultados**:
  Se observan los cambios en el resultado.

Aplicándolo al ámbito de este artículo:

- La **situación inicial** es un resultado electoral concreto: histórico, hipotético o basado en encuestas.
- La **hipotesis de cambio** normalmente es un trasvase de votos entre candidaturas.
- Los **resultados** a evaluar son los escaños repartidos o cualquier otro parámetro de interés.

Por ejemplo:
Tomamos los resultados de las Generales de 2008 en España en Barcelona.
Planteamos un trasvase de 10.000 votos de C's a PP.
Calculamos el nuevo resultado
y vemos que, en comparación con el resultado original,
C's ha perdido un escaño que ha ganado Iniciativa.

Este ejemplo corresponde con un análisis de **caja blanca**,
donde conocemos la situación inicial.
Este enfoque es útil para estudios a posteriori como sería
un anàlisis periodístico post-electoral.

Más interesantes y complejos son los casos de **caja gris**.
Estos son aquellos en los que no conocemos con certeza,
la situación de referencia.
Los llamamos de caja gris y no negra porque,
aunque no sepamos cuál será la situacion inicial,
disponemos de encuestas y datos históricos con los cuales
estimar la probabilidad de cada situación inicial.
Al cruzar el análisis probabilístico de cada situación inicial
con los resultados correspondientes,
podremos evaluar la probabilidad de cada posible resultado.

## Hipótesis de cambio grupal

Es poco frecuente que un solo voto cambie un resultado.
Aunque puede ocurrir, no es lo habitual.
Por eso, formularemos las _hipotesis de cambio_
considerando un grupo de votantes de un determinado perfil
que tomarán coherentemente la misma decisión de cambio de voto.

Podemos incorporar el tamaño del grupo en el enunciado del problema
de dos formas complementarias:

- _¿Cómo un grupo de N personas, que
opte por votar a X en vez de Y, puede alterar el resultado
(y con qué probabilidad)?_

- _¿Cómo de grande ha de ser el grupo
para que cambie el resultado (con una cierta probabilidad)?_


## Procedimiento

La investigación se ha desarrollado en cuatro fases,
cada una de las cuales ha refinado y profundizado progresivamente
en el comportamiento del sistema D'Hondt
cuando se realizan trasvases de votos entre dos candidaturas.

### Fase 1: Análisis empírico {.unnumbered}

Primero se realizó un **análisis empírico**
utilizando un **simulador** de transferencia de votos,
aplicando _variación controlada_
a situaciones históricas y sintéticas.
Los resultados obtenidos contradecían las expectativas
de que el voto concentrado beneficiaría al resultado conjunto.
Esto nos llevó a descartar esta hipótesis como regla universal.
Pero solo simulamos una fracción de la infinitud de escenarios posibles,
por lo que los resultados no son necesariamente extrapolables.
Además, el simulador no proporciona una explicación de los efectos observados.

### Fase 2: Formulación algebraica {.unnumbered}

Dado que el algoritmo de D'Hondt
presentaba limitaciones para la generalización,
desarrollamos una formulación algebraica
que nos permitió abstraernos de él.
Esta representación nos llevó a conclusiones clave, 
como que trasvasar una cantidad de votos
equivalente al precio de corte,
mantenia constante el mismo precio corte,
los restos de todas las candidaturas
y el resultado conjunto de bloque.
Quedó como incognita qué sucede cuando traspasamos
una fracción de ese precio.

### Fase 3: Modelo aproximado {.unnumbered}

Bajo la aproximación, conscientemente burda, de que
el precio de corte no se ve alterado por los trasvases,
los restos quedaron como único parámetro
que determina cuando se gana o pierde un escaño.
Al modelar probabilísticamente los restos iniciales de receptor y emisor,
obtuvimos una probabilidad equivalente
para los escenarios de ganar y de perder un escaño conjunto.
También establecimos flujos progresivos de votos
y comprobamos que seguían patrones similares a los empíricos.

### Fase 4: Modelo general {.unnumbered}

En la cuarta fase, el objetivo era llegar a un modelo general,
eliminando las aproximaciones del modelo anterior.
Dado que el problema seguía siendo complejo,
en lugar de aproximar, redujimos la complejidad
identificando los parámetros esenciales para ignorar el resto.
Así, pudimos establecer, de forma general,
cómo y dónde se producían los cambios de precio
a lo largo de un trasvase progresivo,
y cuáles eran sus implicaciones en la representación individual y conjunta del bloque.
Esto permitió caracterizar y parametrizar las características
observadas empíricamente en función de los parámetros del problema,
y concluir que las observaciones empíricas tenían un carácter universal.




