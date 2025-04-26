---
lang: es
author: David García Garzón
# {.unnumbered}
title: Efectos electorales de trasvases de voto entre partidos con base electoral común
numbersections: true
classoption:
#- twocolumn
bibliography:
- bibliography.bib
- bibliography-vote-concentration-calls.bib
- bibliography-divulgacion-bulo.bib
- bibliography-juegos-sistemas.bib
abstract: |
    Una idea ampliamente extendida
    sobre el sistema de representación proporcional de D'Hondt,
    es que trasvasar votos de un partido pequeño a uno grande
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

---

# Introducción

El sistema de representación proporcional de D’Hondt [@dhondt1878; @sartori2005],
también conocido como _reparto por cocientes decrecientes_,
se emplea habitualmente en España para asignar escaños
en elecciones generales, autonómicas, europeas y municipales [@congreso1985loreg].
El reparto se realiza independientemente dentro de cada circunscripción electoral,
transformando los votos obtenidos por cada candidatura en escaños,
según un orden determinado por sus cocientes de reparto.

Este artículo no busca evaluar la idoneidad del sistema
ni proponer alternativas, como ya hacen otros autores
[@medzihorsky2019rethinking; @lardeyret1991problem; @bochsler2010gains],
sino ofrecer herramientas para **comprender su lógica interna**,
y, de este modo, evaluar cómo distintas decisiones
afectan al reparto de escaños.
Estas herramientas pueden ser útiles tanto para el diseño de campañas,
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
tendría aplicación en otros dilemas y contextos
donde las mecánicas del sistema D'Hondt tengan influencia.


## Lógica de bloque

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
hace competir a las candidaturas por **bases electorales compartidas**,
y estimula, especialmente en períodos electorales,
la **lógica partidista**, que prioriza la captación de poder electoral
por parte de cada candidatura por separado.

Más paradójico aún es que, desde una **lógica partidista**,
algunas candidaturas apelen a la **lógica de bloques**
para captar bases electorales
que, en realidad, son más cercanas
a otras opciones dentro del mismo bloque.

En contextos de **lógica de bloques**,
emergen diversos dilemas estratégicos.
El dilema en el que nos centramos en este artículo,
es si la **concentración del voto** en las candidaturas más fuertes
beneficia al bloque en su conjunto.

Cabe diferenciarlo de otro dilema similar,
igualmente interesante, pero que no abordaremos en este artículo,
que es la conveniencia de los **pactos preelectorales**
para maximizar el impacto del bloque.
El de la concentración del voto es un dilema que,
principalmente, afronta el electorado en el momento de votar.
El segundo, lo afrontan las candidaturas
antes de entrar en la contienda electoral.

## El dilema de la concentración

En contextos de lógica de bloques, es un fenómeno recurrente
apelar al **voto estratégico** o **voto útil**,
buscando la **concentración del voto**
hacia la formación mayoritaria de un bloque.
El supuesto detrás de esta idea es que los partidos grandes,
como el sistema electoral les favorece,
transforman más eficientemente los votos en escaños.

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

Si bien sería muy ingenuo exigir rigor científico a los políticos en campaña,
el argumento está profundamente interiorizado en la sociedad.
Periodistas y analistas lo incorporan en sus análisis y divulgaciones,
lo que contribuye a su perpetuación [@tezanos_2019; @lavanguardia2023grandes; @elmundo2023calculo].

Cabe reconocer que algunos artículos han empezado a cuestionar este supuesto
[@eldiario_2023; @confidencial_2023; @infolibre_2023].
Matizan la idoneidad de su aplicación en algunos casos,
o justifican la divergencia inexperada
con el hecho de que el sistema no siempre
sigue un comportamiento lineal.

Durante mucho tiempo, en la literatura científica,
también se ha dado por supuesto que D'Hondt favorecía a los mayoritarios
[@norris1997; @sutherland2003].
Pero, recientemente, [@medzihorsky2019rethinking]
pone en cuestión, con argumentos analíticos y empíricos,
que D'Hondt genere un beneficio desproporcionado a los grandes.

A esto, se suman casos recientes en diversas convocatorias en España,
donde un trasvase de voto hacia el mayoritario,
no solo no ha tenido el efecto esperado,
sino que han resultado en un peor resultado para el bloque en conjunto[^1].

A la luz de estos precedentes, se evidencia la necesidad
de realizar un análisis más sistemático sobre este asunto.

Este artículo no pone en duda que el sistema electoral en conjunto
beneficie a los mayoritario, es así,
lo que que se examina es si tal beneficio puede ser explotable
para que el voto personal sea más poderoso.

[^1]: Ejemplo real: Elecciones generales de xxx de 20xx en Barcelona.
    Muchos votantes de ZURDOS respondieron al llamamiento de PROGRES
    para concentrar el voto y frenar el ascenso de la extrema derecha.
    Así, ZURDOS se quedó a pocos votos de conseguir un escaño más,
    mientras que a PROGRES les sobraron muchos votos que no se tradujeron en representación.
    El último escaño se lo llevó VOX,
    pero hubiera ido al bloque de izquierda si algunos de los votos trasvasados
    a PROGRES se hubieran mantenido en ZURDOS.


## Una perspectiva habilitadora del sistema D'Hondt

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




