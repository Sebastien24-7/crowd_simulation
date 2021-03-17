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

# # Creation  d'un bouton "Jouer":
# Bouton_Jouer = Button(Simulation, text='Jouer', command=Simulation.destroy)
# # On ajoute l'affichage du bouton dans la fenêtre tk:
# Bouton_Jouer.pack()

# Creation  d'un bouton "Quitter":
Bouton_Quitter = Button(Simulation, text='Quitter', command=Simulation.destroy)
# On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()



### VARIABLES
w_porte = 30


#####TRASH##############
# Not Useful anymore

# Creation of the list of people
def CreaPart(number):
    my_particles = []
    for i in range(0, number):
        xcoord = (width - 40) * random.random() + 30
        ycoord = (height - 40) * random.random() + 30

        coord_sortie = [0, height / 2]
        D = [xcoord - coord_sortie[0], ycoord - coord_sortie[1]]
        # D_norm=D/math.sqrt((xcoord - coord_sortie[0]) ** 2 + (ycoord - coord_sortie[1]) ** 2)
        # print(D)

        vx = 10 * (coord_sortie[0] - xcoord) / math.sqrt(
            (xcoord - coord_sortie[0]) ** 2 + (ycoord - coord_sortie[1]) ** 2)
        vy = 10 * (coord_sortie[1] - ycoord) / math.sqrt(
            (xcoord - coord_sortie[0]) ** 2 + (ycoord - coord_sortie[1]) ** 2)

        # vx = random.random() * 10
        # vy = random.random() * 10

        p = People(xcoord, ycoord, vx, vy)
        my_particles.append(p)
    return my_particles


##Deal with the overlapping at the creation of the particles
def CreaCrowd(my_particles):
    # for i in range(0, len(my_particles)):
    #     # Check it is inside the room (but not functional)
    #     if 25 > my_particles[i].xcoord or my_particles[i].xcoord > width - 50:
    #         my_particles[i].xcoord = (width - 80) * random.random() + 30
    #     if 25 > my_particles[i].ycoord or my_particles[i].ycoord > height - 50:
    #         my_particles[i].ycoord = (height - 80) * random.random() + 30
    #
    #     # Checking the overlapping between particles
    #     for j in range(0, len(my_particles)):
    #         if my_particles[i].distance_collision(my_particles[j]) < 25:
    #             my_particles[i].xcoord = (width - 80) * random.random() + 30
    #             my_particles[i].ycoord = (height - 80) * random.random() + 30
    #
    # return my_particles

    # Initialisation des particules sur forme de grille
        i=5
        j=4
        for k in range(0, len(my_particles)):
            my_particles[k].vx = 0
            my_particles[k].vy = 0
            # my_particles[k].xcoord = 40
            # my_particles[k].ycoord = 40
            if 40*i<=420:
                i=i+1
                my_particles[k].xcoord = 40 * i
                my_particles[k].ycoord = 40 * j
            else :
                i=1
                j=j+1
                my_particles[k].xcoord = 40
                my_particles[k].ycoord = 40 * j

        return my_particles




