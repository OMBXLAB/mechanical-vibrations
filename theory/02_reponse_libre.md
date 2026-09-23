# Réponse libre et identification de l'amortissement

On considère l'oscillateur linéaire à un degré de liberté :

    m x¨(t) + c x˙(t) + k x(t) = 0

avec :

    ωn = √(k/m)
    ccrit = 2√(km)
    ζ = c/ccrit

## 1. Régime sous-amorti

Pour 0 ≤ ζ < 1 :

    ωd = ωn√(1-ζ²)

et

    x(t) = exp(-ζωn t) [A cos(ωd t) + B sin(ωd t)]

La réponse oscille à la pulsation amortie ωd tandis que son enveloppe décroît exponentiellement.

## 2. Amortissement critique

Pour ζ = 1 :

    x(t) = (A + Bt) exp(-ωn t)

C'est la limite entre comportement oscillatoire et apériodique.

## 3. Régime sur-amorti

Pour ζ > 1, l'équation caractéristique possède deux racines réelles négatives. La réponse est une somme de deux exponentielles décroissantes.

## 4. Décrément logarithmique

Dans le régime sous-amorti, si Ai et Ai+1 désignent deux maxima successifs de même signe :

    δ = ln(Ai/Ai+1)

et

    δ = 2πζ / √(1-ζ²)

On peut donc identifier le taux d'amortissement :

    ζ = δ / √(4π² + δ²)

Cette méthode relie directement une mesure temporelle de décroissance à un paramètre du modèle dynamique.
