---
lang: es
bibliography: bibliography.bib
---

# Efectos electorales de trasvases de voto entre partidos con base electoral común

Sobre el sistema de representación proporcional de D'Hondt,
existe una intuición ampliamente difundida que sostiene que
trasvasar votos de un partido pequeño a uno grande
aumenta la representación conjunta del bloque,
bajo la suposición de que este sistema
permite a los partidos más grandes traducen los votos en escaños con mayor eficiencia.
Nuestro análisis descarta categóricamente este supuesto,
mostrando que los efectos de dichos trasvases
se limitan a una diferencia de un escaño por circunscripción,
que puede ser positiva o negativa con la misma probabilidad,
y que es independiente de la dirección del trasvase.
En resumen, en condiciones normales de cierta incertidumbre
sobre los resultados exactos de la votación,
la concentración del voto no produce ningún tipo de mejora
de los resultados conjuntos.
También se estudian, por su importancia y ocurrencia,
ciertos casos especiales en que la incertidumbre es menor
y los supuestos del caso general no aplican.


## Introducción

### Una perspectiva habilitadora del sistema D'Hondt

El sistema de representación proporcional de D’Hondt [@dhondt1878; @sartori2005],
también conocido como _reparto por cocientes decrecientes_,
se emplea habitualmente en España para asignar escaños
en elecciones generales, autonómicas, europeas y municipales [@congreso1985loreg].
El reparto se realiza independientemente dentro de cada circunscripción electoral,
transformando los votos obtenidos por cada candidatura en escaños,
según un orden determinado por sus cocientes de reparto.

El uso habitual del sistema D'Hondt es procedural:
Se aplica un algoritmo y se obtiene el reparto de escaños.
Sin embargo, este artículo adopta una perspectiva diferente,
que facilita una comprensión más intuitiva de las dinámicas internas
y habilita un tratamiento algebraico del reparto de escaños.

El algoritmo de D'Hondt genera una serie de cocientes,
dividiendo los votos de las candidaturas por sucesivos enteros,
y seleccionando los cocientes mayores hasta completar el número de escaños disponibles.
Es decir, como su nombre indica,
los cocientes se escogen en orden decreciente.
A continuación, se asignan los escaños a las candidaturas
de las que provienen los cocientes seleccionados.

La visión procedural del sistema D'Hondt complica la comprensión
de las dinámicas subyacentes, ya que los puntos de decisión
y la intrincada interdependencia entre variables dificultan
la formulación algebraica y enmascaran las relaciones que determinan
el reparto de escaños.

La idea habilitante es entender el algoritmo de D'Hondt
como la búsqueda de un **precio de corte**,
*el número de votos necesarios
para que una candidatura consiga un escaño.*
Este precio, aunque no esté determinado, permite establecer relaciones
entre los demás elementos que intervienen en el reparto,
ignorando las complejidades del algoritmo,
lo cual se desarrollará más adelante.


La existencia de dicho **precio de corte** $P_c$, aunque no sepamos cuál es,
nos permite tratar algebraicamente el resto de elementos relacionados.

$$ V_i = E_i \cdot P_c + R_i $$

Siendo $V_i$ los votos obtenidos por la candidatura $i$,
$E_i$ los escaños que ha conseguido,
y $R_i$ los votos que no han llegado a sumar escaño, que llamaremos **restos**,
y serán por construcción siempre menores que $P_c$.

![Un ejemplo gráfico de la fórmula _Vi = Ei  · Pc + Ri_](seats-and-remainder.pdf)

En resumen, esta idea nos permite trabajar de forma genérica con resultados indefinidos,
sin tener que aplicar el algoritmo,
suponiendo que existe tal precio, representándolo algebraicamente ($P_c$),
y estableciendo relaciones algebraicas con el resto de elementos

### Lógica de bloques

En muchos sistemas políticos democráticos,
los partidos compiten por bases electorales compartidas formando bloques yuxtapuestos en diferentes ejes ideológicos
(como progresismo-conservadurismo, capitalismo-socialismo o independentismo-unionismo).
Esa base electoral compartida genera cierta competencia entre candidaturas afines.
La situación política en España se corresponde plenamente con esto.

En contextos como este, es un fenómeno recurrente apelar al **voto estratégico** o **voto útil**,
buscando un trasvase de votos hacia la formación mayoritaria de un bloque.
Esto se hace bajo la suposición de que los partidos grandes son más eficientes a la hora de convertir votos en escaños,
dado que el sistema D'Hondt tiende a favorecerles.

Si tal supuesto fuera falso,
votantes que votaran estratégicamente bajo esta premisa
podrían incluso provocar el efecto contrario y perjudicar
al bloque, como ha ocurrido en algunas ocasiones[^1].

[^1]: Ejemplo real: Elecciones generales de xxx de 20xx en Barcelona.
    Muchos votantes de ZURDOS respondieron al llamamiento de PROGRES
    para concentrar el voto y frenar el ascenso de la extrema derecha.
    Así, ZURDOS se quedó a pocos votos de conseguir un escaño más,
    mientras que a PROGRES les sobraron muchos votos que no se tradujeron en representación.
    El último escaño se lo llevó VOX,
    pero hubiera ido al bloque de izquierda si algunos de los votos trasvasados
    a PROGRES se hubieran mantenido en ZURDOS.

### Transferencias entre partidos

Formalizamos el problema:
Dada una **situación de referencia**,
un reparto de votos inicial,
**¿en qué sentido y magnitud se alteraría el resultado conjunto de dos formaciones,
si hay una transferencia de N votos de una a la otra?**

Como la situación de referencia es desconocida,
pero hasta cierto punto estimable,
necesitaremos hacer estimaciones probabilísticas del resultado,
con parámetros que podamos ajustar a posteriori a situaciones reales.

## Metodología




