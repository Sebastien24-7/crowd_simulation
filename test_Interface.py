import random
import time
from tkinter import *
from People import *

# On cree une fenetre et un canevas:
Simulation = Tk()
Simulation.title("Crowd Simulation")
width = 500
height = 500
interface = Canvas(Simulation, width=width, height=height, bd=0, bg="white")
interface.pack(padx=100, pady=100)
interface.create_rectangle(10, 10, width - 10, height - 10)

# Creation  d'un bouton "Quitter":
Bouton_Quitter = Button(Simulation, text='Quitter', command=Simulation.destroy)
# On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

# Creation  d'un bouton "Quitter":
Bouton2_Quitter = Button(Simulation, text='rr', command=interface.delete('all'))
# On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton2_Quitter.pack()

#Quelques tests avec les modifs dans la classe People...

dx = random.random()*5
dy = random.random()*5

###############################

def CreaBalle():
    xcoord = (width - 30) * random.random() + 10
    ycoord = (height - 30) * random.random() + 10
    return interface.create_oval(xcoord, ycoord, xcoord + 20, ycoord + 20, fill='red')

def CreaPeople(People):
    p = People
    return interface.create_oval(p.xcoord, p.ycoord, p.xcoord + 20, p.ycoord + 20, fill=p.color)

# Creation of the list of people
def CreaPart():
    my_particles = []
    for i in range(0, 10):
        xcoord = (width - 30) * random.random() + 10
        ycoord = (height - 30) * random.random() + 10
        vx = random.random() * 5
        vy = random.random() * 5
        p = People(xcoord,ycoord,vx,vy)
        my_particles.append(p)
    return my_particles

    # On cree une balle:
    # il faut connecter cette partie avec la classe People

# Creation of the Movement
def deplacement():
    interface.delete('all')
    global dx, dy
    for i in range(0,10):
        p = ListPart[i]
        b=interface.create_oval(p.xcoord, p.ycoord, p.xcoord + 20, p.ycoord + 20, fill=p.color)
        interface.pack()

        #b = CreaPeople(ListPart[i])
        if interface.coords(b)[3] > height - 10:
            p.vy = -p.vy

        if interface.coords(b)[1] < 0:
            p.vy = -p.vy

        if interface.coords(b)[2] > width - 10:
            p.vx = -p.vx

        if interface.coords(b)[0] < 0:
            p.vx = -p.vx

        p.xcoord = p.xcoord + p.vx
        p.ycoord = p.ycoord + p.vy

        #interface.move(b, vx, vy)

    # A améliorer mais l'idée est là (c'était un poil bugé)
    # Test de la collision avec la raquette :
    # if len(interface.find_overlapping(interface.coords(b1)[2], interface.coords(b1)[3],
    #                                interface.coords(b2)[2], interface.coords(b2)[3])) > 1:
    #     dy = -1 * dy

    # On deplace la balle :


    # On repete cette fonction
    Simulation.after(200, deplacement)

def suppr():
    interface.delete('all')

ListPart = CreaPart()
for i in range(0,len(ListPart)):
    deplacement()

# On lance la boucle principale:
Simulation.mainloop()
