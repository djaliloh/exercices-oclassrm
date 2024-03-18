import numpy as np

def jeu_mixte(capital_initial, nombre_parties):
    capital = capital_initial
    for _ in range(nombre_parties):
        if np.random.rand() < 0.5:  # Lancer une pièce équilibrée
            # Jouer au jeu A
            if np.random.rand() < 0.49:  # pile avec probabilité 0.49
                capital += 1
            else:
                capital -= 1
        else:
            # Jouer au jeu B
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
nombre_parties = 1000000  # Nombre de parties à simuler

# Simulation du jeu mixte
resultats_mixte = [jeu_mixte(capital_initial, 1) for _ in range(nombre_parties)]
capital_final_moyen = np.mean(resultats_mixte)

if capital_final_moyen > capital_initial:
    print("Le jeu est gagnant.")
elif capital_final_moyen < capital_initial:
    print("Le jeu est perdant.")
else:
    print("Le jeu est neutre.")


# -----------------
# Reponse: Le jeu est gagnant !
# -----------------