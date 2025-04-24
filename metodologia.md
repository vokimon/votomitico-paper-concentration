## Metodología de análisis

### Variación controlada

Una técnica central en esta investigación
es el método de _variación controlada_,
que utilizamos para comprender
cómo un cambio en el escenario electoral
afecta a los resultados.

Este enfoque se inspira en la Teoría de Juegos [@todo]
pero también incorpora herramientas de
simulación, optimización y teoría de sistemas [@todo].

Plantea estos tres pasos:

- **Situación inicial o de referencia**:
  Se supone un estado inicial del sistema.

- **Hipótesis de cambio**:
  Se plantea una modificación en la situación.

- **Evaluación de resultados**:
  Se observan los cambios en el resultado.

En el ámbito de este artículo,

- La **situación inicial** es un resultado electoral concreto.
- La **hipotesis de cambio** es un trasvase de votos entre candidaturas.
- Los **resultados** a evaluar son los escaños repartidos o cualquier otro parámetro de interés.

Por ejemplo:
Tomamos los resultados de las Generales de 2008 en España en Barcelona.
Planteamos un trasvase de 10.000 votos de C's a PSOE.
Calculamos el nuevo resultado
y vemos que C's ha perdido un escaño que ha ganado Iniciativa.

Este caso corresponde con un análisis de **caja blanca**,
donde conocemos la situación inicial.
Este enfoque es útil para estudios a posteriori como un anàlisis post-electoral.

Pero casi nos interesan más los casos de **caja gris**.
Estos son aquellos en los que no conocemos con certeza,
la situación de referencia.
Los llamamos de caja gris y no negra porque,
aunque no sepamos cuál será la situacion inicial,
disponemos de encuestas y datos históricos con los cuales
estimar la probabilidad de cada situación inicial.
Al cruzar el análisis probabilístico de cada situación inicial
con los resultados correspondientes,
podremos evaluar la probabilidad de cada posible resultado.


### Procedimiento

- Análisis empírico con simuladores
- Análisis con modelo aproximado
- Análisis con modelo integral


