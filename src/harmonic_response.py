"""Fonctions de réponse harmonique d'un oscillateur 1 DDL."""

import numpy as np


def amplification_dynamique(r, zeta: float):
    """Facteur X/(F0/k) en fonction du rapport r = omega/omega_n."""
    r = np.asarray(r, dtype=float)
    if zeta < 0:
        raise ValueError("zeta doit être positif ou nul.")
    return 1.0 / np.sqrt((1.0 - r**2) ** 2 + (2.0 * zeta * r) ** 2)


def phase(r, zeta: float):
    """Déphasage en radians, calculé avec atan2 pour le bon quadrant."""
    r = np.asarray(r, dtype=float)
    return np.arctan2(2.0 * zeta * r, 1.0 - r**2)


def rapport_resonance(zeta: float):
    """Rapport omega_r/omega_n du pic de déplacement, s'il existe."""
    if zeta < 0:
        raise ValueError("zeta doit être positif ou nul.")
    if zeta >= 1.0 / np.sqrt(2.0):
        return None
    return np.sqrt(1.0 - 2.0 * zeta**2)
