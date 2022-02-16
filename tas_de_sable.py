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
from unittest import case



#####################################################
# Définition des constantes
#####################################################

HAUTEUR_CANEVAS = 500
LARGEUR_CANEVAS = 500

NB_CASES_GRILLE = 100


#####################################################
# Définition des variables globales
#####################################################

global case

global configuration_courante

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

### il faudra à la fin remplacer la couleur par défaut "red" par la couleur noire ("black")
### car le rouge sert à visualiser si le code fonctionne correctement



def creationConfiguration(taille):
    """ Créer une matrice carrée nulle de taille choisie par l'utilisateur"""

    ligne = []
    matrice = []

    for i in range(taille):
        ligne.append(0)

    for j in range(taille):
        matrice.append(ligne)

    return matrice



### Fonction qui remplace tous les 0 de la matrice par un nombre aléatoire ("configurationAleatoire")



def couleurCases(matrice):
    """ Colorie toutes les cases en fonction de leur nombre de grain de sable"""


    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 0:
                canevas.itemconfigure(case, fill="white")
            elif matrice[i][j] == 1:
                canevas.itemconfigure(case, fill="blanched almond")
            elif matrice[i][j] == 2:
                canevas.itemconfigure(case, fill="NavajoWhite2")
            elif matrice[i][j] == 3:
                canevas.itemconfigure(case, fill="tan1")
            elif matrice[i][j] == 4:
                canevas.itemconfigure(case, fill="sienna3")
            elif matrice[i][j] == 5:
                canevas.itemconfigure(case, fill="salmon4")
            elif matrice[i][j] == 6:
                canevas.itemconfigure(case, fill="sienna4")
            elif matrice[i][j] == 7:
                canevas.itemconfigure(case, fill="saddle brown")
            elif matrice[i][j] == 8:
                canevas.itemconfigure(case, fill="maroon")
            else :
                canevas.itemconfigure(case, fill="black")




def initialisationConfiguration(matrice):
    """ Chaque élément de la matrice est remplacé par un zéro : on obtient une matrice nulle"""

    for i in range(len(matrice)):
        for j in range(len(matrice)):
            matrice[i][j] = 0

    return matrice

<<<<<<< HEAD
=======
def configAleatoire(matrice):
    """Fonction qui assimile à chaque case une valeur aléatoire
     de grains de sable jusqu'à 3 (compris)"""


    for i in range(len(matrice)):
        for j in range(len(matrice)):
            matrice[i][j] = rd.randint(0, 3)
            
    return matrice
    

>>>>>>> 5454ed96fc5f44c1e9974d583a567e1345d100c4

#####################################################
# Boucle principale
#####################################################

racine = tk.Tk()
racine.title("Simulation de l'écoulement d'un tas de sable")


#####################################################
# Création des widgets


##### Canevas (+ grille + cases)
canevas = tk.Canvas(racine, height=HAUTEUR_CANEVAS, width=LARGEUR_CANEVAS, bg="white")

creationGrille(NB_CASES_GRILLE)

for i in range(NB_CASES_GRILLE):
    for j in range(NB_CASES_GRILLE):
        creationCase(i, j)



##### Boutons
bouton_configuration_aleatoire = tk.Label(racine, text="Configuration aléatoire", bg="grey")




#####################################################
# Placement des widgets


canevas.grid(column=1, row=0)

bouton_configuration_aleatoire.grid(column=0, row=0)



#####################################################
# Gestion de la configuration courante 


configuration_courante = creationConfiguration(NB_CASES_GRILLE)

#configurationAleatoire(configuration_courante)



#####################################################
# Gestion des évenements liés aux widgets


###### lier la fonction "configurationAleatoire" avec le bouton "Configuration Aleatoire"









racine.mainloop()