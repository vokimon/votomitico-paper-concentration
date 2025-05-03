# Análisis con un modelo general

## Objetivo

Durante esta fase,
se desarrollará un modelo
para los trasvases de votos entre candidaturas
de aplicación general
sin la aproximación del anterior modelo
que consideraba el precio de corte constante
durante los trasvases.

Para ello, limitaremos el espacio inabarcable de escenarios,
a un espacio limitado de escenarios
que solo incluya aquellos a los que se pueda llegar,
desde un un escenario inicial de referencia,
haciendo trasvases de votos entre dos candidaturas A y B.
Caracterizaremos el espacio parametrizándolo
a partir de un escenario singular,
y despues estudiaremos cómo evoluciona
el resultado según nos movemos en ese espacio.
Finalmente, se establecerá un modelo probabilístico
para acabar determinando en qué términos un trasvase
puede considerarse estratégicamente positivo, negativo o neutro.

## Espacio de trasvases

Dado un escenario inicial, incierto pero fijo,
consideremos las candidaturas A y B entre las que trasvasar votos.
Consideremos la familia de escenarios alternativos,
desde un trasvase total a A a un trasvase total a B
conformando un espacio contiguo 1D o un segmento de escenarios.

![
Espacio de trasvases y evolución de los cocientes.
Los cocientes de A crecen, los de B decrecen,
y los del resto de candidaturas, por ejemplo,
_Pmax_ y _Pmin_, son constantes.
Las líneas grises permiten comprovar que los cocientes
_Va/j_ y _Vb/k_ coinciden en _Vab/(k+j)_.
Esos puntos de intersección con los cocientes
dividen la línea Vab/k en k segmentos iguales.
](figures/transferspace.pdf){#fig:transferspace}

En este espacio, representado en la figura \ref{fig:transferspace},
los votos al resto de candidaturas se mantienen constantes
y, por tanto, sus coeficientes.
Los votos de A, $V_a$ crecen linealmente desde 0 a $V_{ab} = V_a^0 +V_b^0$,
siendo $V_a^0$ y $V_b^0$ los votos en el escenario inicial.
Los votos de B decrecen linealmente de forma complementaria, de $V_{ab}$ a 0.
Los coeficientes $C_a^j$ evolucionan proporcionalmente a $V_a$,
y lo mismo pasa con $C_b^j$ con $V_b$.

Remarcamos varias cosas:

- Primero la simetría: Lo que le pasa a A en un lado le pasa a B en el otro.
- Segundo, las relaciones entre cocientes:
  Los coeficientes $C_a^j = Va/j$ y  $C_b^k = Vb/k$
  coinciden en $V_{ab} \over k + j$.
  Estos puntos de cruce son importantes porque son los puntos
  donde los coeficientes cambian de orden.
  Para $V_{ab}/k$, esos puntos de cruce de los coeficientes
  dividen el espacio de trasvases en $k$ secciones iguales.


## Escenario de concentración plena

Los escenarios en los extremos del espacio nos van a servir
para parametrizar el espacio entero.
Son los de concentración total en uno de los dos partidos.
Por simetría, ambos son equivalentes, pero para este desarrollo
nos centraremos en el escenario en el que concentramos todo el voto en B
($V_a=0$, $V_b = V_{ab}$).

El reparto nos dará que:

$$
    V_b = V_{ab} = E_{ab} P_{max} + R_{ab}
$$

Donde

- $P_{max}$ es el precio de corte en este escenario
- $E_{ab}$ son los escaños asignados en este escenario
- $R_{ab}$ los restos que quedan en este escenario

Dado que B tiene $E_{ab}$ escaños,
el último cociente asignado de B habrá sido $V_{ab} \over E_{ab}$.
Para poder entrar, ese cociente debería ser mayor o igual que $P_{max}$.
De hecho, podría ser $V_{ab} \over E_{ab}$ el que fijara $P_{max}$ o
el último cociente de una tercera candidatura C y que llamaremos $P_c$.

Pasa lo mismo con el precio mínimo $P_{min}$,
lo puede fijar el primer cociente no escogido de B,
$V_{ab} \over E_{ab} +1$, o el primer cociente no escogido
de alguna tercera candidatura D que llamaremos $P_d$.

$$
{V_{ab} \over E_{ab}} >= P_{max} >= P_{min} >= {V_{ab} \over E_{ab} +1}
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

En el modelo aproximado, supusimos que,
después de un trasvase, el precio quedaba fijo.
Comprobemos qué evolución tiene y cómo afecta al reparto de escaños.

Partiendo de la situación con el voto concentrado en B,
a medida que vamos trasvasando votos a A,
el precio sigue siendo $P_{max}$ hasta que
al perder votos, el coeficiente $V_b \over E_{ab}$ pasa por debajo.
Esto sucede cuando $V_a = R_{ab}$.

Si el precio es $P_{max}$  en el intérvalo $[0, R_{ab}]$,
por el teorema de los precios repetidos,
se repetirá a intérvalos $P_{max}$,
o más formalmente:

$$
P(V_a) = P_{max} \quad \text{si} \quad \exists k \in \mathbb{N},\ 
0 \leq k \leq E_{ab},\ 
V_a \in [k P_{max},\ k P_{max} + R_{ab}]
$$

A partir de ese punto, $V_a = kP_{max} + R_{ab}$,
el precio lo marca el cociente decreciente de B correspondiente,
en rojo en la figura \ref{fig:transferspace-detail}.
Esto no supone un cambio en el número de escaños,
solo un cambio en el orden de asignación de los dos últimos escaños
que siguen siendo de C y B.

Aquí pueden pasar dos cosas, dependiendo de qué sea más alto,
$P_{min}$ o el cociente $V_{ab} \over E_{ab} + 1$.

Si es más alto el cociente $V_{ab} \over E_{ab} + 1$,
cuando el precio llega a ese valor,
B pierde el escaño a favor del siguiente cociente de A,
$V_a \over k + 1$, que pasa a tener representación.
Lo que tenemos es un traspaso directo del escaño entre B y A.
Al ser directo, no habría un cambio en la representación conjunta.
Ese intercambio de escaño se produciría en $V_a = (k+1) {V_{ab} \over E_{ab} +1}$
lo que divide el espacio de trasvases en $E_{ab} + 1$ zonas
de igual tamaño, en las que las candidaturas consiguen complementariamente
0, 1, ..., $E_{ab}$ escaños, como ejemplifica la figura \ref{fig:transferspace-direct}.

![
Escenario de trasvase directo entre A y B,
cuando Pmin no supera Vab/(Eab+1)
](figures/transferspace-direct.pdf){#fig:transferspace-direct}


Si, en cambio, $P_{min} > { V_{ab} \over E_{ab} +1 }$,
es este coeficiente el que toma el relevo como precio de corte
y la candidatura a la que pertenezca le arrebatará el escaño
al bloque A-B hasta que el cociente creciente de A
supere ese precio.

Encontrando la intersección de las curbas y aplicando el teorema de repetición,
obtenemos los intérvalos donde precio es $P_{min} y,
más importante, el resultado conjunto pierde un escaño.

$$
P(V_a) = P_{min} \quad \text{si} \quad \exists k \in \mathbb{N},\ 
0 \leq k \leq E_{ab},\ 
V_a \in [V_{ab} - E_{ab} P_{min} + k P_{min},\ P_{min} + k P_{min}]
$$

Esto nos divide el espació,
como muestra la figura \ref{fig:transferspace-seat-leak},
en $E_{ab}+1$ zonas
de tamaño $V_{ab} - E_{ab} P_{min}$.
en las que como antes la representación es máxima,
separadas por $E_{ab}$ zonas
de tamaño $(E_{ab}+1) P_{min} - V_{ab}$
en las que otra candidatura se lleva el escaño.

![
Escenario de trasvase con cesiones a un tercero.
Se da cuando Pmin supera Vab/(Eab+1).
Para pasar de una candidatura a otra,
el escaño pasa antes por un tercero.
Se alternan zonas de resultado pleno con zonas
en las que se pierde un escaño.
](figures/transferspace-seat-leak.pdf){#fig:transferspace-seat-leak}


## Análisis probabilístico

**OUTLINE**

- Solo dos resultados conjuntos posibles, $E_{ab}$ y $E_{ab}-1$
- Cambio: Del estado inicial al post cambio
    - Ganancia: estar en $E_{ab}-1$ y pasar a $E_{ab}$
    - Perdida: estar en $E_{ab}$ y pasar a $E_{ab}-1$
    - Status quo:  $E_{ab}$ -> $E_{ab}$ o $E_{ab}-1$ -> $E_{ab}-1$

## Discusión

**TODO**


