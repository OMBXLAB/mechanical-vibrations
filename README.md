# Vibrations mécaniques

Ce dépôt rassemble des développements pédagogiques et numériques autour de la **dynamique vibratoire des systèmes mécaniques**.

L'objectif est de partir des équations du mouvement, de construire les modèles analytiques, puis de les confronter progressivement à des calculs numériques en Python.

## Contenu du projet

- oscillateur à **1 degré de liberté (1 DDL)** ;
- réponse libre avec amortissement visqueux ;
- régimes sous-amorti, critique et sur-amorti ;
- décrément logarithmique et identification de l'amortissement ;
- réponse harmonique forcée, amplification dynamique, phase et résonance ;
- vibrations en torsion ;
- excitation par mécanisme bielle-manivelle ;
- systèmes à **plusieurs degrés de liberté** ;
- matrices de masse, raideur et amortissement ;
- valeurs propres, fréquences propres et formes modales ;
- coordonnées modales et matrices généralisées ;
- amortissement modal / Rayleigh ;
- réponses libre et forcée des systèmes multi-DDL.

## Équation générale — 1 DDL

Pour un système masse–ressort–amortisseur :

    m x¨(t) + c x˙(t) + k x(t) = f(t)

avec m la masse, c le coefficient d'amortissement visqueux, k la raideur et f(t) l'excitation extérieure.

    ωn = √(k/m)
    ζ = c / (2√(km))
    ωd = ωn √(1 - ζ²)   pour 0 < ζ < 1

## Systèmes multi-DDL

    [M] x¨(t) + [C] x˙(t) + [K] x(t) = f(t)

Le problème modal associé s'écrit :

    ([K] - λ[M]) φ = 0
    λr = ωr²

Les vecteurs propres définissent les formes modales.

## Organisation

    mechanical-vibrations/
    ├── README.md
    ├── theory/
    ├── src/
    ├── examples/
    ├── figures/
    └── requirements.txt

## Cas d'étude

Les documents de travail couvrent notamment la modélisation d'un système amorti, l'identification des paramètres à partir d'une réponse libre, la résonance en torsion, l'excitation par bielle-manivelle et l'analyse modale de systèmes à 2 et 3 DDL.

## Objectif numérique

Les prochaines versions intégreront des scripts Python pour calculer les réponses temporelles, visualiser l'influence de l'amortissement, tracer les réponses fréquentielles, déterminer fréquences propres et formes modales, reconstruire les réponses physiques et comparer calculs analytiques et numériques.

---

Projet personnel de mécanique — **OMBXLAB**
