---
lang: es
bibliography:
- bibliography.bib
- bibliography-vote-concentration-calls.bib
- bibliography-divulgacion-bulo.bib
---

# Efectos electorales de trasvases de voto entre partidos con base electoral común

Sobre el sistema de representación proporcional de D'Hondt,
existe una intuición ampliamente difundida que sostiene que
trasvasar votos de un partido pequeño a uno grande
aumenta la representación conjunta del bloque,
bajo la suposición de que este sistema
permite a los partidos más grandes
traducir los votos en escaños con mayor eficiencia.
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

El sistema de representación proporcional de D’Hondt [@dhondt1878; @sartori2005],
también conocido como _reparto por cocientes decrecientes_,
se emplea habitualmente en España para asignar escaños
en elecciones generales, autonómicas, europeas y municipales [@congreso1985loreg].

Este artículo no busca evaluar la idoneidad del sistema
ni proponer alternativas, como ya hacen otros autores
[@medzihorsky2019rethinking; @lardeyret1991problem; @bochsler2010gains],
sino ofrecer herramientas para **comprender su lógica interna**,
y, de este modo, evaluar cómo distintas decisiones
afectan al reparto de escaños.
Estas herramientas son útiles tanto para el diseño de campañas,
como para el análisis post-electoral,
pero especialmente para guiar decisiones de **voto estratégico**
[@wilder1999explaining; @schroeder2019understanding],
donde interpretaciones infundadas,
por error o interés de quien las difunde,
pueden inducir al electorado a estrategias contrarias a su intención.

Este articulo en concreto se centra,
en el **dilema de la concentración del voto en los mayoritarios**,
dentro de un contexto de **lógica de bloques**.
aunque el marco teórico que se establece
tendría utilidad en otros dilemas y contextos
donde las mecánicas del sistema D'Hondt tengan influencia.

### Lógica de bloques

El contexto de nuestro análisis parte de una **lógica de bloques**,
donde agrupamos las candidaturas en dos conjuntos antagónicos,
con el objetivo de maximizar los escaños obtenidos
por uno de los bloques en su conjunto.

Este enfoque no responde tanto a una realidad formal del sistema electoral,
que no reconoce alianzas preelectorales a efectos de reparto,
sino a una realidad política común:
la existencia de proyectos de gobierno compartido
que dependen del resultado agregado del bloque.

Dentro de este contexto, emergen distintos dilemas estratégicos:
cómo distribuir el voto entre las candidaturas del bloque,
cuándo explorar pactos preelectorales, y
qué impacto tienen los trasvases internos sobre el resultado final.

### El dilema de la concentración del voto

En este artículo nos centramos en un dilema muy concreto
y ampliamente asumido por el electorado:
la idea de que, ante la ausencia de alianzas formales,
es **más eficaz concentrar el voto en la candidatura más fuerte del bloque**.

Esta creencia está muy extendida
y a menudo se apoya en ejemplos históricos o intuiciones sobre el sistema D’Hondt,
pero rara vez se fundamenta en un análisis estructurado del reparto.

Nuestro objetivo es cuestionar esta suposición,
ofreciendo un marco que permita **explorar cuándo esta estrategia es ventajosa**
y cuándo puede ser, en cambio, **contraproducente**.

A lo largo del artículo mostraremos que la respuesta
depende de múltiples factores,
entre ellos el número total de escaños,
la distribución de votos entre bloques y
la relación de fuerzas dentro del bloque minoritario.

### Lógica de bloque

Decimos que un perfil del electorado opera según una **lógica de bloque**
cuando éste pecibe que,
para alcanzar sus objetivos y prioridades políticas,
es más importante el resultado de un bloque de partidos en conjunto,
que lo que le pase a una candidatura o a otra en concreto.

Esto se da, sobre todo, en contextos multipartidistas
en los que las candidaturas comparten posición
en uno o varios ejes ideológicos o políticos,
como los ejes progresismo-conservadurismo,
capitalismo-socialismo o independentismo-unionismo.

