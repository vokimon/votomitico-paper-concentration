
### Fase 2: Desarrollo de un modelo simplificado

### Objetivo

El objetivo de esta fase es desarrollar un modelo matemático  
que permita explicar las observaciones empíricas de la fase 1.  
A partir del modelo, se extraerán conclusiones sobre qué predicciones  
se pueden hacer sobre el efecto de un trasvase entre dos partidos  
en el resultado conjunto de ambos.

### Procedimiento

1. **Establecimiento de un marco algebraico para D'Hondt**
    Para superar la perspectiva procedural de D'Hondt y permitir su tratamiento algebraico,
    se estableció un marco de trabajo que relaciona todas sus entidades (Votos, restos, cocientes, escaños) a partir de el precio de corte.

2. **Cálculo probabilístico de los cambios en la representación**
    Dada la incertidumbre de saber la magnitud de los restos,
    se estableció su distribución de probabilidad,
    que considerando un número de votos recibidos o emitidos,
    permite calcular la probabilidad de un cambio en los escaños en cierto sentido.

3. **Cruce de probabilidades entre emisor y receptor**  
    Se construyó una representación gráfica del cruce de probabilidades
    entre emisor y receptor de un trasvase que permite
    conocer la probabilidad de cada posible resultado.

4. **Comprobación de la coincidencia con los patrones cíclicos observados**  
    Finalmente, se analizó la evolución de un trasvase progresivo de votos, en este modelo,
    comprobando si se generaban los mismos patrones cíclicos que ya se habían observado empíricamente. 


Después del procedimiento, lo siguiente es el **marco algebraico para D'Hondt**, donde detallamos las definiciones de los elementos clave como el precio de corte, los cocientes y los restos, con las correcciones y las aclaraciones que hemos hecho.

### Marco algebraico para D'Hondt

Para superar la visión procedural clásica de D'Hondt,
planteamos un marco algebraico que relaciona todas las entidades involucradas en el reparto de escaños:
votos, restos, cocientes, escaños y el precio de corte.
La potencia de esta aproximación es que, al entender que el objetivo del algoritmo es encontrar el precio de corte (Pc),
podemos suponer que este precio está fijado, pero representado algebraicamente sin un valor específico, y relacionar el resto de las entidades sin tener que ejecutar el algoritmo.

#### Definición de los elementos:

- **Votos (Vi)**: Son el número total de votos obtenidos por la candidatura **i**.
- **Escaños (Ei)**: Son el número de escaños asignados a la candidatura **i**.
- **Restos (Ri)**: Son los votos restantes para la candidatura **i**, calculados como la diferencia entre los votos a la candidatura y el producto de los escaños por el precio de corte:  
  $$ Ri = Vi - Ei \cdot Pc $$
  donde $ 0 \leq Ri < Pc $.

- **Cocientes (Pij)**: Representan el precio necesario para que la candidatura **i** obtenga el **j**-ésimo escaño.  
    $ Pij = Vi / j$
- **Precio de corte (Pc)**: Es el valor que, una vez fijado, caracteriza la solución.
Dado el número de votos de cada candidatura,
el precio de corte permite inferir los escaños y sus restos.

### Probabilidad de cambios en la representación

Dada una situación inicial de referencia desconocida,
planteemos que cambiamos los votos de una candidatura en N votos.
¿Qué cambios son posibles y con qué probabilidades se pueden
producir en su repesentación en escaños?

Si no conocemos la representación de una candidatura o incluso si la conocemos con una cierta incerteza siguiendo una distribución normal,
podemos decir por el Theorema de 




#### Desarrollo del Modelo de Probabilidades

Una vez establecido el **precio de corte** ($$ P_c $$), analizamos cómo los trasvases de votos entre partidos afectarían la distribución de escaños. Para hacerlo, representamos cada posible situación de los restos de los partidos \( A \) y \( B \) en un **cuadro de probabilidades**. En este cuadro, cada punto dentro del cuadro representaba una combinación de los restos de \( A \) y \( B \) al inicio del proceso, con los valores de los restos dentro del rango \( [0, P_c) \).

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

---

## Fase 2: Desarrollo de un modelo simplificado

### Objetivo

El objetivo de esta fase es construir un modelo matemático que permita explicar las observaciones empíricas de la Fase 1 y, a partir de este, extraer conclusiones sobre los trasvases de votos entre los partidos dentro de un bloque ideológico. Este modelo no solo nos ayuda a comprender los patrones cíclicos observados en la simulación, sino que también nos permite realizar predicciones bajo incertidumbre.

### Procedimiento

#### 1. Establecimiento de un marco algebraico para D'Hondt

Para superar la visión procedural clásica de D'Hondt y facilitar su tratamiento algebraico, hemos propuesto un **marco de trabajo** que relaciona todas las entidades involucradas en el sistema de reparto de escaños. 

