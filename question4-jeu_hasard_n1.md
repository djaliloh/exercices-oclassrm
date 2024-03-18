
En premier lieu un jeu que l’on notera A qui est un simple jeu de pile ou face avec une pièce biaisée (pile avec une probabilité de p=0.49). Le joueur mise un euro et lance la pièce : s’il obtient pile il gagne un euro en plus de récupérer sa mise, sinon il perd sa mise.

Ensuite, un jeu que l’on notera B, qui est un jeu avec deux pièces biaisées. La première pièce donne pile avec une probabilité p1 = 0.09 et la seconde pièce donne pile avec une probabilité p2 = 0.74. Le joueur de ne peut miser qu’un euro à la fois ! En revanche, on regarde à chaque lancé son capital (la somme d’argent total) dont il dispose pour déterminer quelle pièce lancer : si le capital est un multiple de 3, on lance la pièce numéro une, sinon on lance la seconde pièce. Comme dans le jeu A, le joueur remporte sa mise plus un euro supplémentaire si la pièce choisie tombe sur pile, sinon il perd sa mise.


On considère qu’un jeu est gagnant lorsqu’un joueur est censé finir avec un capital plus élevé qu’initialement après avoir effectué un grand nombre (par exemple : plusieurs centaines) de parties. Mettez en place ces deux jeux de hasard avec Python, via l’utilisation de librairies vues un peu plus tôt, en considérant que le joueur part avec un capital de 1000€. 

Quelle affirmation parmi les suivantes est vraie :

     Le jeu A est perdant alors que le jeu B est gagnant.

    Les deux jeux sont gagnants. 

    Les deux jeux sont perdants.

    On ne peut pas déterminer à partir des informations données