Paradójicamente, esta coincidencia ideológica
les hace competir por **bases electorales compartidas**,
y estimula, especialmente en períodos electorales,
la **lógica partidista**, que prioriza la captación de poder
por parte de cada candidatura en concreto.

Más paradójico aún es que, desde una **lógica partidista**,
algunas candidaturas apelen a la **lógica de bloques**
para captar bases electorales
que, en realidad, son más cercanas
a otras opciones dentro del mismo bloque.

En contextos de **lógica de bloques**,
emergen diversos dilemas estratégicos.
Uno interesante es si conviene explorar pactos preelectorales
para maximizar el impacto del bloque.
Otro dilema, en el que nos centramos en este artículo,
es si la **concentración del voto** en las candidaturas más fuertes
beneficia al bloque en su conjunto.

## El dilema de la concentración

En contextos de lógica de bloques, es un fenómeno recurrente
apelar al **voto estratégico** o **voto útil**,
buscando la **concentración del voto**
hacia la formación mayoritaria de un bloque.
Esto se hace bajo la suposición de que los partidos grandes
son más eficientes a la hora de convertir votos en escaños,
dado que el sistema D'Hondt tiende a favorecerles.

Algunos ejemplos recientes de este tipo de llamamientos
por parte de políticos de color diverso incluyen:

- Asturias 2023: Garzón (IU) [@garzon2023asturias]
- Generales 2023: Sánchez (PSOE) [@sanchez2023generales]
- Generales 2023: Abascal (Vox) [@abascal2023generales]
- Galiza 2024: Rego (BNG) [@rego2024galiza]
- Euskadi 2024: Larrea (PNV) [@larrea2024euskadi]
- Euskadi 2024: Otegi (EH Bildu) [@otegi2024bildu]
- Europeas 2024: Feijóo (PP) [@feijoo2024europeas]
- Europeas 2024: Díaz (Sumar) [@diaz2024europeas]
- Catalanas 2024: Aragonès (ERC) [@erc2024concentrarvoto]
- Catalanas 2024: Puigdemont (Junts) [@puigdemont2024catalanas]
- Catalanas 2024: Illa (PSC) [@illa2024catalunya]

Si bien sería muy ingenuo exigir rigor de los políticos en campaña,
el argumento está profundamente interiorizado en la sociedad.
Periodistas y analistas lo incorporan en sus análisis y divulgaciones
lo que contribuye a su perpetuación [@tezanos_2019; @lavanguardia2023grandes; @elmundo2023calculo].

Cabe reconocer que algunos artículos han empezado a cuestionar este supuesto
[@eldiario_2023; @confidencial_2023; @infolibre_2023].
Matizan la idoneidad de su aplicación en algunos casos,
o justifican que no siempre sigue un comportamiento lineal.

Durante mucho tiempo, en la literatura científica,
también se ha dado por supuesto que D'Hondt favorecia a los mayoritarios
[@norris1997; @sutherland2003].
Pero, recientemente, [@medzihorsky2019rethinking]
pone en cuestión, con argumentos analíticos y empíricos,
que D'Hondt genere un beneficio desproporcionado a los grandes.

Tambien existen evidencias en casos recientes en España,
donde una concentración de voto en el mayor
no solo no ha tenido el efecto esperado,
sinó que ha sido contraproducente para el bloque[^1].

A la luz de estos precedentes, se ha evidenciado la necesidad  
de realizar un análisis más sistemático sobre este asunto.

[^1]: Ejemplo real: Elecciones generales de xxx de 20xx en Barcelona.
    Muchos votantes de ZURDOS respondieron al llamamiento de PROGRES
    para concentrar el voto y frenar el ascenso de la extrema derecha.
    Así, ZURDOS se quedó a pocos votos de conseguir un escaño más,
    mientras que a PROGRES les sobraron muchos votos que no se tradujeron en representación.
    El último escaño se lo llevó VOX,
    pero hubiera ido al bloque de izquierda si algunos de los votos trasvasados
    a PROGRES se hubieran mantenido en ZURDOS.



## Metodologia de análisis



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




