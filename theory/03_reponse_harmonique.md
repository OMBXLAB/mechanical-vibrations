# Réponse harmonique et résonance

Pour une excitation harmonique :

    f(t) = F0 cos(ωt)

l'équation du mouvement est :

    m x¨ + c x˙ + kx = F0 cos(ωt)

On introduit le rapport de fréquence :

    r = ω/ωn

La réponse permanente peut être décrite par son amplitude X et son déphasage φ.

## Facteur d'amplification dynamique

En normalisant l'amplitude par le déplacement statique F0/k :

    β = X/(F0/k)

on obtient :

    β(r) = 1 / √[(1-r²)² + (2ζr)²]

## Phase

    φ = atan2(2ζr, 1-r²)

L'utilisation de atan2 permet de conserver le quadrant physique du déphasage.

## Résonance

Pour le déplacement d'un système amorti, le maximum de β existe pour ζ < 1/√2 et se situe à :

    r_r = √(1-2ζ²)

donc :

    ωr = ωn√(1-2ζ²)

Lorsque l'amortissement est faible, ωr est proche de ωn et le pic d'amplification est marqué.
