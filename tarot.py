from random import randint



class Partie:

    def __init__(self, ensJoueur):
        self.annonce = 0
        self.finPartie = False
        self.debutPartie = False
        self.joueurs = ensJoueur
        self.indiceJoueurQuiPrend = -1
        couleur = ["carreau", "pic", "trefles", "coeur"]
        self.cartes = [Carte("Excuse", 4.5, "Excuse"), Carte("le petit", 4.5, "atout"),
                       Carte("21", 4.5, "atout"),
                       Carte("2", 1.5, "atout"), Carte("3", 1.5, "atout"),
                       Carte("4", 1.5, "atout"),
                       Carte("5", 1.5, "atout"), Carte("6", 1.5, "atout"),
                       Carte("7", 1.5, "atout"),
                       Carte("8", 1.5, "atout"), Carte("9", 1.5, "atout"),
                       Carte("10", 1.5, "atout"), Carte("11", 1.5, "atout"),
                       Carte("12", 1.5, "atout"), Carte("13", 1.5, "atout"),
                       Carte("14", 1.5, "atout"),
                       Carte("15", 1.5, "atout"), Carte("16", 1.5, "atout"),
                       Carte("17", 1.5, "atout"),
                       Carte("18", 1.5, "atout"), Carte("19", 1.5, "atout"),
                       Carte("20", 1.5, "atout")]

        for c in couleur:
            self.cartes.append(Carte("Roi", 4.5, c))
            self.cartes.append(Carte("Dame", 3.5, c))
            self.cartes.append(Carte("Cavalier", 2.5, c))
            self.cartes.append(Carte("Valet", 1.5, c))
            for i in range(10):
                self.cartes.append(Carte(str(i + 1), 1.5, c))

        self.distribuerCarte()
        #self.enchere()

    def distribuerCarte(self):
        carte_a_distribuer = list(self.cartes)
        for i in range(len(self.joueurs)):
            for j in range(15):
                r = randint(0, len(carte_a_distribuer) - 1)
                c = carte_a_distribuer[r]
                self.joueurs[i].main.append(c)
                del carte_a_distribuer[r]

        for j in self.joueurs:
            j.chien = carte_a_distribuer

        print(self.joueurs[0])

    def enchere(self):
        """pas encore de prise -> 0
            prise->1
            garde-> 2
            garde sans-> 3
            garde contre->4 """

        i = 0
        while i < 5 and self.annonce < 4:
            paroleJ = self.joueurs[i].parler(self.annonce)
            if paroleJ != 0:
                self.annonce = paroleJ
                self.indiceJoueurQuiPrend = i
            i += 1

        print("joueur qui prend : " + str(self.indiceJoueurQuiPrend))
        if self.indiceJoueurQuiPrend != -1:
            print("annonce : " + str(self.annonce))
            if self.annonce == 1 or self.annonce == 2:
                self.joueurs[self.indiceJoueurQuiPrend].possedeChien = True
                self.joueurs[self.indiceJoueurQuiPrend].construireChien()
            self.debuterPartie()

        else:
            self.finirPartie()

    def debuterPartie(self):
        self.debutPartie = True

    def finirPartie(self):
        self.finPartie = True


class Joueur:
    def __init__(self, num):
        self.numero = num
        self.main = []
        self.chien = []
        self.possedeChien = False

    def parler(self, annonce):
        """pas encore de prise -> 0
            prise->1
            garde-> 2
            garde sans-> 3
            garde contre->4 """

        annonceJ = input("valeur annonce " + str(self.numero) + " :")

        while (int(annonceJ) != 0 and int(annonceJ) <= annonce) or int(annonceJ) > 4:
            annonceJ = input("valeur annonce " + str(self.numero) + " :")

        return int(annonceJ)

    def __str__(self):
        jeu = ""
        for c in self.main:
            jeu += str(c) + ", "

        return "Joueur : " + str(self.numero) + " Jeu : " + jeu

    def construireChien(self):
        if self.possedeChien:
            possibilitesPourChienAff = ""
            possibilitesPourChien = self.main + self.chien
            chien = []

            for i in range(3):
                possibilitesPourChienAff=""
                for c in possibilitesPourChien:
                    possibilitesPourChienAff += str(c) + ", "


                indCarte = int(input(
                    "Choisir une carte a ecarter dans le chien (pas de roi ni de bout) .  Votre jeu : " + possibilitesPourChienAff))
                while (possibilitesPourChien[indCarte] in chien) or not(possibilitesPourChien[indCarte].isValideChien()) :
                    indCarte = int(input(
                        "Carte invalide - Choisir une carte a ecarter dans le chien (pas de roi ni de bout) .  Votre jeu : " + str(
                            possibilitesPourChienAff)))

                chien.append(possibilitesPourChien[indCarte])
                print(possibilitesPourChien.pop(indCarte))


            print("le chien :")
            for c in chien :
                print (" "+str(c)+" ")
        else:
            print("erreur")


class Carte:

    def __init__(self, nom, valeur, couleur):
        self.nom = nom
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        if (self.couleur != "atout" and self.couleur != "Excuse"):
            return self.nom + " de " + self.couleur
        elif (self.couleur != "Excuse"):
            return self.nom + "(atout)"
        else:
            return self.nom

    def isValideChien(self):
        if self.nom == "Roi" or self.nom=="Excuse" or self.nom=="le petit" or self.nom=="21" :
            return False
        else :
            return True

    def montrerCarteDuChien(self):
        if self.couleur=="atout" :
            return True
        else :
            return False



