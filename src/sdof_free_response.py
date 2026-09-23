"""Oscillateur linéaire masse-ressort-amortisseur à un degré de liberté.

Grandeurs dynamiques principales, réponse libre analytique pour les trois
régimes d'amortissement et identification par décrément logarithmique.
"""

import numpy as np


def caracteristiques(m: float, c: float, k: float) -> tuple[float, float]:
    """Retourne (omega_n, zeta)."""
    if m <= 0 or k <= 0:
        raise ValueError("m et k doivent être strictement positifs.")
    if c < 0:
        raise ValueError("c doit être positif ou nul.")
    omega_n = np.sqrt(k / m)
    zeta = c / (2.0 * np.sqrt(k * m))
    return omega_n, zeta


def reponse_libre(t, m: float, c: float, k: float, x0: float, v0: float):
    """Réponse libre pour les régimes sous-amorti, critique et sur-amorti."""
    t = np.asarray(t, dtype=float)
    omega_n, zeta = caracteristiques(m, c, k)
    tol = 1e-10

    if zeta < 1.0 - tol:
        omega_d = omega_n * np.sqrt(1.0 - zeta**2)
        a = x0
        b = (v0 + zeta * omega_n * x0) / omega_d
        return np.exp(-zeta * omega_n * t) * (
            a * np.cos(omega_d * t) + b * np.sin(omega_d * t)
        )

    if abs(zeta - 1.0) <= tol:
        a = x0
        b = v0 + omega_n * x0
        return (a + b * t) * np.exp(-omega_n * t)

    racine = np.sqrt(zeta**2 - 1.0)
    r1 = -omega_n * (zeta - racine)
    r2 = -omega_n * (zeta + racine)
    a = (v0 - r2 * x0) / (r1 - r2)
    b = x0 - a
    return a * np.exp(r1 * t) + b * np.exp(r2 * t)


def decrement_logarithmique(zeta: float) -> float:
    """Décrément logarithmique théorique pour 0 <= zeta < 1."""
    if not 0 <= zeta < 1:
        raise ValueError("Le décrément est défini ici pour le régime sous-amorti.")
    return 2.0 * np.pi * zeta / np.sqrt(1.0 - zeta**2)


def zeta_depuis_decrement(delta: float) -> float:
    """Identifie zeta à partir du décrément logarithmique."""
    if delta < 0:
        raise ValueError("delta doit être positif ou nul.")
    return delta / np.sqrt((2.0 * np.pi) ** 2 + delta**2)
