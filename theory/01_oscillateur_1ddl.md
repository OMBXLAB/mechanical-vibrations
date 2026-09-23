# Bases théoriques — oscillateur à 1 DDL

## Équation du mouvement

    m x¨ + c x˙ + k x = f(t)

Sous forme normalisée :

    x¨ + 2ζωn x˙ + ωn² x = f(t)/m

avec ωn = √(k/m) et ζ = c/(2√(km)).

## Réponse libre

Pour f(t)=0, la nature de la réponse dépend de ζ.

### Sous-amorti — 0 < ζ < 1

    x(t) = A exp(-ζωn t) cos(ωd t - φ)
    ωd = ωn √(1-ζ²)

### Amortissement critique — ζ = 1

    x(t) = exp(-ωn t) (A + Bt)

### Sur-amorti — ζ > 1

La réponse est la combinaison de deux exponentielles décroissantes réelles.

## Décrément logarithmique

    δ = ln(Ai / Ai+1)
    δ = 2πζ / √(1-ζ²)

## Réponse harmonique

Avec r = ω/ωn :

    β(r) = 1 / √((1-r²)² + (2ζr)²)

Pour un amortissement suffisamment faible, la pulsation associée au maximum de réponse est :

    ωr = ωn √(1 - 2ζ²)

Ces relations constituent la base des développements numériques du dépôt.
