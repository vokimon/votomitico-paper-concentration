# Outline

## Ultimo trabajado

- Introduccion
  - Resumen extendido
  - Logica de bloque
  - Dilema de concentracion del voto
  - Una perspectiva habilitadora de D'Hondt
- Metodologia de análisis
   - Situacion inicial y hipótesis de cambio
   - Caja negra y Caja gris
   - Procedimiento
     - Análisis empírico con simuladores
     - Análisis con modelo aproximado
     - Análisis con modelo integral
- Análisis empírico con simuladores
- Marco algebraico para el sistema D'Hondt
- Análisis con modelo aproximado
- Análisis con modelo integral
- Condiciones que habilitan el voto estratégico
    - Certidumbre en los restos
    - Partidos muy pequeños
    - Pocos escaños a repartir
    - Muchos escaños a repartir con umbral electoral
- Causas y refuerzos del Mito
- Conclusiones

## ultimo con chatgpt

1. Introducción
    - Planteamiento del dilema:
        - El problema de los bloques y la tendencia a concentrar el voto en candidaturas grandes.
        - Confusión generalizada sobre el funcionamiento del sistema D'Hondt.
    - Objetivo del trabajo:
        - Proporcionar herramientas conceptuales y técnicas para analizar los efectos del sistema de reparto proporcional.
        - Facilitar una comprensión más precisa para fundamentar mejor las estrategias de voto y las interpretaciones post-electorales.
    - Contribución del artículo:
        - Clarificación del sistema a través de un marco algebraico.
        - Introducción de una metodología de análisis contrafactual y anticipativo.
        - Identificación de ideas erróneas comunes y cómo corregirlas.

2. Metodología de análisis
    - Enfoque general:
        - Uso de hipótesis de cambio para explorar efectos de modificaciones en el reparto.
    - Tipos de análisis:
        - Caja blanca / A posteriori: con resultado electoral conocido.
        - Caja gris / Anticipativo: con parámetros inciertos, usando modelos probabilísticos.
    - Aplicación transversal:
        - Esta metodología se aplica tanto al análisis empírico como al algebraico.

3. Marco algebraico del sistema D'Hondt
    - Formalización del algoritmo:
        - Separación entre generación de cocientes y selección ordenada.
        - Introducción de los coeficientes y su significado.
    - Concepto de precio de corte ($P_c$):
        - Interpretación del último cociente elegido.
        - Fórmulas clave: relación entre votos, escaños y restos.
    - Valor umbral ($P_d$):
        - Papel en la estabilidad del reparto.
        - Relevancia en los modelos con cambio dinámico de precios.

4. Exploración de dinámicas y efectos
    - Fase 1 — Fundamento empírico:
        - Casos representativos que motivan el estudio (sin analizarlos en detalle).
    - Fase 2 — Modelo de reparto a precio fijo:
        - Evaluación de efectos de cambios manteniendo constante el precio.
        - Identificación de distorsiones y límites de este enfoque.
    - Fase 3 — Dinámica con cambio de precio:
        - Modelo más realista donde el precio se ajusta.
        - Evaluación de transiciones de escaños bajo cambios marginales de votos.

5. Errores comunes y correcciones
    - Mitos y creencias extendidas:
        - Por qué se cree que es mejor votar siempre a la candidatura más grande.
    - Análisis crítico:
        - Qué parte de esa lógica se sostiene y qué parte no.
        - Cómo las herramientas desarrolladas ayudan a responder con precisión.

6. Conclusiones
    - Resumen de aportaciones:
        - Herramientas para entender el reparto y anticipar efectos de cambios.
    - Utilidad del enfoque:
        - Cómo puede servir a votantes, partidos o analistas.
    - Líneas futuras:
        - Posibles extensiones del marco algebraico o de la metodología.



### **Fase 2: Desarrollo Probabilístico y Modelado de Trasvases**

1. **Introducción a la fase 2**
   - **Contexto**: Explicación breve de la fase 1, destacando el comportamiento observado y el reto de modelarlo.
   - **Objetivo de la fase 2**: Establecer un modelo basado en probabilidades para analizar los efectos de los trasvases de votos.

