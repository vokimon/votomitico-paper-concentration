### Fase 1: Simulación y Verificación de la Hipótesis Inicial

#### Objetivo

Verificar experimentalmente la hipótesis inicial y explorar cómo los trasvases de votos entre dos partidos de un mismo bloque afectan al resultado conjunto.

#### Hipótesis Inicial

Nuestra hipótesis inicial era que,
a medida que se aumentaba la concentración de votos en el partido mayoritario de un bloque,
los escaños conjuntos (de ambos partidos) aumentarían de forma creciente.
Esta hipótesis concordaba con el consenso ampliamente aceptado de que,
cuanto mayor fuera la candidatura,
más se beneficiaría de los votos transferidos, favoreciendo al conjunto.

#### Procedimiento

Para verificar esta hipótesis,
utilizamos un simulador, desarrollado específicamente,
para realizar trasvases de votos entre partidos.
En lugar de centrarnos en casos específicos,
se realizaron trasvases de votos entre pares arbitrarios de partidos dentro de un mismo bloque,
con el fin de generar variabilidad en los resultados y descubrir patrones generales.
Se emplearon datos reales de elecciones generales y autonómicas
en la circunscripción de Barcelona
desde 1977, las primeras elecciones democráticas,
hasta 2011.
También se usaron datos sintéticos, con el fin de tener escenarios más controlados.

#### Observaciones Iniciales

Al inicio, esperábamos que, conforme se concentrara más apoyo en el partido mayoritario,
los escaños conjuntos de ambos partidos aumentaran cada vez más.
Sin embargo, la simulación nos mostró un comportamiento inesperado.
Cuando aumentaba, lo hacía en un único escaño, que, conforme trasvasábamos más votos,
se perdía y después volvía a ganar de forma cíclica.

#### Patrones Observados

Segun el escenario, se detectaron dos patrones diferenciados durante las simulaciones:

1. **Patrón Cíclico con Ganancia y Pérdida de un Escaño Conjunto**:  
   En la mayoría de casos, los escaños conjuntos alternaban un escaño de ganancia con otro de pérdida en ciclos a medida que progresaba el trasvase.
   Ese escaño se tomaba y cedia a una tercera candidatura que siempre era la misma.

2. **Patrón Cíclico sin Variación en los Escaños Conjuntos**:  
   En otro conjunto de casos menos común, 
   el trasvase de votos se producía de forma cíclica y directa
   entre los dos partidos del bloque
   sin provocar ganancia o pérdida de escaños conjuntos.

#### Conclusiones

Ambos patrones mostraron un comportamiento que contradecía la expectativa inicial de que,
a medida que se concentraba el voto en el partido mayoritario,
los escaños conjuntos aumentaran de forma continua.
En cambio, se encontraron fluctuaciones cíclicas en los escaños.

Al trabajar con los casos sintéticos, descubrimos que lo que determinaba
qué patrón se seguía era la relación de los restos combinados de la situación inicial.
Si añadiamos o quitabamos a una candidatura los votos correspondientes al precio de escaño,
el patrón se mantenía igual, mientras que si haciamos lo mismo con cantidades de votos inferiores,
el patrón cambiaba.

La detección de estos patrones, sin una explicación clara,
motivó el desarrollo de la siguiente fase de la investigación,
donde exploramos en mayor detalle los factores subyacentes
que influían en este comportamiento.

