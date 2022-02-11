#####################################################
# Import des librairies
#####################################################

import tkinter as tk



#####################################################
# Définition des variables
#####################################################

hauteur_canevas = 500
largeur_canevas = 500



#####################################################
# Boucle principale
#####################################################

racine = tk.Tk()
racine.title("Ecoulement d'un tas de sable")



#####################################################
# Création des widgets
#####################################################

canevas = tk.Canvas(racine, height=hauteur_canevas, width=largeur_canevas, bg="white")

bouton_configuration_aleatoire = tk.Label(racine, text="Configuration aléatoire", bg="grey")


#####################################################
# Placement des widgets
#####################################################

canevas.grid(column=1, row=0)

bouton_configuration_aleatoire.grid(column=0, row=0)


#####################################################
# Fonctions liées aux widgets (commandes des widgets)
#####################################################








racine.mainloop()