import numpy as np

def jeu_A(capital_initial, nombre_parties):
    capital = capital_initial
    for _ in range(nombre_parties):
        if np.random.rand() < 0.49:  # pile avec probabilité 0.49
            capital += 1
        else:
            capital -= 1
    return capital

def jeu_B(capital_initial, nombre_parties):
    capital = capital_initial
    for _ in range(nombre_parties):
        if capital % 3 == 0:  # Si le capital est un multiple de 3, utiliser la première pièce
            if np.random.rand() < 0.09:  # pile avec probabilité 0.09
                capital += 1
            else:
                capital -= 1
        else:
            if np.random.rand() < 0.74:  # pile avec probabilité 0.74
                capital += 1
            else:
                capital -= 1
    return capital

# Paramètres
capital_initial = 1000
nombre_parties = 1000  # Nombre de parties à simuler

# Simulation du jeu A
resultats_A = [jeu_A(capital_initial, nombre_parties) for _ in range(1000)]
capital_moyen_A = np.mean(resultats_A)

# Simulation du jeu B
resultats_B = [jeu_B(capital_initial, nombre_parties) for _ in range(1000)]
capital_moyen_B = np.mean(resultats_B)

print("Capital moyen après 1000 parties pour le jeu A:", capital_moyen_A)
print("Capital moyen après 1000 parties pour le jeu B:", capital_moyen_B)
