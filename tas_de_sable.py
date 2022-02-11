#####################################################
# groupe LDDBI L1
# Lucas AUCLAIR
# Nikita VERSHYNIN
# Camille LE CORRE
# https://github.com/uvsq22102239/projet_tas_de_sable
#####################################################








#####################################################
# Import des librairies
#####################################################

import tkinter as tk



#####################################################
# Définition des constantes
#####################################################

HAUTEUR_CANEVAS = 500
LARGEUR_CANEVAS = 500

NB_CASES_GRILLE = 100


#####################################################
# Définition des variables globales
#####################################################



#####################################################
# Définition des fonctions
#####################################################


def creationGrille(nb_cases):
    """ Fonction créant la grille affichée sur le canevas, qui prend en argument le nombre
        de cases contenues dans une ligne ou une colonne (car la grille est carrée)"""


    taille_case = LARGEUR_CANEVAS // nb_cases

    for i in range(1, (nb_cases)):
        # lignes verticales
        canevas.create_line((i * taille_case), 0, (i * taille_case), HAUTEUR_CANEVAS)
        # lignes horizontales
        canevas.create_line(0, (i * taille_case), LARGEUR_CANEVAS, (i * taille_case))

    return


#####################################################
# Boucle principale
#####################################################

racine = tk.Tk()
racine.title("Simulation de l'écoulement d'un tas de sable")



#####################################################
# Création des widgets


##### Canevas
canevas = tk.Canvas(racine, height=HAUTEUR_CANEVAS, width=LARGEUR_CANEVAS, bg="white")

creationGrille(NB_CASES_GRILLE)


##### Boutons
bouton_configuration_aleatoire = tk.Label(racine, text="Configuration aléatoire", bg="grey")


##### Cases grille



#####################################################
# Placement des widgets


canevas.grid(column=1, row=0)

bouton_configuration_aleatoire.grid(column=0, row=0)


#####################################################
# Gestion des évenements liés aux widgets









racine.mainloop()