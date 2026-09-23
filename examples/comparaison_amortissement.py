"""Comparaison des trois régimes d'amortissement d'un oscillateur 1 DDL."""

import matplotlib.pyplot as plt
import numpy as np

from src.sdof_free_response import reponse_libre

m = 1.0
k = 100.0
omega_n = np.sqrt(k / m)
c_critique = 2.0 * m * omega_n

t = np.linspace(0.0, 3.0, 2000)
x0, v0 = 0.05, 0.0

cas = {
    "Sous-amorti (ζ = 0,10)": 0.10 * c_critique,
    "Critique (ζ = 1)": c_critique,
    "Sur-amorti (ζ = 1,50)": 1.50 * c_critique,
}

for etiquette, c in cas.items():
    plt.plot(t, reponse_libre(t, m, c, k, x0, v0), label=etiquette)

plt.xlabel("Temps (s)")
plt.ylabel("Déplacement x(t) (m)")
plt.title("Réponse libre — influence de l'amortissement")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
