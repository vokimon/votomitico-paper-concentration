---
lang: es
author: David García Garzón
# {.unnumbered}
title: Efectos electorales de trasvases de voto entre partidos con base electoral común
classoption:
#- twocolumn
numbersections: true
link-citations: true
link-bibliography: true
header-includes:
  - \usepackage{draftwatermark}
bibliography:
- bibliography.bib
- bibliography-vote-concentration-calls.bib
- bibliography-divulgacion-bulo.bib
- bibliography-juegos-sistemas.bib
- bibliography-encuestas.bib
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

!include intro.md

!include metodologia.md

!include analisis-empirico.md

!include algebra-dhondt.md

!include modelo-aproximado.md

!include modelo-general.md

# Condiciones que habilitan el voto estratégico

**OUTLINE**

- En general, la incertidumbre sobre los restos no deja espacio para el voto estrategico
- En casos concretos hay certidumbre en los restos y podemos armarlo
    - Partidos muy pequeños
    - Pocos escaños a repartir
    - Muchos escaños a repartir con umbral electoral
- En ninguno de estos casos el criterio es votar al más grande,
    sino que depende de la situación esperada

# Discusión

**OUTLINE**

- Contraste de los resultados con la literatura existente
- Refuerza el mito: Sesgo de disponibilidad sumando restos a posteriori:
    - Tambien es un sesgo de retrospección
    - Sobreestimamos la probabilidad de un evento porque
      ejemplos recientes, notorios o emocionalmente impactantes
      están fácilmente disponibles en nuestra memoria
    - En este caso cuando vemos a posteriori
      que un trasvase podría haber supuesto un escaño más.
    - A priori, ese mismo trasvase podria haber generado una perdida
- Refuerza el mito: El sistema beneficia a mayoritarios
    - Metricas de injusticia
        - Relacion escaños/votos
        - Relacion restos/votos
    - Impacto del voto: restos absolutos
- Refuerza el mito: Restos relativos a los votos o votos relativos a representación
    - Diluye la percepción de fuerza de tu voto
    - Argumento para denunciar injusticia del sistema
        - No válido para la utilidad del voto
    - Elementos del sistema electoral que perjudican los minoritarios
        - Umbral electoral -> solo aplica en pocas circunscripciones en autonómicas
            - Según la situación puede ser más util votar al pequeño para que llegue al umbral
        - Escasez de escaños
            - Los restos son una parte mayor de los votos
            - Hondt es tan proporcional como votos se dediquen a escaños
            - Se nota mas la desproporcion con Hamilton
            - En voto estrategico: Es más importante donde esté cada formación que si es grande o pequeño
        - Multiples circunscripciones
            - Aqui no tenemos control porque los escaños no se agregan entre distritos
            - Ni para grandes ni para chicos
        - Reparto de D'Hondt

# Conclusiones

**OUTLINE**

- Aportaciones: Resultados para las transferencia intra-bloque
    - Impacto: Mejor voto estrategico. Sin mitos, con evidencia.
    - Necesidad de difusión de los resultados
- Aportaciones: Nuevas herramientas para estudiar D'Hondt
    - Impacto: dirimir otros mitos/dilemas: pactos, umbral, voto en blanco...

!include derivaciones.md

# Referencias {.unnumbered }

::: {#refs}
:::

\newpage
\thispagestyle{empty}

!include todo.md

!include article-outlines.md


