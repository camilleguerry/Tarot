import pygame
import tarot_vue
import tarot

from pygame.locals import *



pygame.init()


class ControleurJoueur:

    def __init__(self,i):
        self.joueur_model=tarot.Joueur(i)
        self.joueur_vue=tarot_vue.VueJoueur(i,self.joueur_model.main)


class ControlleurPartie :

    def __init__(self):
        self.continuer = 1


        self.ensJoueur_model = [ControleurJoueur(0).joueur_model, ControleurJoueur(1).joueur_model,
                           ControleurJoueur(2).joueur_model, ControleurJoueur(3).joueur_model,
                           ControleurJoueur(4).joueur_model]

        self.ensJoueur_vue = [ControleurJoueur(0).joueur_vue, ControleurJoueur(1).joueur_vue,
                                ControleurJoueur(2).joueur_vue, ControleurJoueur(3).joueur_vue,
                                ControleurJoueur(4).joueur_vue]



    def run (self):
        partie_vue=tarot_vue.VuePartie(self.ensJoueur_vue)
        partie_vue.affichePlateau()
        partie_vue.afficheChien()
        p = tarot.Partie(self.ensJoueur_model)

        for i in range(5):

            self.ensJoueur_vue[i].updateMain(self.ensJoueur_model[i].main)


        self.ensJoueur_vue[0].afficherCartes()


        pygame.display.flip()












controleur=ControlleurPartie()
controleur.run()



"""while controleur.continuer:
    controleur.continuer = int(input())"""

while controleur.continuer:

    for event in pygame.event.get():

        if event.type == QUIT:
            print("ok")

            controleur.continuer = 0