Este marco parte de la premisa de que el objetivo del sistema no es simplemente repartir escaños de forma secuencial, sino establecer implícitamente un **precio de corte** ($P_c$), que representa la cantidad de votos necesarios para conseguir un escaño. Con este enfoque, podemos representar y trabajar algebraicamente los votos, los escaños y los restos, sin necesidad de aplicar el algoritmo paso a paso.

#### 2. Cálculo probabilístico de los cambios en la representación

Dado que la **situación inicial** de votos y escaños es incierta, planteamos un modelo probabilístico para estimar los cambios posibles en los escaños cuando hay un trasvase de votos entre partidos. 

Definimos los **restos combinados** de los partidos en el marco de trabajo y los representamos dentro de una distribución de probabilidad que permite calcular la probabilidad de que un trasvase de N votos cause un cambio en la representación en escaños. Este modelo es útil cuando no tenemos acceso a los resultados exactos, pero contamos con estimaciones sobre los votos y los cocientes de cada partido.

#### 3. Cruce de probabilidades entre emisor y receptor

Para comprender cómo un trasvase de votos entre dos partidos puede alterar la representación conjunta del bloque, construimos una **gráfica de cruce de probabilidades**. En ella, representamos la probabilidad de los diferentes resultados que pueden surgir cuando se transfieren N votos de un partido a otro. 

Este cruce de probabilidades permite no solo prever los posibles efectos de un trasvase, sino también ajustar el modelo a la realidad de cada elección, considerando las distribuciones específicas de votos y restos.

#### 4. Comprobación de la coincidencia con los patrones cíclicos observados

Una vez implementado el modelo, verificamos si los patrones observados en las simulaciones de la Fase 1 se reproducen bajo este enfoque. Al realizar trasvases progresivos de votos entre los partidos, observamos si los ciclos de ganancia y pérdida de escaños se alinean con los resultados empíricos. Este análisis es clave para confirmar la validez del modelo y ajustarlo a los patrones de comportamiento observados.

### **Fase 2: Desarrollo Analítico y Modelización**

1. **Hipótesis Inicial**
   - Breve descripción de las observaciones y los resultados previos de la fase 1.
   - Explicación de la necesidad de un modelo para explicar los resultados observados (distribución de restos, trasvases de votos, etc.).

2. **Procedimiento**
   - Resumen del procedimiento de análisis, describiendo de manera general los pasos que se seguirán para llegar al modelo probabilístico.

3. **Descripción Algebraica de D'Hondt**
   - **Justificación y Conexión del Precio de Corte \( P_c \)** como una aproximación válida para simplificar el modelo. Se explica cómo el concepto de \( P_c \) permite abstraer las complejidades del algoritmo de D'Hondt, facilitando el análisis algebraico de los votos, escaños y restos, sin necesidad de aplicar todos los detalles del algoritmo.
   - Introducción de la fórmula algebraica básica: \( V_i = E_i \cdot P_c + R_i \), donde \( V_i \) son los votos, \( E_i \) los escaños y \( R_i \) los restos.

4. **Desarrollo Probabilístico**
   - Análisis de la distribución de los restos con un precio de corte fijo.
   - Comprobación empírica de la hipótesis de distribución uniforme.
   - Introducción de la matriz de probabilidades cruzadas para modelar las transferencias de votos.
   - Estudio de las zonas de ganancia/pérdida de escaños y la confirmación de la ganancia cero.
   - **Trasvases sucesivos** como una línea en la matriz y contraste de resultados con los patrones empíricos observados.

5. **Resultados y Análisis**
   - Discusión de los resultados obtenidos a partir del modelo probabilístico.
   - Validación empírica de las predicciones del modelo.

6. **Reflexiones sobre el Modelo**
   - **Cercanía a resultados empíricos**: Análisis sobre cómo los resultados obtenidos en el modelo se ajustan a los patrones empíricos observados, y si el modelo refleja adecuadamente las condiciones de los casos reales. (Este punto podría ir también en el apartado de **Resultados y Análisis**, si se considera más apropiado).
   - **Reflexión**: Los resultados empíricos abarcan casos muy limitados y concretos. Esto implica que el modelo propuesto puede no ser completamente representativo de todas las posibles variaciones en situaciones más generales o diversas.
   - **Limitación**: Existen casos en los que la probabilidad de los restos no es indeterminada, lo que afecta la validez de las suposiciones del modelo y puede llevar a conclusiones incorrectas si no se ajusta adecuadamente.
   - **Limitación**: El modelo considera un precio de corte fijo \( P_c \), lo que simplifica el análisis, pero sabemos que durante un trasvase de votos, el precio de corte puede cambiar, lo que introduce una fuente de incertidumbre no contemplada en este modelo simplificado.

7. **Conclusiones**
   - Resumen de lo que se ha logrado hasta el momento.
   - Conclusiones sobre el modelo propuesto y su capacidad para explicar el comportamiento observado.
   - Transición hacia la fase 3, donde se utilizará un modelo algebraico más riguroso y detallado.