2. **Desarrollo de conceptos clave**
   - **Precio de corte**: Reintroducir el concepto de **precio de corte** (\(P_c\)), que es la clave para entender la asignación de escaños.
   - **Restos**: Explicar que, con un precio fijo \(P_c\), los restos de los votos están restringidos en el intervalo \(0..P_c\), y cómo esta restricción nos permite realizar ciertos cálculos.

3. **Análisis empírico y probabilístico de los restos**
   - **Comportamiento de los restos**: Descripción de cómo, al modificar los votos, los restos se mueven en un espacio circular.
   - **Distribución uniforme de los restos**: Establecer que, para un precio fijo, los restos siguen una distribución aproximadamente uniforme (aunque falta una aproximación analítica más rigurosa).
   - **Comportamiento ante trasvases de votos**: Explicar cómo los trasvases de \(N\) votos (positivos o negativos) pueden afectar los resultados, y cómo este análisis está relacionado con el **precio de corte**.

4. **Construcción del modelo probabilístico para los trasvases**
   - **Transferencia entre candidaturas**: Introducir la idea de una transferencia de votos entre dos candidaturas y cómo se construye una matriz de probabilidades cruzadas para evaluar los efectos del trasvase en ambos lados.
   - **Relación entre las probabilidades de los emisores y receptores**: Describir cómo las probabilidades cruzadas de las dos candidaturas se relacionan con el escaño y cómo se mantiene una esperanza de ganancia cero.

5. **Resultados sobre el comportamiento cíclico**
   - **Ciclicidad del trasvase**: Explicar que las transferencias de votos siguen una progresión continua que se corresponde con los resultados cíclicos observados en la fase 1.
   - **Geometría toroidal**: Detallar cómo la geometría de los trasvases puede modelarse a través de un espacio toroidal, donde las fronteras se conectan entre sí.

6. **Conclusiones intermedias**
   - **Simplificaciones del modelo**: Resumir las simplificaciones que se hicieron, como el precio de corte constante, a pesar de que sabemos que varía en la práctica.
   - **Desplazamiento hacia la fase 3**: Establecer que, aunque el modelo probabilístico funciona para ciertos casos, la fase 3 permitirá un análisis más preciso y algebraico.

---

### **Fase 3: Desarrollo Algebraico y Simplificaciones**

1. **Introducción a la fase 3**
   - Descripción de cómo la fase 3 se mueve hacia un análisis más algebraico, usando **el precio de corte** de manera más rigurosa y con nuevas simplificaciones.

2. **Nuevos elementos en el modelo algebraico**
   - Introducción del **primer cociente excluido** (\(P_d\)) como un nuevo parámetro.
   - Explicación de cómo la variación de \(P_c\) y \(P_d\) afecta al reparto de escaños.

3. **Modelado de transferencias en un espacio 1D**
   - Descripción de cómo la transferencia de votos entre dos candidaturas puede modelarse de manera simplificada en un espacio unidimensional.
   - Análisis de la evolución de los cocientes en función de los votos transferidos.

4. **Puntos de corte y su impacto**
   - Análisis de los puntos de corte de los cocientes y cómo estos determinan las zonas de ganancia/pérdida de escaños.

5. **Conclusiones**
   - Reflexión sobre cómo las simplificaciones anteriores y el nuevo enfoque algebraico permiten ajustar mejor los resultados a la realidad observada.

---

### **Fase 4 (Posible)**

1. **Casos que no se ajustan al modelo**
   - Análisis de excepciones y los casos que no siguen el patrón del modelo, explicando las razones y cómo estos se pueden tratar de manera independiente.

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
   - **Justificación y Conexión del Precio de Corte \( P_c \)** como una aproximación válida para simplificar el modelo.
        Se explica cómo el concepto de \( P_c \)
        permite abstraer las complejidades del algoritmo de D'Hondt,
        facilitando el análisis algebraico de los votos, escaños y restos,
        sin necesidad de aplicar todos los detalles del algoritmo.
   - Introducción de la fórmula algebraica básica:
        \( V_i = E_i \cdot P_c + R_i \), donde \( V_i \) son los votos, \( E_i \) los escaños y \( R_i \) los restos.

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


