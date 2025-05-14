# Análisis con un modelo general

El modelo previo de trasvases de votos
ha demostrado ser útil para explicar
los resultados empíricos observados en simulaciones.

Sin embargo, al tratarse de una aproximación,
no ofrece garantías sobre su aplicabilidad en todos los casos.
Asume que los trasvases no alteran el precio,
y conocemos casos en los que esto no se da.

Este capítulo presenta un modelo general,
aplicable a cualquier escenario de trasvase entre dos candidaturas,
incluidos aquellos en los que el precio de corte se ve alterado.

## Objetivo

Para construir el nuevo modelo de aplicación general,
se seguirán los siguientes pasos:

1. Delimitar el espacio de escenarios posibles solo a aquellos que son alcanzables mediante trasvases de votos.
2. Identificar los parámetros mínimos del espacio que determinan como cambian los resultados al movernos en él.
3. Estudiar la evolución del precio a lo largo del espacio y sus consecuencias en el reparto de escaños.
4. Incorporar la incertidumbre a través de un análisis probabilístico.
5. Valorar las oportunidades de voto estratégico a partir de los resultados obtenidos.

## El Espacio de Trasvases

Dado un escenario inicial,
concreto pero incierto,
consideramos el conjunto de escenarios
resultantes de hacer
trasvases de votos
entre las candidaturas A y B,
manteniendo inalterados
los votos del resto de candidaturas.

El espacio de trasvases resultante,
representado en la figura \ref{fig:transferspace},
conforma un segmento unidimensional de escenarios,
que va desde una asignación total de los votos del bloque a A
hasta una asignación total a B.

