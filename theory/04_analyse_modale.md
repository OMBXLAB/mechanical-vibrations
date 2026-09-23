# Introduction à l'analyse modale

Pour un système mécanique linéaire à plusieurs degrés de liberté :

    [M] x¨ + [C] x˙ + [K] x = f(t)

## Problème propre

Dans le système non amorti et sans excitation :

    [M] x¨ + [K] x = 0

La recherche d'une solution harmonique conduit à :

    ([K] - λ[M]) φ = 0
    λr = ωr²

Chaque valeur propre fournit une pulsation propre et chaque vecteur propre associé une forme modale.

## Coordonnées modales

En regroupant les vecteurs propres dans [Φ] et en posant x(t) = [Φ]q(t) :

    [M~] = [Φ]ᵀ[M][Φ]
    [K~] = [Φ]ᵀ[K][Φ]
    [C~] = [Φ]ᵀ[C][Φ]

Lorsque les hypothèses de découplage modal sont satisfaites, le système couplé en coordonnées physiques est transformé en équations modales indépendantes.

La suite du projet appliquera cette formulation aux systèmes à 2 et 3 DDL étudiés dans les exercices.
