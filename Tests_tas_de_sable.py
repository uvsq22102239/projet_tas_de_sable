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
import random as rd
from functools import partial



#####################################################
# Définition des constantes
#####################################################

HAUTEUR_CANEVAS = 500
LARGEUR_CANEVAS = 500

NB_CASES_GRILLE = 50


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





def couleurCases(matrice):
    """ Colorie toutes les cases en fonction de leur nombre de grains de sable"""


    for i in range(len(matrice)):
        for j in range(len(matrice)):
            case = canevas.create_rectangle(coordonneesCase(i, j), fill="red")
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

    return




def initialisationConfiguration(taille):
    """ Créer une matrice carrée nulle de taille choisie par l'utilisateur"""

    global configuration_courante
    matrice=[]

    for i in range(taille):
        l=[]
        for j in range(taille):
            l.append(0)
        matrice.append(l)


    configuration_courante = matrice
    couleurCases(configuration_courante)


    return configuration_courante




def configurationAleatoire(taille):
    """Fonction qui assimile à chaque case une valeur aléatoire
     de grains de sable jusqu'à 3 (compris)"""

    global configuration_courante
    matrice = initialisationConfiguration(taille)

    for i in range(taille):
        for j in range(taille):
            matrice[i][j] = rd.randint(0, 10)

    configuration_courante = matrice
    couleurCases(configuration_courante)

    return configuration_courante




def ecoulementSable(matrice):
    """Modifie la matrice pour simuler l'écoulement du tas de sable"""

    cpt = 0
    liste_cases_instables = []

    for i in range(len(matrice)):           # Vérifie s'il y a des cases instable (et les compte)
        for j in range(len(matrice)):
            if matrice[i][j] >= 4 :
                cpt += 1
    
    if cpt != 0:                            # S'il y a une case instable, alors la matrice sera modifiée
        for i in range(len(matrice)):           # On parcourt la matrice pour savoir la position des cases instables
            for j in range(len(matrice)):
                if matrice[i][j] >= 4:          # S'il s'agit d'une case instable
                    liste_cases_instables.append([i,j])         #Alors on note ses coordonnées dans une liste (pour ne pas les oublier)
                    if (i==0 and j==0) or (i==0 and (j==len(matrice)-1)) or ((i==len(matrice)-1) and j==0) or ((i==len(matrice)-1) and (j==len(matrice)-1)):     # Si la case instable est un coin
                        matrice[i][j] -= 2              # Les coins donnent 2 grains de sable à leurs voisins
                    elif (i==0 and 0<j<(len(matrice)-1)) or ((i==len(matrice)-1) and 0<j<(len(matrice)-1)) or (0<i<(len(matrice)-1) and j==0) or (0<i<(len(matrice)-1) and j==(len(matrice)-1)):        #Si la case est un bord
                        matrice[i][j] -= 3
                    else :
                        matrice[i][j] -= 4
        for k in liste_cases_instables:
            ajoutSableVoisins(k[0], k[1], configuration_courante)

    couleurCases(configuration_courante)
#   ecoulementSable.
    
    


def ajoutSableVoisins(i,j, matrice):
        """ Fonction utilisée pour l'écoulement du sable, qui prend en argument les coordonnées de la 
        case instable et ajoute 2, 3 ou 4 grains de sable à ses voisins"""


        if i==0 and j==0:
            matrice[i+1][j] += 1
            matrice[i][j+1] += 1
        elif i==0 and (j==len(matrice)-1):
            matrice[i+1][j] += 1
            matrice[i][j-1] += 1
        elif (i==len(matrice)-1) and j==0:
            matrice[i-1][j] += 1
            matrice[i][j+1] += 1
        elif (i==len(matrice)-1) and (j==len(matrice)-1):
            matrice[i-1][j] += 1
            matrice[i][j-1] += 1
        elif i==0 and 0<j<(len(matrice)-1):
            matrice[i][j-1] += 1
            matrice[i][j+1] += 1
            matrice[i+1][j] += 1
        elif (i==len(matrice)-1) and 0<j<(len(matrice)-1):
            matrice[i][j-1] += 1
            matrice[i][j+1] += 1
            matrice[i-1][j] += 1
        elif (0<i<(len(matrice)-1) and j==0):
            matrice[i-1][j] += 1
            matrice[i+1][j] += 1
            matrice[i][j+1] += 1
        elif 0<i<(len(matrice)-1) and j==(len(matrice)-1):
            matrice[i-1][j] += 1
            matrice[i+1][j] += 1
            matrice[i][j-1] += 1
        else :
            matrice[i][j-1] += 1
            matrice[i][j+1] += 1
            matrice[i-1][j] += 1
            matrice[i+1][j] += 1




def pileCentree(taille, N):
    """ Créér une configuration pile centrée"""

    matrice = []
    for i in range(taille):
        l=[]
        for j in range(taille):
            l.append(0)
        matrice.append(l)

    coord = taille // 2
    matrice[coord][coord] = N

    configuration_courante = matrice
    couleurCases(configuration_courante)

    return configuration_courante




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





##### Boutons
bouton_configuration_aleatoire = tk.Button(racine, text="Configuration aléatoire", bg="grey", command=partial(configurationAleatoire, NB_CASES_GRILLE))
bouton_reinitialisation = tk.Button(racine, text="Réinitialiser", bg="grey", command=partial(initialisationConfiguration, NB_CASES_GRILLE))
bouton_ecoulement = tk.Button(racine, text="Ecoulement du sable", bg="grey", command=lambda :ecoulementSable(configuration_courante))
slider_pile_centree = tk.Scale(racine, from_=0, to=1000)
bouton_pile_centree = tk.Button(racine, bg="grey", text="Pile centrée", command=lambda: pileCentree(NB_CASES_GRILLE, slider_pile_centree.get()))


#####################################################
# Placement des widgets


canevas.grid(column=1, row=0, rowspan=5)

bouton_configuration_aleatoire.grid(column=0, row=0)
bouton_reinitialisation.grid(column=0, row=1)
bouton_ecoulement.grid(column=0, row=2)
slider_pile_centree.grid(column=0, row=3)
bouton_pile_centree.grid(column=0, row=4)



#####################################################
# Gestion de la configuration courante 


configuration_courante = configurationAleatoire(NB_CASES_GRILLE)
configurationAleatoire(NB_CASES_GRILLE)





#####################################################
# Gestion des évenements liés aux widgets









racine.mainloop()