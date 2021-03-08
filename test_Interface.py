import math
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

# Creation  d'un bouton "Quitter":
Bouton_Quitter = Button(Simulation, text='Quitter', command=Simulation.destroy)
# On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

# Creation  d'un bouton "Quitter":
Bouton2_Quitter = Button(Simulation, text='rr', command=interface.delete('all'))
# On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton2_Quitter.pack()

w_porte = 30
###############################

def CreaBalle():
    xcoord = (width - 40) * random.random() + 10
    ycoord = (height - 40) * random.random() + 10
    return interface.create_oval(xcoord, ycoord, xcoord + 20, ycoord + 20, fill='red')


def CreaPeople(People):
    p = People
    return interface.create_oval(p.xcoord, p.ycoord, p.xcoord + 20, p.ycoord + 20, fill=p.color)

# Creation of the list of people
def CreaPart():
    my_particles = []
    for i in range(0, 10):
        xcoord = (width - 40) * random.random() + 10
        ycoord = (height - 40) * random.random() + 10
        vx = random.random() * 5
        vy = random.random() * 5
        p = People(xcoord, ycoord, vx, vy)
        my_particles.append(p)
    return my_particles


# Create the environment
def CreateEnv():
    # Create the room
    interface.create_rectangle(20, 20, width - 20, height - 20, outline="red", width=5)
    interface.pack()
    # Create the door
    interface.create_line(20, (height / 2 - w_porte), 20, (height / 2 + w_porte), fill="green", width=5)
    interface.pack()


# Creation of the Movement
def deplacement():
    interface.delete('all')
    global dx, dy
    p = ListPart
    getting_out = 0
    CreateEnv()

    for i in range(0, len(p)):

        b = interface.create_oval(p[i].xcoord, p[i].ycoord, p[i].xcoord + 20, p[i].ycoord + 20, fill=p[i].color)
        interface.pack()

        # b = CreaPeople(ListPart[i])
        if interface.coords(b)[3] > height - 30:
            p[i].vy = -p[i].vy

        if interface.coords(b)[1] < 20:
            p[i].vy = -p[i].vy

        if interface.coords(b)[2] > width - 30:
            p[i].vx = -p[i].vx

        if interface.coords(b)[0] < 20:

            if (height / 2 - w_porte) < interface.coords(b)[1] < (height / 2 + w_porte):
                p[i].vx, p[i].vy = [0, 0]
                interface.delete(b)
                # p.pop(i)
            else:
                p[i].vx = -p[i].vx

        p[i].xcoord = p[i].xcoord + p[i].vx
        p[i].ycoord = p[i].ycoord + p[i].vy

        # Check for collisions between the balls
        for j in range(i + 1, len(ListPart)):
            # the ** is the operator for square
            distance = math.sqrt(
                ((p[j].xcoord + 10) - (p[i].xcoord + 10)) ** 2 + ((p[j].ycoord + 10) - (p[i].ycoord + 10)) ** 2)
            # Check for collision
            if distance < 13:
                # We keep in memory the first speed
                temp_vx = p[i].vx
                temp_vy = p[i].vy

                # Change the speed between particles
                p[i].vx = p[j].vx * 0.9
                p[i].vy = p[j].vy * 0.9

                p[j].vx = temp_vx * 0.9
                p[j].vy = temp_vy * 0.9

                p[i].touched += 1
                p[j].touched += 1

                # Start of relfexion about visualizing the gradient of contact (to modify)
                if p[i].touched == 1:
                    p[i].color = "Yellow"
                if p[j].touched == 1:
                    p[j].color = "Yellow"

                if p[i].touched > 1:
                    p[i].color = "Orange"
                if p[j].touched > 1:
                    p[j].color = "Orange"

                if p[i].touched >= 5:
                    p[i].color = "Red"
                if p[j].touched >= 5:
                    p[j].color = "Red"

    # To reduce the speed of simulation
    Simulation.after(10, deplacement)


def suppr():
    interface.delete('all')


ListPart = CreaPart()
# for i in range(0, len(ListPart)):
deplacement()

# On lance la boucle principale:
Simulation.mainloop()
