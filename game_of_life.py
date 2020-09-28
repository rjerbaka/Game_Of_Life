from tkinter import *
from math import *
from random import *
import numpy
import os
from time import sleep

flag = 0
ligne= 30
colonne= 30
#nbvie = floor(90 * 0.2)
pv = 0.2
v = 6
M = [[0] * colonne for i in range(ligne)]
cellules = [[0] * colonne for i in range(ligne)]

def gsize(self):
    global ligne
    global colonne
    global flag
    if flag==1: return
    ligne = taille.get()
    colonne = taille.get()

def vie(self):
    #global nbvie
    global pv
    pv = pvie.get()
    #p = float(pv/100)
    #nbvie = floor(ligne*colonne*p)

def speed(self):
    global v
    v = 603 - 6*(vitesse.get())

def nb_voisin (i,j):
        global ligne
        global colonne
        nb_voisin=0
        for k in range(i-1,i+2):
            if M[k%ligne][(j-1)%colonne]!=0:
                                nb_voisin+=1
            if M[k%ligne][(j+1)%colonne]!=0:
                                nb_voisin+=1
            if k%ligne!=i and M[k%ligne][j]!=0:
                                nb_voisin+=1
        return nb_voisin


def arreter():
    global flag
    flag = 0

def jeu_de_vie():
        global flag
        global v
        flag = 1
        fen.after(v,jeu)



def jeu():
            global ligne
            global colonne
            global flag
            global M
            global v

            voisin=0
            vecteur=[]
            x=0
            y=0
            for i in range(ligne):
                vecteur.append([])
                for j in range (colonne):
                    voisin=nb_voisin(i,j)
                    if voisin==2:
                        vecteur[i].append(M[i][j])
                        continue
                    if voisin==3:
                        vecteur[i].append(1)
                        continue
                    vecteur[i].append(0)
            M=vecteur
            can.delete("all")
            for i in range(ligne):
                    for j in range(colonne):

                        x = i*(600/float(colonne))
                        dx = (i+1)*(600/float(colonne))
                        y = j*(600/float(ligne))
                        dy =float((j+1)*(600/float(ligne)))

                        if M[i][j]==0:
                            cellules[i][j] = can.create_rectangle(x, y, dx, dy, \
                         fill="white",outline ="black")
                        if M[i][j]==1:
                            cellules[i][j] = can.create_rectangle(x, y, dx, dy, \
                         fill="red",outline ="black")

            if flag > 0:
                fen.after(v,jeu)




def initialisation():
        global ligne
        global colonne
        #global nbvie
        global M
        global cellules
        global pv
        #n=nbvie
        l = ligne
        c = colonne
        can.delete("all")
        M = [[0] * c for i in range(l)]
        cellules = [[0] * c for i in range(l)]
        vecteur = numpy.random.binomial(1, pv/float(100), size=l*l)

        for i in range(l):
                for j in range(c):

                    M[i][j] = vecteur[(i-1)*l+j]

                    x = i*(600/float(c))
                    dx = (i+1)*(600/float(c))
                    y = j*(600/float(l))
                    dy =float((j+1)*(600/float(l)))

                    if M[i][j]==0:
                        cellules[i][j] = can.create_rectangle(x, y, dx, dy, \
                     fill="white",outline ="black")
                    if M[i][j]==1:
                        # n = n - 1
                        cellules[i][j] = can.create_rectangle(x, y, dx, dy, \
                     fill="red",outline ="black")



fen = Tk()
fen.title("Le Jeu de la vie")
fen.geometry("800x600")
can = Canvas(fen,bg="white",height=600,width=600)
can.pack(side = LEFT)


Button(fen, text='Quitter', width=20, command=fen.destroy, foreground = "#5c708f" ).pack(side = BOTTOM)

vitesse = Scale(fen, from_ = 0, to = 100, orient = HORIZONTAL, command = speed, \
foreground = "#5c708f")
vitesse.pack(side=BOTTOM)
vitesse.set(6)
Label(text ='\nVitesse', foreground = "#5c708f").pack(side = BOTTOM)

pvie = Scale(fen, from_ = 0, to = 100, orient = HORIZONTAL, command = vie, \
foreground = "#5c708f")
pvie.pack(side=BOTTOM)
pvie.set(20)
Label(text ='\n% de Vie', foreground = "#5c708f").pack(side = BOTTOM)

taille = Scale(fen, from_ = 0, to = 100, orient = HORIZONTAL, command = gsize, \
foreground = "#5c708f")
taille.pack(side=BOTTOM)
taille.set(30)
Label(text ='\nTaille de la grille', foreground = "#5c708f").pack(side = BOTTOM)

Button(fen, text='Lancer', width=20, command=jeu_de_vie, \
foreground = "#5c708f").pack(side = TOP)

Button(fen, text='Arreter', width=20, command=arreter, \
foreground = "#5c708f").pack(side = TOP)

init = Button(fen, text='Initialiser', width=20, command=initialisation, \
foreground = "#5c708f")
init.pack(side = TOP)

fen.mainloop()
