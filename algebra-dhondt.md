# Marco algebraico para D'Hondt

## Objetivo

El objetivo de esta fase es
proporcionar una formulación algebraica del sistema D'Hondt
que facilite su análisis,
superando las limitaciones analíticas de la visión procedural.
Para ello, se propone una perspectiva diferente de este método de reparto,
que permite relacionar los parámetros involucrados y
comprender las dinámicas entre ellos,
sin ejecutar el algoritmo.

## Derivación algebraica

El algoritmo de reparto consta de dos partes:
La **generación de cocientes**
y la posterior **selección ordenada**
de los coeficientes[^coeficientes_entrelazados].

[^coeficientes_entrelazados]:
    Separamos estas dos partes para facilitar la conceptualización,
    pero, el algoritmo en su versión típica las entrelaza
    para minimizar el número de operaciones a realizar.

    No se calcula un determinado cociente
    hasta que no se ha seleccionado el anterior de la misma candidatura,
    aprovechando que:

    $$
    { V_i \over j } > { V_i \over j + 1}
    $$

    Son optimizaciones que tenían mucho sentido
    cuando las divisiones se hacían a mano.
    Consideramos que esta versión, menos óptima pero más simple,
    deja más claro el propósito del algoritmo.

La **generación de cocientes** calcula,
para cada candidatura $i$, los cocientes:

$$
    C^j_i = {V_i \over j}
    \quad , \quad \forall{ j \in [1..E] } \quad \forall{ i \in [1..K] }
$$

Donde:

- $E$ es el número de escaños disponibles
- $K$ es el número de candidaturas
- $V_i$ son los votos que obtuvo la candidatura $i$

La **selección ordenada** ordena los coeficientes
y escoge, de mayor a menor, tantos como escaños disponibles $E$.
Una candidatura obtendrá tantos escaños
como cocientes derivados de sus votos se hayan escogido.

¿Qué significan estos coeficientes?
Pensemos el reparto como un intercambio de escaños por votos.
Estableceríamos un precio en votos por cada escaño.
Con esa perspectiva, se puede entender el coeficiente $V_i / j$
como el precio máximo con el cual
la candidatura $i$ podría conseguir $j$ escaños,
como ilustra la figura \ref{seat-costs}.


