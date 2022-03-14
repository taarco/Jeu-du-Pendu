import random
from graphics_nsi import *

#by Taarco

def perdu(n):
    if n == 1:
        draw_line(Point(500, 450), Point(800, 450), white)
    elif n == 2:
        draw_line(Point(600, 450), Point(600, 50), white)
    elif n == 3:
        draw_line(Point(600, 50), Point(800, 50), white)
    elif n == 4:
        draw_line(Point(800, 50), Point(800, 100), white)
    elif n == 5:
        draw_circle(Point(800, 125),25,white)
    elif n == 6:
        draw_line(Point(800, 150), Point(800, 250), white)
    elif n == 7:
        draw_line(Point(800, 150), Point(850, 175), white)
    elif n == 8:
        draw_line(Point(800, 150), Point(750, 175), white)
    elif n == 9:
        draw_line(Point(800, 250), Point(750, 300), white)
    elif n == 10:
        draw_line(Point(800, 250), Point(850,300), white)
    affiche_all()

def main():
    al = 'abcdefghijklmnopqrstuvwxyz'
    fichier = open("liste_francais.txt", "r")
    ListeMot = fichier.read().split()
    aleatoire = random.choice(ListeMot)
    aleatoire2 = aleatoire
    MotUtilisateur = []
    for i in aleatoire:
        if i in al:
            MotUtilisateur.append("_")
        else:
            MotUtilisateur.append(i)
    LettresUtilise = ""

    init_graphic(1080,720,'Jeu Du Pendu',(0,52,7))

    mort = False
    continuer = True
    faux = 0
    print(aleatoire)
    while not mort and continuer:
        if not ('_' in MotUtilisateur):
            continuer = False

        if faux == 10:
            mort = True

        aff_pol('Lettres utilisés :', 30, Point(45,25), white)
        w = 0
        for i in range(len(LettresUtilise)):
            if i%5 == 0:
                w+=1
            aff_pol(LettresUtilise[i], 20, Point(70+20*(i%5), 100+ 30*w), white)

        draw_fill_rectangle(Point(560,585), 600, 120, (0,70,10))
        aff_pol("Mot : " + ' '.join(MotUtilisateur), 40, Point(300, 550), white)
        if continuer and not mort:
            k = wait_key()
            if k in aleatoire:
                if not (k in LettresUtilise):
                    LettresUtilise += k.upper()+' '
                for i in range(len(aleatoire)):
                    if aleatoire[i] == k:
                        MotUtilisateur[i] = k
            elif k in al:
                if not (k in LettresUtilise):
                    LettresUtilise += k.upper()+' '
                faux += 1
                perdu(faux)

    if mort:
        aff_pol("Perdant !", 100, Point(400,300), red)
        aff_pol("le mot était : " + ' ' .join(aleatoire), 25, Point(400,410), red)
    else:
        aff_pol("Gagnant !", 100, Point(400, 300), gold)

    wait_escape()


main()