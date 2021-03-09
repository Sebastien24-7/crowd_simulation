import math
import random
import time
from tkinter import *
from People import *

##SETUP
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

## VARIABLES
w_porte = 30


#####TRASH##############
# Not Useful anymore
# def CreaBalle():
#     xcoord = (width - 40) * random.random() + 10
#     ycoord = (height - 40) * random.random() + 10
#     return interface.create_oval(xcoord, ycoord, xcoord + 20, ycoord + 20, fill='red')
#
# def CreaPeople(People):
#     p = People
#     return interface.create_oval(p.xcoord, p.ycoord, p.xcoord + 20, p.ycoord + 20, fill=p.color)


# Creation of the list of people
def CreaPart():
    my_particles = []
    for i in range(0, 50):
        xcoord = (width - 40) * random.random() + 20
        ycoord = (height - 40) * random.random() + 20

        # Check it is inside the room (but not functional)
        if 20 > xcoord or xcoord > width - 20:
            xcoord = (width - 50) * random.random() + 20
        if 20 > ycoord or ycoord > height - 20:
            ycoord = (height - 50) * random.random() + 20

        else:
            # coord_sortie = [0, height/2]
            # D = [xcoord - coord_sortie[0], ycoord - coord_sortie[1]]
            #
            # # D_norm=D/math.sqrt((xcoord - coord_sortie[0]) ** 2 + (ycoord - coord_sortie[1]) ** 2)
            # vx = 10*(coord_sortie[0]-xcoord) / math.sqrt((xcoord - coord_sortie[0]) ** 2 + (ycoord - coord_sortie[1]) ** 2)
            # vy = 10*(coord_sortie[1]-ycoord) / math.sqrt((xcoord - coord_sortie[0]) ** 2 + (ycoord - coord_sortie[1]) ** 2)
            # print(D)
            vx = random.random() * 10
            vy = random.random() * 10

            p = People(xcoord, ycoord, vx, vy)
            my_particles.append(p)

    return my_particles


# Compute and give the adapted speed for the particles to reach the door
def ComputeTraject(my_particles):
    coord_sortie = [0, height / 2]

    for i in range(0, len(my_particles)):
        # Compute the distance
        D = [my_particles[i].xcoord - coord_sortie[0], my_particles[i].ycoord - coord_sortie[1]]

        # Give the adapted speed to each particle
        my_particles[i].vx = 10 * (coord_sortie[0] - my_particles[i].xcoord) / math.sqrt(
            (my_particles[i].xcoord - coord_sortie[0]) ** 2 + (my_particles[i].ycoord - coord_sortie[1]) ** 2)
        my_particles[i].vy = 10 * (coord_sortie[1] - my_particles[i].ycoord) / math.sqrt(
            (my_particles[i].xcoord - coord_sortie[0]) ** 2 + (my_particles[i].ycoord - coord_sortie[1]) ** 2)
        # print(D)


# Create the environment
def CreateEnv():
    # Create the room
    interface.create_rectangle(20, 20, width - 20, height - 20, outline="red", width=5)
    interface.pack()
    # Create the door
    interface.create_line(20, (height / 2 - w_porte), 20, (height / 2 + w_porte), fill="green", width=5)
    interface.create_rectangle(0, (height / 2 - w_porte), 20, (height / 2 + w_porte), fill="green", width=5)
    interface.pack()


# Creation of the Movement
def deplacement():
    interface.delete('all')

    p = ListPart
    ComputeTraject(p)
    part_out = []
    CreateEnv()

    # nombre=0
    # n = StringVar(nombre)
    # texteLabel = Label(Simulation, text=StringVar(nombre))
    # texteLabel.pack()

    for i in range(0, len(p)):

        b = interface.create_oval(p[i].xcoord, p[i].ycoord, p[i].xcoord + 20, p[i].ycoord + 20, fill=p[i].color)
        interface.pack()

        # Speed reduced to 0 outside of the room
        if (0 < p[i].xcoord < 20) & ((height / 2 - w_porte) < p[i].ycoord < (height / 2 + w_porte)):
            p[i].vx, p[i].vy = [0, 0]
            # nombre = nombre+1
            # print(nombre)
        if interface.coords(b)[3] > height - 30:
            p[i].vy = -p[i].vy

        if interface.coords(b)[1] < 20:
            p[i].vy = -p[i].vy

        if interface.coords(b)[2] > width - 30:
            p[i].vx = -p[i].vx

        if interface.coords(b)[0] < 20:

            if (height / 2 - w_porte) < interface.coords(b)[1] < (height / 2 + w_porte):
                p[i].vx, p[i].vy = [-1, 0]
                if p[i] not in part_out:
                    part_out.append(p[i])
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
            if distance < 20:
                # We keep in memory the first speed
                vx1 = p[i].vx
                vy1 = p[i].vy
                vx2 = p[j].vx
                vy2 = p[j].vy

                nx = p[i].xcoord - p[j].xcoord
                ny = p[i].ycoord - p[j].ycoord
                nx1 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * nx
                ny1 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * ny
                nx2 = ((vx2 * nx + vy2 * ny) / (nx * nx + ny * ny)) * nx
                ny2 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * ny
                tx1 = vx1 - nx1
                ty1 = vy1 - ny1
                tx2 = vx2 - nx2
                ty2 = vy2 - ny2
                # Change the speed between particles

                p[j].vx = tx1 + nx2
                p[j].vy = ty1 + ny2

                p[i].vx = tx2 + nx1
                p[i].vy = ty2 + ny1

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
    Simulation.after(100, deplacement)

    particles_out = len(part_out)
    print(particles_out)

    # Stop the code if everyone is out
    if len(part_out) == len(p):
        exit()


def suppr():
    interface.delete('all')


ListPart = CreaPart()
deplacement()

# On lance la boucle principale:
Simulation.mainloop()
