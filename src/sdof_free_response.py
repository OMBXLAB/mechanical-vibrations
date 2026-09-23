"""Réponse libre d'un oscillateur linéaire à 1 DDL."""

import numpy as np


def caracteristiques(m: float, c: float, k: float) -> tuple[float, float]:
    """Retourne la pulsation propre non amortie et le taux d'amortissement."""
    if m <= 0 or k <= 0:
        raise ValueError("m et k doivent être strictement positifs.")
    omega_n = np.sqrt(k / m)
    zeta = c / (2.0 * np.sqrt(k * m))
    return omega_n, zeta


def reponse_libre_sous_amortie(t, m, c, k, x0, v0):
    """Solution analytique pour 0 <= zeta < 1."""
    omega_n, zeta = caracteristiques(m, c, k)
    if not 0 <= zeta < 1:
        raise ValueError("Cette fonction traite uniquement le régime sous-amorti.")
    omega_d = omega_n * np.sqrt(1.0 - zeta**2)
    a = x0
    b = (v0 + zeta * omega_n * x0) / omega_d
    return np.exp(-zeta * omega_n * t) * (
        a * np.cos(omega_d * t) + b * np.sin(omega_d * t)
    )


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    t = np.linspace(0.0, 5.0, 2000)
    x = reponse_libre_sous_amortie(t, 1.0, 0.4, 100.0, 0.05, 0.0)
    plt.plot(t, x)
    plt.xlabel("Temps (s)")
    plt.ylabel("Déplacement (m)")
    plt.title("Réponse libre sous-amortie")
    plt.grid(True)
    plt.show()