![Interpretando el significado de los coeficientes:
Con _Vi_ votos, si el precio fuera _Vi/3_,
la candidatura _i_ podria comprar 3 escaños.
Si el precio fuera algo superior,
no tendriá votos suficientes para un tercero
y se quedaría con 2.
](figures/seat-costs.pdf){#seat-costs}

Cuando seleccionamos estos coeficientes, de mayor a menor,
lo que estamos haciendo es bajar el precio de forma controlada,
permitiendo un escaño más con cada coeficiente,
hasta que todos los escaños disponibles se han repartido.
Podemos considerarlo como una **subasta a la baja**.

El último cociente escogido, fija **precio de corte** ($P_c$).
Este parámetro es clave
porque condensa el resultado del algoritmo en un solo valor.
Permite calcular, sin volver a ejecutar el algoritmo,
el resultado, es decir, los escaños de cada candidatura ($E_i$).

$$
Ei = \left\lfloor{ Vi \over Pc } \right\rfloor   \quad , \quad \forall{i}
$$

O, expresado de otra manera:

$$ V_i = E_i \cdot P_c + R_i   \quad , \quad \forall{i} $$ 

![
Relación entre votos, escaños y restos tras aplicar el precio de corte.
_Vi = Ei  · Pc + Ri_](figures/seats-and-remainder.pdf){#seat-and-remainder}

Donde aparece un nuevo e importante parámetro interno:
los **restos** $Ri$,
que son los votos de la candidatura $i$ que podrían haber
ido a la abstención sin alterar el resultado.
Esto pone una distinción muy sólida de lo que significa voto útil o inútil.
Y tenemos que,
por construcción,
los restos de cada candidatura
están acotados por el precio de corte:

$$ 0 <= R_i < P_c    \quad , \quad \forall{i} $$

Otro parámetro significativo es el **primer cociente no escogido**, $P_d$.
Por definición, es el siguiente cociente menor que $P_c$.
Eso quiere decir que cualquier precio $P$ tal que $P_d < P <= P_c$,
no incorporaría ningún escaño más al resultado,
y, por lo tanto, repartiría los mismos escaños que $P_c$.

De forma general, un reparto por $P$ es exacto si
Se reparten justo los escaños disponibles,
y nadie tiene restos para un escaño de más.
Formalmente:

$$
    E = \sum_i{E_i} \quad \and \quad 0 <= R_i < P \forall i
$$

$P_c$ además asegura que haya una candidatura sin restos.
Formalmente:

$$
    \exist R_i ,  R_i = 0
$$


## Interpretación

### Observación: Los restos no alteran el resultado

Podemos modificar una situación dada
eliminando para una candidatura tantos votos como restos,
por ejemplo, enviándolos a la abstención.

$$
V_i' = V_i - R_i; \quad R_i' = 0
$$

El escenario resultante repartirá
los mismos escaños $E_i$ al mismo precio $P_c$
que el escenario original.



### Observación: Posibilidad de mejora sumando restos, con peros

Analizando un resultado concreto, es común observar que
si juntamos los restos de dos candidaturas,
se podría obtener un escaño adicional.
Eso es cierto, y sugiere que una redistribución
de los votos podría mejorar
el resultado conjunto.

Pero sería un sesgo retrospectivo
pensar que esta observacion se puede aplicar
más allá de un analisis a posteriori.
Si no conocemos la situación de partida,
no conocemos los restos disponibles.
Si se trasvasan menos votos,
que los que le faltan a los restos del receptor
para sumar un escaño, se podría no ganar el escaño adicional.
Si se trasvasan más votos
que los restos que dispone el emisor,
podría perder uno de los escaños de los que dispone.


### Observación: Resultados recurrentes a intervalos $P_c$

Dada una situación inicial con un **precio de corte** $P_c$ fijado,
si hacemos un trasvase entre dos candidaturas, emisora (A) y receptora (B),
de un número de votos igual a $P_c$,
obtenemos una situación equivalente en la que se mantiene:

- el mismo precio de corte $P_c$,
- los mismos restos de todas las candidaturas,
- los mismos escaños para las candidaturas que no sean A y B,
- la misma suma de escaños entre las candidaturas A y B,

Solo cambia la distribucion de esos escaños entre A y B
que A resta un escaño y B lo suma.

    Va' = Va - Pc = Pc Ea + Ra - Pc = Pc (Ea -1) + Ra => Ea' = Ea-1
    Vb' = Va + Pc = Pc Eb + Rb + Pc = Pc (Eb +1) + Rb => Eb' = Eb+1
 
Esto pasa en cualquier situación de partida
en la que haya suficientes votos para hacer tal trasvase.
Implica que los mismos resultados
van a estar repitiendose a medida que
transferimos más votos,
descartando, que haya escenarios mejores
con el voto concentrado, que no existan ya
con el voto no concentrado.

En este punto, aún no podríamos descartar
que, con mayor concentración de voto,
sea más probable acabar en una situación positiva,
que en una situación con poca concentración.

## Conclusiones

En resumen,
al abstraer el precio de corte $P_c$ como resultado del algoritmo
y establecer relaciones entre este valor y el resto de parámetros,
se pueden obtener conclusiones generales sobre la aplicación de D'Hondt
sin tener que ejecutar el algoritmo para cada caso.

Los votos a una candidatura se dividen
en votos que consiguen escaños y restos que no intervienen en el reparto.
Los restos de toda candidatura estan limitados por el precio de corte.

También hemos detectado varios trasvases que
mantienen algunas condiciones del reparto.
Por ejemplo, reducir para una candidatura
tantos votos como restos tiene o
trasvasar entre dos candidaturas
tantos votos como el precio de corte.

Los efectos de este ultimo tipo de trasvase, además,
demuestran que, por concentración de voto,
no vamos a obtener un resultado conjunto
que no sea posible obtener con menos concentración.
Esto no nos permite descartar, sin embargo, que,
cuando hay más concentración, los resultados
mejores sean más probables que cuando no la hay.

Por eso debemos establecer un modelo probabilistico,
que considere la probabilidad de estar en cada situación,
para considerar si un trasvase determinado,
tiene más probabilidad de llevaros a un peor o a un mejor
resultado conjunto.
Esto es lo que abordamos en la siguiente fase.