![
Espacio de trasvases y evolución de los cocientes.
](figures/transferspace.pdf){#fig:transferspace}

Si llamamos $V_{ab}$ a la suma de votos de A y B en el escenario inicial,
los votos de A, $V_a$, crecen linealmente, a lo largo del espacio,
de 0 a $V_{ab}$,
y los de B, $V_b$, decrecen de forma complementaria, de $V_{ab}$ a 0.

Los cocientes de A, $C_a^j = V_a / j$, en azul en la figura,
y de B, $C_b^k = V_b / k$, en rojo,
evolucionan proporcionalmente a sus respectivos votos.

Por otro lado, los cocientes de las demás candidaturas,
como los cocientes $P_c$ y $P_d$, se mantienen constantes.
Solo representamos esos dos, porque,
como se explica más adelante,
serán los únicos relevantes para el análisis.

Un cruce de dos cocientes en la gráfica
indica un cambio en su orden relativo.
Cuando uno de los cocientes implicados en el cruce
es el que marcaba el precio de corte,
tras el cruce, el otro pasa a ocupar esa posición,
y, si el nuevo cociente de corte no tenia escaño
se lo arrebatará al anterior cociente de corte.

Si el cociente que marca el precio de corte se cruza con otro,
este último lo reemplaza en esa posición,
y si no tenía escaño, se lo quitará.

En la figura \ref{fig:transferspace},
se observa que los cocientes de A y B se cruzan
en los puntos $C_a^j = C_b^k = \frac{V_{ab}}{j + k}$,
para cada par $k$ y $j$.
Los que se producen en el mismo valor,
digamos, en $\frac{V_{ab}}{k}$,
dividen el espacio en $k$ segmentos iguales.

## Escenario de concentración plena

Para caracterizar el especio de trasvases,
usaremos los escenarios en los extremos,
es decir, aquellos de concentración total
en uno de los dos partidos.
Debido a la simetría complementaria del espacio de trasvases,
podemos escoger uno u otro extremo.
Concretamos el desarrollo utilizando el escenario en el que concentramos
todo el voto en B ($V_a = 0$, $V_b = V_{ab}$).

El reparto nos dará que:

$$
    V_b = V_{ab} = E_{ab} P_{max} + R_{ab}
$$

Donde:

- $P_{max}$ es el precio de corte en este escenario
- $E_{ab}$ son los escaños asignados en este escenario
- $R_{ab}$ son los restos que quedan en este escenario

Dado que B tiene $E_{ab}$ escaños,
el último cociente asignado de B habrá sido $\frac{V_{ab}}{E_{ab}}$.
Para poder entrar, ese cociente debería ser mayor o igual que $P_{max}$.
De hecho, podría ser $\frac{V_{ab}}{E_{ab}}$ el que fijara $P_{max}$ o
el último cociente de una tercera candidatura C, que llamaremos $P_c$.

Pasa lo mismo con el precio mínimo $P_{min}$: 
lo puede fijar el primer cociente no escogido de B, 
$\frac{V_{ab}}{E_{ab} + 1}$, o el primer cociente no escogido 
de alguna tercera candidatura D que llamaremos $P_d$.

$$
\frac{V_{ab}}{E_{ab}} \geq P_{max} \geq P_{min} \geq \frac{V_{ab}}{E_{ab} + 1}
$$

## Evolución del precio

![
La evolución del precio de corte en el espacio de trasvases.
El precio, representado como un borde verde,
resigue diferentes cocientes según varia la concentración en A o en B.
Se diferencian varias zonas:
Las mesetas en violeta donde el precio lo determina Pmax.
Los valles en amarillo donde el precio lo determina Pmin.
Las pendientes donde lo determinan sucesivos cocientes de A (crecientes en azul)
y B (decrecientes en rojo).
](figures/transferspace-detail.pdf){#fig:transferspace-detail}

![
Ejemplo en el que _Pmax_ y _Pmin_ estan fijados por _Vab/Eab_ y _Vab/(Eab+1)_.
Que fije _Pmin_ es necesario para que el trasvase no suponga cesiones a terceros.
](figures/transferspace-unlimited.pdf){#fig:transferspace-unlimited}

En el modelo aproximado, se asumió que,
después de un trasvase, el precio quedaba fijo.
Ahora, con el nuevo marco de los espacios de trasvases,
procederemos a analizar cómo evoluciona el precio
y cómo afecta al reparto de escaños.
Usaremos los **cruces entre cocientes** para identificar
los momentos en los que el orden de los cocientes cambia
y sus impactos en el precio y en la asignación de escaños.

Hay cuatro puntos clave, que después extenderemos a todo el espacio,  
apoyándonos en el _teorema de la repetición de resultados_  
(ver §\ref{teorema-repeticion-resultados}).

1. **Escenario de concentración total en B**  
    Cuando $V_a = 0$, el precio comienza, 
    marcado por el cociente $P_{max}$,
    representado en violeta en la figura \ref{fig:transferspace-detail}.

2. **Cruce con el cociente $\frac{V_b}{E_{ab}}$ de B**  
    Este cociente está representado en rojo en la figura,
    y su cruce se produce cuando $V_a = R_{ab}$,
    es decir, cuando se agotan los restos de B.
    Como este cociente ya tiene un escaño asignado,
    no hay cambio en el reparto de escaños.
    Solo cambia el cociente que marca el precio.

3. **Cruce con $P_{\min}$**  
    Este cociente está marcado en amarillo en la figura
    y su cruce se produce en $V_a = V_{ab} - E_{ab} P_{\min}$.
    Este cruce implica un traspaso de escaño de B a D.

4. **Cruce con el cociente $\frac{V_a}{1}$**  
    Este cociente está marcado en azul en la figura
    y su cruce se produce en $V_a = P_{\min}$.
    Este cruce implica un traspaso de escaño de D a A.

Esta descripción es compatible con el caso
en que $P_{min} < \frac{V_{ab}}{E_{ab}+1}$,
y por tanto $P_{\min} = \frac{V_{ab}}{E_{ab}+1}$.
En este caso, el tercer punto y el cuarto coinciden en un único cruce,
como pasa en la figura \ref{fig:transferspace-direct},
y se produce una transferencia directa de escaño de B a A,
sin pasar por D.

Extendiendo estos puntos según indica el
_teorema de repetición de resultados_,
los puntos 1 y 2 se repiten cada $P_{max}$
mientras que los puntos 3 y 4 se repiten cada $P_{min}$.
Resulta en esta fórmula general, para el precio:

$$
P(V_a) = 
\begin{cases} 
P_{max}
& \text{si } V_a \in \left[
k P_{max}, R_{ab} +  k P_{max} \right],
\quad k \in \{0, 1, \dots, E_{ab}\} \\
\frac{V_{ab} - V_a}{E_{ab} - k}
& \text{si } V_a \in \left[
R_{ab} +  k P_{max}, V_{ab} - E_{ab} P_{min} + k P_{min}  \right],
\quad k \in \{0, 1, \dots, E_{ab}-1\} \\
P_{min}
& \text{si } V_a \in \left[
V_{ab} - E_{ab} P_{min} + k P_{min},  P_{min} + k P_{min}
\right],
\quad k \in \{0, 1, \dots, E_{ab}-1\} \\
\frac{V_a}{k+1}
& \text{si } V_a \in \left[
P_{min} + k P_{min}, P_{max} + k P_{max}
\right],
\quad k \in \{0, 1, \dots, E_{ab}-1 \}
\end{cases}
$$

Lo interesante son las zonas donde $P_{min}$ marca el precio.
Estas zonas es donde el escaño en disputa se lo lleva D, un tercero,
y el bloque A-B lo pierde.

Esto divide el espacio de trasvases
como ilustra la figura \ref{fig:transferspace-seat-leak},
en dos tipos de zonas:
Zonas donde el resultado conjunto es pleno,
separadas por zonas,
donde una tercera formación les resta un escaño.

El tamaño de las zonas de resultado pleno es:

$$
    V_{ab} - E_{ab} P_{min}
$$

Y, el de las zonas de resultado menor:

$$
    (E_{ab}+1) P_{min} - V_{ab}
$$

![
Escenario de trasvase con cesiones a un tercero.
Se da cuando Pmin supera Vab/(Eab+1).
Para pasar de una candidatura a otra,
el escaño pasa antes por un tercero.
Se alternan zonas de resultado pleno con zonas
en las que se pierde un escaño.
](figures/transferspace-seat-leak.pdf){#fig:transferspace-seat-leak}

Esto concuerda con el patrón cíclico observado empíricamente.
El otro patrón observado empíricamente,
sin cesión a un tercero, se da cuando
$P_{min} = \frac{V_{ab}}{E_{ab}+1}$.
Es decir, cuando juntando todos los votos
de A y B, el primer cociente excluido
es el de esta unión.

![
Escenario de trasvase directo entre A y B,
cuando Pmin es Vab/(Eab+1).
No es un espacio necesariamente favorable.
Quiere decir que aunque sumen todos los restos,
siempre quedarían a las puertas del siguiente escaño.
](figures/transferspace-direct.pdf){#fig:transferspace-direct}


## Análisis probabilístico

**OUTLINE**

- Solo dos resultados conjuntos posibles, $E_{ab}$ y $E_{ab}-1$
- Cambio: Del estado inicial al post cambio
    - Ganancia: estar en $E_{ab}-1$ y pasar a $E_{ab}$
    - Perdida: estar en $E_{ab}$ y pasar a $E_{ab}-1$
    - Status quo:  $E_{ab} \rightarrow E_{ab}$ o $E_{ab}-1 \rightarrow E_{ab}-1$

## Discusión

**TODO**


