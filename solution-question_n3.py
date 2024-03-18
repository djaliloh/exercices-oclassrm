import random

def lancer_de():
    return random.randint(1, 6)


total_lancers = 10000 
lancers_sous_echantillon = 1000
frequence_6_total = 0
frequence_4_sous_echantillon = 0


for _ in range(5):

    frequence_4_sous_echantillon_temp = 0
    
    # Effectuer 10 000 lancers
    for _ in range(total_lancers):
        resultat_lancer = lancer_de()
        if resultat_lancer == 6:
            frequence_6_total += 1
        
    # Prendre un échantillon aléatoire de 1 000 lancers
    sous_echantillon = random.sample(range(total_lancers), lancers_sous_echantillon)
    for indice_lancer in sous_echantillon:
        if lancer_de() == 4:
            frequence_4_sous_echantillon_temp += 1
    
    # la moyenne des fréquences de 4 dans le sous-échantillon
    frequence_4_sous_echantillon += frequence_4_sous_echantillon_temp / lancers_sous_echantillon

# les moyennes des fréquences de 6 pour les 10 000 lancers
m = frequence_6_total / (total_lancers * 5)

# les moyennes des fréquences de 4 pour les 1 000 lancers dans le sous-échantillon
n = frequence_4_sous_echantillon / 5

print("m :", m)
print("n :", n)
