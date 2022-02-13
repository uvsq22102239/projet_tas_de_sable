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
from tkinter import Menu #, Menubutton => si on veut faire des sous-menu de boutons donc à voir à la fin



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


    for k in range(1, (nb_cases)):
        # lignes verticales
        canevas.create_line((k * taille_case), 0, (k * taille_case), HAUTEUR_CANEVAS)
        # lignes horizontales
        canevas.create_line(0, (k * taille_case), LARGEUR_CANEVAS, (k * taille_case))

    return

def config_aleatoire(nb_cases):
    """fonction qui met les grains de sable aléatoirement : à revoir
     je l'ai faite provisoirement pour le bouton configuration aletoire"""
    


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


##### Boutons et menu
mon_menu = Menu(racine)
racine.config(menu=mon_menu)

actions_menu = Menu(mon_menu)
mon_menu.add_cascade(label="Actions/Options", menu = actions_menu)
actions_menu.add_command(label="Configuration aléatoire", command = config_aleatoire)



##### Cases grille



#####################################################
# Placement des widgets

canevas.grid(column=1, row=0)

#####################################################
# Gestion des évenements liés aux widgets




def coordonneesCase(ligne, colonne):
    """ Définie les coordonnées d'une case de la grille """

    taille_case = LARGEUR_CANEVAS // NB_CASES_GRILLE
    
    x0 = colonne * taille_case
    y0 = ligne * taille_case
    x1 = (colonne + 1) * taille_case
    y1 = (ligne + 1) * taille_case

    liste_coordonnées = [x0, y0, x1, y1]

    return liste_coordonnées


def creationCase(ligne, colonne):
    """ Créer un carré correspondant à une case en fonction de son placement dans la grille """
    
    canevas.create_rectangle(coordonneesCase(ligne, colonne), fill="red")

    return


for i in range(NB_CASES_GRILLE):
    for j in range(NB_CASES_GRILLE):
        creationCase(i, j)





racine.mainloop()