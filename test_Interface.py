import random
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

#Quelques tests avec les modifs dans la classe People...
p=People(10,10)
print (p)
dx = 5
dy = 5



print("my_particles")


###############################



# On lance la boucle principale:
Simulation.mainloop()

# Il faudrait réussir à mettre tous les particules dans une liste pour calculer leur déplacement ensemble

def CreaBalle():
    xcoord = (width - 30) * random.random() + 10
    ycoord = (height - 30) * random.random() + 10
    return interface.create_oval(xcoord, ycoord, xcoord + 20, ycoord + 20, fill='red')

# Better to fix a speed for now
#dx = 10 * random.random()
#dy = 10 * random.random()

def CreaPeople(People):
    p = People
    return interface.create_oval(p.xcoord, p.ycoord, p.xcoord + 20, p.ycoord + 20, fill=p.color)

# Creation of the list of people
def CreaPart():
    my_particles = []
    for i in range(0, 5):
        xcoord = (width - 30) * random.random() + 10
        ycoord = (height - 30) * random.random() + 10
        p = People(xcoord,ycoord)
        my_particles.append(p)
    return my_particles

    # On cree une balle:
    # il faut connecter cette partie avec la classe People

# Creation of the Movement
def deplacement(ListPart):
    global dx, dy
    for i in range(0, 1):
        b=interface.create_oval(ListPart[i].xcoord, ListPart[i].ycoord, ListPart[i].xcoord + 20, ListPart[i].ycoord + 20, fill=ListPart[i].color)
        if interface.coords(b)[3] > height - 10:
            dy = -dy
        if interface.coords(b)[3] < 30:
            dy = -dy
        if interface.coords(b)[2] > width - 10:
            dx = -dx
        if interface.coords(b)[2] < 30:
            dx = -dx

    # A améliorer mais l'idée est là (c'était un poil bugé)
    # Test de la collision avec la raquette :
    # if len(interface.find_overlapping(interface.coords(b1)[2], interface.coords(b1)[3],
    #                                interface.coords(b2)[2], interface.coords(b2)[3])) > 1:
    #     dy = -1 * dy

    # On deplace la balle :
    interface.move(b, dx, dy)

    # On repete cette fonction
    Simulation.after(30, deplacement)

ListPart=CreaPart()
print(ListPart)
CreaPeople(ListPart[0])