# Compute and give the adapted speed for the particles to reach the door
def ComputeTraject(my_particles):
    coord_sortie = [0, height / 2]

    for i in range(0, len(my_particles)):
        # Compute the distance
        D = [my_particles[i].xcoord - coord_sortie[0], my_particles[i].ycoord - coord_sortie[1]]
        # print(D)

        # Give the adapted speed to each particle
        my_particles[i].vx = 10 * (coord_sortie[0] - my_particles[i].xcoord) / math.sqrt(
            (my_particles[i].xcoord - coord_sortie[0]) ** 2 + (my_particles[i].ycoord - coord_sortie[1]) ** 2)
        my_particles[i].vy = 10 * (coord_sortie[1] - my_particles[i].ycoord) / math.sqrt(
            (my_particles[i].xcoord - coord_sortie[0]) ** 2 + (my_particles[i].ycoord - coord_sortie[1]) ** 2)


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

    # ComputeTraject(p)
    part_out = []
    CreateEnv()

    # nombre=0
    # n = StringVar(nombre)
    # texteLabel = Label(Simulation, text=StringVar(nombre))
    # texteLabel.pack()

    for i in range(0, len(p)):

        b = interface.create_oval(p[i].xcoord, p[i].ycoord, p[i].xcoord + 20, p[i].ycoord + 20, fill=p[i].color)
        interface.pack()

        p[i].ComputeTraj([0, height / 2])

        # Check for bouncing on the walls or going through the door

        # Speed reduced to 0 outside of the room
        if (0 < p[i].xcoord < 15) & ((height / 2 - w_porte) < p[i].ycoord < (height / 2 + w_porte)):
            p[i].vx, p[i].vy = [0, 0]
            # nombre = nombre+1
            # print(nombre)
        if interface.coords(b)[3] > height - 30:
            p[i].vy = -p[i].vy

        if interface.coords(b)[1] < 25:
            p[i].vy = -p[i].vy

        if interface.coords(b)[2] > width - 30:
            p[i].vx = -p[i].vx

        if interface.coords(b)[0] < 20:

            if (height / 2 - w_porte) < interface.coords(b)[1] < (height / 2 + w_porte) - 20:
                p[i].vx, p[i].vy = [-1, 0]
                p[i].color="green"
                if p[i] not in part_out:
                    part_out.append(p[i])
            else:
                p[i].vx = -p[i].vx

        p[i].xcoord = p[i].xcoord + p[i].vx
        p[i].ycoord = p[i].ycoord + p[i].vy

        ## Check for collisions between the balls ####
        for j in range(0, len(ListPart)):
            # Check for collision
            if p[i].distance_collision(p[j]) <= 20:
                if p[i].DistanceSortie([0, height / 2])<p[j].DistanceSortie([0, height / 2]):
                    while True:
                        p[i].xcoord = p[i].xcoord + p[i].vx
                        p[i].ycoord = p[i].ycoord + p[i].vy
                        p[j].xcoord = p[j].xcoord
                        p[j].ycoord = p[j].ycoord
                        p[i].color = "Red"
                        if p[i].distance_collision(p[j]) > 20:
                            break
                else:
                    p[j].xcoord = p[j].xcoord + p[j].vx
                    p[j].ycoord = p[j].ycoord + p[j].vy
                    p[i].xcoord = p[i].xcoord
                    p[i].ycoord = p[i].ycoord
                    p[j].color = "Blue"


        ### Check for collisions between the balls ####
        # for j in range(i + 1, len(ListPart)):
        #     # Check for collision
        #     if p[i].distance_collision(p[j]) < 20:
        #         # We keep in memory the first speed
        #         vx1 = p[i].vx
        #         vy1 = p[i].vy
        #         vx2 = p[j].vx
        #         vy2 = p[j].vy
        #
        #         nx = p[i].xcoord - p[j].xcoord
        #         ny = p[i].ycoord - p[j].ycoord
        #         nx1 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * nx
        #         ny1 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * ny
        #         nx2 = ((vx2 * nx + vy2 * ny) / (nx * nx + ny * ny)) * nx
        #         ny2 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * ny
        #         tx1 = vx1 - nx1
        #         ty1 = vy1 - ny1
        #         tx2 = vx2 - nx2
        #         ty2 = vy2 - ny2
        #
        #         # Change the speed between particles
        #         p[j].vx = tx1 + nx2
        #         p[j].vy = ty1 + ny2
        #
        #         p[i].vx = tx2 + nx1
        #         p[i].vy = ty2 + ny1
        #
        #         p[i].touched += 1
        #         p[j].touched += 1
        #
        #         # Start of relfexion about visualizing the gradient of contact (to modify)
        #         if p[i].touched == 1:
        #             p[i].color = "Yellow"
        #         if p[j].touched == 1:
        #             p[j].color = "Yellow"
        #
        #         if p[i].touched > 1:
        #             p[i].color = "Orange"
        #         if p[j].touched > 1:
        #             p[j].color = "Orange"
        #
        #         if p[i].touched >= 5:
        #             p[i].color = "Red"
        #         if p[j].touched >= 5:
        #             p[j].color = "Red"
        #
        #     else:
        #         if (p[i].xcoord - p[j].xcoord) > 20:
        #             p[j].ComputeTraj([0, height / 2])

                ##Trying to create the collision angle to reset properly the direction
                # converter = math.pi / 180  # to convert degrees in radians
                # if nx == 0:
                #     p[j].angle = math.pi / 2
                # else:
                #     p[j].angle = math.atan(ny / nx)

                # Replace them so as to avoid overlapping
                # p[j].xcoord += random.random()*7
                # p[j].ycoord += random.random()*7
                # p[i].xcoord -= random.random()*7
                # p[i].ycoord -= random.random()*7

                # if (interface.find_overlapping(p[i].xcoord, p[i].ycoord, p[j].xcoord, p[j].ycoord) == 0):
                #     p[j].ComputeTraj([0, height / 2])
                # else:
                #     p[j].xcoord += random.random() * 5
                #     p[j].ycoord += random.random() * 5

    # To reduce the speed of simulation
    Simulation.after(20, deplacement)

    particles_out = len(part_out)
    print(particles_out)

    # Stop the code if everyone is out
    if len(part_out) == len(p):
        print("Everyone is out of the room")
        exit()


def suppr():
    interface.delete('all')


particles = CreaPart(50)
# ListPart = particles
ListPart = CreaCrowd(particles)
deplacement()

# On lance la boucle principale:
Simulation.mainloop()
