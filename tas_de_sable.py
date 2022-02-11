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
# Définition des variables
#####################################################

hauteur_canevas = 500
largeur_canevas = 500

nb_cases_grille = 100



#####################################################
# Boucle principale
#####################################################

racine = tk.Tk()
racine.title("Ecoulement d'un tas de sable")



#####################################################
# Création des widgets
#####################################################

##### Canevas
canevas = tk.Canvas(racine, height=hauteur_canevas, width=largeur_canevas, bg="white")


def creationGrille(nb_cases):
    """ Fonction créant la grille affichée sur le canevas, qui prend en argument le nombre
        de cases contenues dans une ligne ou une colonne (car la grille est carrée)"""


    taille_case = largeur_canevas // nb_cases

    for i in range(1, (nb_cases)):
        # lignes verticales
        canevas.create_line((i * taille_case), 0, (i * taille_case), hauteur_canevas)
        # lignes horizontales
        canevas.create_line(0, (i * taille_case), largeur_canevas, (i * taille_case))

    return


creationGrille(nb_cases_grille)


##### Boutons
bouton_configuration_aleatoire = tk.Label(racine, text="Configuration aléatoire", bg="grey")

##### Cases grille


#####################################################
# Placement des widgets
#####################################################

canevas.grid(column=1, row=0)

bouton_configuration_aleatoire.grid(column=0, row=0)


#####################################################
# Fonctions liées aux widgets (commandes des widgets)
#####################################################








racine.mainloop()