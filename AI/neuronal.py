# T-Rex AI - NN et GA


import numpy as np
import random as rd

# ----------------------- DESCRIPTIONS ----------------------- #

# Variables d'entrée normalisées entre 0 et 1
# max_cactus_size : 75
# max_speed : 13
# max_distance : 600
# Variable  de sortie : HAUT pour > 0.6
#                       BAS  pour < 0.4

# STRUCTURE DU RN :      3   --   3   --   1
#
#              distance.╭─╮ ____ ╭─╮
#                       ╰─╯ ╲  ╱ ╰─╯
#                taille.╭─╮ _╲╱_ ╭─╮ ____ ╭─╮.sortie
#                       ╰─╯  ╱╲  ╰─╯      ╰─╯
#               vitesse.╭─╮ ╱__╲ ╭─╮
#                       ╰─╯      ╰─╯
#

# STOCKAGE DES DONNEES:
# On garde seulement les poids et le seuil de chaque perceptron.
# Le suil est compté comme poids associé à une entrée "-1"
# On a donc 1 RN = 16 'poids' (12 poids et 4 seuils)
# → Conversion entre liste simple et paire de matrice (W1, W2)
#   selon les besoins.

# Format matriciel :
# Retenir que les couches sont vues comme des vecteurs lignes
# Les poids associés à un perceptron sont dcsur la meme col.




# ------------------------ GENERATION ------------------------ #



def individu_alea():
    return 0


class Reseau_Neurones():
    def __init__(self):        
        # Structure fixée 3-3-1
        self.nbEntrees  = 3  # Distance - Taille - Vitesse
        self.nbCachee = 3
        self.nbSortie = 1 
        
        self.W1 = np.random.randn(self.nbEntrees, self.nbCachee)
        self.W2 = np.random.randn(self.nbCachee, self.nbSortie)

    def forward(self, X):
        # Propagation des entrées
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.tranfert(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.tranfert(self.z3) 
        return yHat
        
    def tranfert(self, z):
        # Ici la fonction sigmoidde
        return 1/(1+np.exp(-z))

test = Reseau_Neurones()