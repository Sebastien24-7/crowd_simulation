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
def CreaBalle():
    xcoord = (width - 30) * random.random() + 10
    ycoord = (height - 30) * random.random() + 10
    return interface.create_oval(xcoord, ycoord, xcoord + 20, ycoord + 20, fill='red')


dx = 10 * random.random()
dy = 10 * random.random()


def CreaPeople():
    p = People()
    p.xcoord = 50.0
    p.ycoord = 50.0
    p.color = "Yellow"
    return interface.create_oval(p.xcoord, p.ycoord, p.xcoord + 20, p.ycoord + 20, fill=p.color)


# ############################### Creation of the Movement
# def deplacement(b1):
#
#         global dx, dy
#         if interface.coords(b1)[3] > height-10:
#             dy=-dy
#         if interface.coords(b1)[3] < 30:
#             dy=-dy
#         if interface.coords(b1)[2] > width-10:
#             dx=-dx
#         if interface.coords(b1)[2] < 30:
#             dx=-dx
#
#         #On deplace la balle :
#         interface.move(b1,dx,dy)
#
#         #On repete cette fonction
#         Simulation.after(30,deplacement)


# On cree une balle:
# il faut connecter cette partie avec la classe People

for i in range(0, 1):
    b1 = CreaBalle()
    b2 = CreaPeople()

    # deplacement(b1)

# On lance la boucle principale:
Simulation.mainloop()
