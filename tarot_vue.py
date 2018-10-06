import pygame
import os
from enum import Enum
from pygame.locals import *
from tkinter import *

#pygame.init()


# Ouverture de la fenêtre Pygame

height=600
width=1000

hauteurCarte=116
largeurCarte=63

fenetre = pygame.display.set_mode((width, height))


class EtatPartie(Enum):
    ANNONCE = 1
    JEU = 2
    DECOMPTE = 3


class EtatCarte(Enum):
    VISIBLE=1
    CACHE=2


class VuePartie :
    def __init__(self, ensJoueur):
        self.etatPartie=EtatPartie.ANNONCE
        self.ensJoueur=ensJoueur

    def affichePlateau(self) :
        #Chargement et collage du fond
        fond = pygame.image.load("image/tapis_de_jeu.png").convert()
        fond = pygame.transform.scale(fond, (width, height))
        fenetre.blit(fond, (0,0))

    def updateEtat(self, etat):
        self.etatPartie =etat

    def afficheChien(self):
        if self.etatPartie == EtatPartie.ANNONCE:
            carte = pygame.image.load("image/dosCarte.png").convert()
            carte.set_colorkey((255, 255, 255))
            carte = pygame.transform.scale(carte, ( largeurCarte,hauteurCarte))

            fenetre.blit(carte, (width/2-largeurCarte, height/2-hauteurCarte))
            fenetre.blit(carte, (width/2-largeurCarte+20, height/2-hauteurCarte+20))
            fenetre.blit(carte, (width/2-largeurCarte+40, height/2-hauteurCarte+40))





class VueJoueur :
    def __init__(self,num,main):

        self.main=[]

        for carte in main:
            self.main.append(VueCartes(carte.nom, carte.couleur))

        self.num=num
        #self.tourJoueur= -1 # 0->joueur 0, 1->joueur 1 ...



    """def updateTours(self, tourJoueur ):
        self.tourJoueur=tourJoueur"""

    def updateMain(self, main1):
        for carte in main1 :
            self.main.append(VueCartes(carte.nom, carte.couleur))


    def afficherCartes (self):

        x1=0
        y1=height-116

        carte1 = pygame.image.load("image/dosCarte.png").convert()
        carte1.set_colorkey((255, 255, 255))
        carte1 = pygame.transform.scale(carte1, (63, 116))

        x2=0
        y2=0

        x3 = width/2
        y3 = 0

        x4 = width-63
        y4 = height/4

        x5 = 0
        y5 = height/4

        print(self.main)

        for carte in self.main :
            carte.affiche(x1,y1)
            x1=x1+63

            fenetre.blit(carte1, (x2, y2))
            fenetre.blit(carte1, (x3, y3))
            fenetre.blit(carte1, (x4, y4))
            fenetre.blit(carte1, (x5, y5))
            x2=x2+10
            x3 = x3 + 10
            y4 = y4 + 10
            y5 = y5 + 10

class VueCartes:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

    def affiche(self,x,y):
        fichier ="image/"+self.nom +self.couleur+".png"
        print(fichier)
        if os.path.isfile(fichier) :
            carte = pygame.image.load(fichier).convert()
            print ("ici")
        else:
            carte=pygame.image.load("image/dosCarte.png").convert()

        carte.set_colorkey((255, 255, 255))
        carte = pygame.transform.scale(carte, (63, 116))
        fenetre.blit(carte, (x, y))























