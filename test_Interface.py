import random
from tkinter import *
from People import *

#On cree une fenetre et un canevas:
Simulation = Tk()
Simulation.title("Crowd Simulation")
width=500
height = 500
interface = Canvas(Simulation, width=width, height=height, bd=0, bg="white")
interface.pack(padx=100, pady=100)
interface.create_rectangle(10, 10, width - 10, height - 10)

# Creation  d'un bouton "Quitter":
Bouton_Quitter = Button(Simulation, text='Quitter', command=Simulation.destroy)
# On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

############################### Creation of the Particles
my_particles = []


# Il faudrait réussir à mettre tous les particules dans une liste pour calculer leur déplacement ensemble

def CreaBalle():
    xcoord = (width - 30) * random.random() + 10
    ycoord = (height - 30) * random.random() + 10
    return interface.create_oval(xcoord, ycoord, xcoord + 20, ycoord + 20, fill='red')


# Better to fix a speed for now
# dx = 10 * random.random()
# dy = 10 * random.random()

def CreaPeople():
    p = People()
    p.xcoord = 50.0
    p.ycoord = 50.0
    p.color = "Yellow"
    return interface.create_oval(p.xcoord, p.ycoord, p.xcoord + 20, p.ycoord + 20, fill=p.color)


# On cree une balle:
# il faut connecter cette partie avec la classe People

for i in range(0, 1):
    b1 = CreaBalle()
    b2 = CreaPeople()

    my_particles.append(b1)
    my_particles.append(b2)
    print(my_particles)


############################### Creation of the Movement
def deplacement():
    global dx, dy
    for i in range(0, 1):
        if interface.coords(my_particles(i))[3] > height - 10:
            dy = -dy
        if interface.coords(my_particles(i))[3] < 30:
            dy = -dy
        if interface.coords(my_particles(i))[2] > width - 10:
            dx = -dx
        if interface.coords(my_particles(i))[2] < 30:
            dx = -dx

    # A améliorer mais l'idée est là (c'était un poil bugé)
    # Test de la collision avec la raquette :
    # if len(interface.find_overlapping(interface.coords(b1)[2], interface.coords(b1)[3],
    #                                interface.coords(b2)[2], interface.coords(b2)[3])) > 1:
    #     dy = -1 * dy

    # On deplace la balle :
    interface.move(my_particles(i), dx, dy)

    # On repete cette fonction
    Simulation.after(30, deplacement)


dx = 5
dy = 5

###############################

deplacement()

# On lance la boucle principale:
Simulation.mainloop()
