import math
import random
from datetime import datetime
from time import *
from timeit import default_timer
from tkinter import *
from People import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from environment import *
import numpy as np
from matplotlib import pyplot as plt


##SETUP
# On cree une fenetre et un canevas:
from environment import *

Simulation = Tk()
Simulation.title("Crowd Simulation")
Simulation.geometry("750x700")
width = 500
height = 500

Frame1 = Frame(Simulation, borderwidth=5, relief=RAISED, height=50, width=50)
Frame1.grid(row=0, column=1)
# SEB
title = Label(Frame1, text="Welcome to the Crowd Simulator !", fg="black", font="Verdana 15 bold", width=35)
title.grid()

interface = Canvas(Simulation, width=width, height=height, bd=0, bg="white", cursor="cross")
interface.grid(row=1, column=1)

interface2 = Canvas(Simulation, width=width, height=height, bd=0, bg="white", cursor="cross")
interface2.grid(row=1, column=2)


##### Trying to set up the screen of simulation
Frame2 = Frame(Simulation, borderwidth=5, relief=SUNKEN, height=50, width=100)
Frame2.grid(row=2, column=1)

##Variables attached to Simulation
example = StringVar(Frame2, name="example")
example.set('Choisissez le Nombre de Particules :')
result = StringVar(Frame2, name="result")
result.set('Nombre de Particules sorties :')

crowd_selec = StringVar(Frame2, name="crowd_selec")
crowd_selec.set('Choisissez le type de Population :')
crowd_type = StringVar(Frame2, name="crowd_type", value="1")  # Value =1 enables to unchecked the radiobutton

Nbr_particles = IntVar(interface, name="Nbr_particles")  # Variable who will contain the input Number
Nbr_part_out = IntVar(interface, name="Nbr_part_out")

examplelabel = Label(Frame2, textvariable=example, width=52)
resultlabel = Label(Frame2, textvariable=result)
chronolabel = Label(Frame2, text="TEMPS", fg="black", font="Verdana 15 bold")
examplelabel.grid(row=2, column=1)
resultlabel.grid(row=3, column=1)
chronolabel.grid(row=1, column=1)

sp = Spinbox(Frame2, from_=0, to_=100, width=10)
sp.grid(row=2, column=2)

### VARIABLES
w_porte = 30
part_out = []
ListPart = []
world = Room()  # The aim is to use it for everything linked to the creation of the room etc
ListObstacles = Room().ListObstacles
coord_sortie = [0, world.height / 2]
start = 0.0
str_time = ""

#####TRASH##############
# Not Useful anymore

# Function to display some data
def lancer():
    ##To get the value
    global ListPart

    interface.setvar(name="Nbr_particles", value=sp.get())
    example.set("Nombre d'individus :" + interface.getvar(name="Nbr_particles"))
    print("Nombre d'individus", interface.getvar(name="Nbr_particles"))
    particles = CreaPart((int)(interface.getvar(name="Nbr_particles")))

    ListPart = CreaCrowd(particles)
    chilling()  # Particles move in every direction

    # # Get the real value of the number of particles
    # if (int)(sp.get()) != 0:
    #     start = default_timer()  # NEED TO STAY HERE, so as to neglect the initialisation
    #     deplacement()


def evacuate():
    ## Create an alert and makes everyone move towards the exit
    global start
    start = default_timer()  # NEED TO STAY HERE, so as to neglect the initialisation
    deplacement()


def resfresh():
    ## To update the screen of display
    interface.setvar(name="Nbr_part_out", value=len(part_out))
    result.set("Nombre d'individus sorties :" + (str)(
        interface.getvar(name="Nbr_part_out")))  # Don't know why we need to concatenate
    print("Nombre d'individus sorties :", interface.getvar(name="Nbr_part_out"))


def graph():
    fig = Figure()
    ListPart
    l=0
    k=0
    j=0
    for i in range (0,len(ListPart)):
        if ListPart[i].name == "Enfant":
            k=k+1
        if ListPart[i].name == "Adulte":
            j=j+1
        if ListPart[i].name == "Ancien":
            l=l+1
    print(k)
    t = ("Enfant","Adulte","Ancien")
    Y=(k,j,l)
    fig.add_subplot(111).plot(t, Y)
    canvas = FigureCanvasTkAgg(fig, master=Simulation)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=1,column=2)

def select():
    print(crowd_type.get())


##Creation of RadioButton to select how to study the room evacuation :
crowdlabel = Label(Frame2, textvariable=crowd_selec)
R1 = Radiobutton(Frame2, text="Population Homogène", variable=crowd_type, value="Homogène", command=select)
R2 = Radiobutton(Frame2, text="Population Aléatoire", variable=crowd_type, value="Aléatoire", command=select)
crowdlabel.grid(row=4, column=0)
R1.grid(row=4, column=1, padx=(10, 0))
R2.grid(row=4, column=2)

# Creation of a Button "Launch":
Bouton_Lancer = Button(Frame2, text='Lancer', command=lancer, activebackground="RED")
Bouton_Lancer.grid(row=5, column=0)  # We add the button to the display of interface tk

# Creation of a Button "Evacuate":
Bouton_Lancer = Button(Frame2, text='Evacuer', command=evacuate, activebackground="RED")
Bouton_Lancer.grid(row=5, column=1)  # We add the button to the display of interface tk

# Creation of a Button "Refresh":
Bouton_Refresh = Button(Frame2, text='Rafraîchir', command=resfresh, activebackground="RED")
Bouton_Refresh.grid(row=5, column=2)  # We add the button to the display of interface tk

Bouton_Graph = Button(Frame2, text='Graphique', command=graph, activebackground="RED")
Bouton_Graph.grid(row=6, column=1)  # We add the button to the display of interface tk

###########
# Function to take the time needed to get out of the room
def updateTime():
    global str_time
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    chronolabel['text'] = str_time
    chronolabel.after(1000, updateTime)


# define the countdown func. (so as to count the number of people getting out in a limited amount of time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the Building!!')


# To uncomment so as to use it
# # input time in seconds
# t = input("Enter the time in seconds: ")
#
# # function call
# countdown(int(t))


# Creation of the list of people
def CreaPart(number):
    my_particles = []
    possible_types = ["kid", "adult", "old"]
    for i in range(0, number):
        xcenter = (world.width - 40) * random.random() + 30
        ycenter = (world.height - 40) * random.random() + 30

        D = [xcenter - coord_sortie[0], ycenter - coord_sortie[1]]
        # D_norm=D/math.sqrt((xcoord - coord_sortie[0]) ** 2 + (ycoord - coord_sortie[1]) ** 2)
        # print(D)

        # vx = 1 * (coord_sortie[0] - xcenter) / math.sqrt(
        #     (xcenter - coord_sortie[0]) ** 2 + (ycenter - coord_sortie[1]) ** 2)
        # vy = 1 * (coord_sortie[1] - ycenter) / math.sqrt(
        #     (xcenter - coord_sortie[0]) ** 2 + (ycenter - coord_sortie[1]) ** 2)

        vx = random.random() * 5 - 1
        vy = random.random() * 5 - 1
        # vx, vy = [0, 0]

        k = random.randrange(len(possible_types))

        type = possible_types[k]

        p = People(xcenter, ycenter, vx, vy, type)
        print(p)
        my_particles.append(p)
    return my_particles


##Deal with the overlapping at the creation of the particles
def CreaCrowd(my_particles):
    ### RANDOM CROWD ####
    if (str)(interface.getvar(name="crowd_type")) == "Aléatoire":
        for i in range(0, len(my_particles)):
            # Check it is inside the room (but not functional)
            if (25 + my_particles[i].radius) > my_particles[i].xcenter or my_particles[i].xcenter > (
                    width - 50 - my_particles[i].radius):
                my_particles[i].xcenter = (width - 80) * random.random() + 30
            if (25 + my_particles[i].radius) > my_particles[i].ycenter or my_particles[i].ycenter > (
                    height - 50 - my_particles[i].radius):
                my_particles[i].ycenter = (height - 80) * random.random() + 30

            # Checking the overlapping between particles
            for j in range(0, len(my_particles)):
                if my_particles[i].distance_collision(my_particles[j]) < (
                        my_particles[i].radius + my_particles[j].radius):
                    my_particles[i].xcenter = (world.width - 80) * random.random() + 30
                    my_particles[i].ycenter = (world.height - 80) * random.random() + 30

    ## ORDERED CROWD ####
    if (str)(interface.getvar(name="crowd_type")) == "Homogène":

        # Initialisation des particules sur forme de grille
        i = 0
        j = 4
        for k in range(0, len(my_particles)):
            # my_particles[k].vx = 0
            # my_particles[k].vy = 0
            # my_particles[k].xcenter = 40
            # my_particles[k].ycenter = 40
            if 40 * i <= 420:
                i = i + 1
                my_particles[k].xcenter = 40 * i
                my_particles[k].ycenter = 40 * j
            else:
                i = 1
                j = j + 1
                my_particles[k].xcenter = 40
                my_particles[k].ycenter = 40 * j

    return my_particles


# Compute and give the adapted speed for the particles to reach the door
def ComputeTraject(my_particles):
    for i in range(0, len(my_particles)):
        # Compute the distance
        D = [my_particles[i].xcenter - coord_sortie[0], my_particles[i].ycenter - coord_sortie[1]]
        # print(D)

        # Give the adapted speed to each particle
        my_particles[i].vx = 10 * (coord_sortie[0] - my_particles[i].xcenter) / math.sqrt(
            (my_particles[i].xcenter - coord_sortie[0]) ** 2 + (my_particles[i].ycenter - coord_sortie[1]) ** 2)
        my_particles[i].vy = 10 * (coord_sortie[1] - my_particles[i].ycenter) / math.sqrt(
            (my_particles[i].xcenter - coord_sortie[0]) ** 2 + (my_particles[i].ycenter - coord_sortie[1]) ** 2)


# Create the environment
def CreateEnv():
    # Create the room
    interface.create_rectangle(20, 20, world.width - 20, world.height - 20, outline="red", width=5)
    interface.grid()
    # Create the door
    interface.create_line(20, (world.height / 2 - w_porte), 20, (world.height / 2 + w_porte), fill="green", width=5)
    interface.create_line(100, (world.height / 2 - w_porte), 100, (world.height / 2 + w_porte), fill="black", width=4)
    interface.create_rectangle(0, (world.height / 2 - w_porte), 20, (world.height / 2 + w_porte), fill="green", width=5)
    interface.grid()

    ## Add obstacles to the room (they are created in the class Room)
    for i in range(len(ListObstacles)):
        # # Just to see if it is working
        # print(ListObstacles[i])
        if ListObstacles[i].shape == "Rectangle":  ##can be center + or - 10 but I put radius to generalize
            interface.create_rectangle((ListObstacles[i].xcenter - ListObstacles[i].radius),
                                       (ListObstacles[i].ycenter - ListObstacles[i].radius),
                                       (ListObstacles[i].xcenter + ListObstacles[i].radius),
                                       (ListObstacles[i].ycenter + ListObstacles[i].radius),
                                       fill=ListObstacles[i].color)
        elif ListObstacles[i].shape == "Circle":
            interface.create_oval((ListObstacles[i].xcenter - ListObstacles[i].radius),
                                  (ListObstacles[i].ycenter - ListObstacles[i].radius),
                                  (ListObstacles[i].xcenter + ListObstacles[i].radius),
                                  (ListObstacles[i].ycenter + ListObstacles[i].radius), fill=ListObstacles[i].color)


# Creation of the Movement
def deplacement():
    interface.delete('all')

    p = ListPart
    # ComputeTraject(p)

    updateTime()  # So as to get the real time
    CreateEnv()
    collision(p)

    for i in range(0, len(p)):

        b = interface.create_oval((p[i].xcenter - p[i].radius), (p[i].ycenter - p[i].radius),
                                  (p[i].xcenter + p[i].radius), (p[i].ycenter + p[i].radius), fill=p[i].color)
        interface.grid()

        p[i].ComputeTraj([0, world.height / 2])

        # Check for bouncing on the walls or going through the door

        # Speed reduced to 0 outside of the room
        if (0 < p[i].xcenter < 15) & ((world.height / 2 - w_porte) < p[i].ycenter < (world.height / 2 + w_porte)):
            p[i].vx, p[i].vy = [0, 0]

        if interface.coords(b)[3] > world.height - 25:
            p[i].vy = -p[i].vy

        if interface.coords(b)[1] < 25:
            p[i].vy = -p[i].vy

        if interface.coords(b)[2] > world.width - 25:
            p[i].vx = -p[i].vx

        if interface.coords(b)[0] < 20:
            if (world.height / 2 - w_porte) < interface.coords(b)[1] < (world.height / 2 + w_porte) - 20:
                p[i].vx, p[i].vy = [-1, 0]
                p[i].color = "green"
                if p[i] not in part_out:
                    part_out.append(p[i])
            else:
                p[i].vx = -p[i].vx

        # le mur
        if 100 < interface.coords(b)[0] < 105:
            if (world.height / 2 - w_porte) - 20 < interface.coords(b)[1] < (world.height / 2 + w_porte):
                if p[i].Distance([100, (world.height / 2 - w_porte)]) > p[i].Distance(
                        [100, (world.height / 2 + w_porte)]):
                    [p[i].vx, p[i].vy] = [0, -(p[i].vy + p[i].vx)]
                    p[i].color = "black"
                else:
                    [p[i].vx, p[i].vy] = [0, +(p[i].vy + p[i].vx)]
                    p[i].color = "blue"

        # ## Check for collisions between the balls ####
        for j in range(0, len(ListPart)):
            # Check for collision
            if (p[i].distance_collision(p[j]) <= p[i].radius + p[j].radius):
                if (p[i].Distance([0, world.height / 2]) <= p[j].Distance([0, world.height / 2])):
                    if p[i].xcoord < 0:
                        break
                    p[i].xcenter = p[i].xcenter + p[i].vx
                    p[i].ycenter = p[i].ycenter + p[i].vy
                    print(p[i].vy)
                    p[j].xcoord = p[j].xcoord  # Stays behind the particle closer to the door
                    p[j].ycoord = p[j].ycoord
                    p[i].color = "Red"
                    if p[i].distance_collision(p[j]) > 20:
                        print("It's finished")
                        break
                else:
                    if p[i].xcenter < 0:
                        break
                    p[j].xcenter = p[j].xcenter + p[j].vx
                    p[j].ycenter = p[j].ycenter + p[j].vy
                    p[i].xcenter = p[i].xcenter
                    p[i].ycenter = p[i].ycenter
                    p[j].color = "Blue"

    # To reduce the speed of simulation
    Simulation.after(20, deplacement)
    particles_out = len(part_out)
    print(particles_out)

    # Stop the code if everyone is out
    if len(part_out) == len(p):
        print("Everyone is out of the room")
        print("And all of them get out in " + (str)(str_time) + "seconds")
        exit()


def suppr():
    interface.delete('all')

# GOAL : Create an environnement before the alerte
def chilling():
    interface.delete('all')

    p = ListPart
    # ComputeTraject(p)

    CreateEnv()
    collision(p)

    for i in range(0, len(p)):

        b = interface.create_oval((p[i].xcenter - p[i].radius), (p[i].ycenter - p[i].radius),
                                  (p[i].xcenter + p[i].radius), (p[i].ycenter + p[i].radius), fill=p[i].color)
        interface.grid()

        # p[i].ComputeTraj([0, world.height / 2])

        # Check for bouncing on the walls or going through the door

        # Speed reduced to 0 outside of the room
        if (0 < p[i].xcenter < 15) & ((world.height / 2 - w_porte) < p[i].ycenter < (world.height / 2 + w_porte)):
            p[i].vx, p[i].vy = [0, 0]

        if interface.coords(b)[3] > world.height - 30:
            p[i].vy = -p[i].vy

        if interface.coords(b)[1] < 30:
            p[i].vy = -p[i].vy

        if interface.coords(b)[2] > world.width - 30:
            p[i].vx = -p[i].vx

        if interface.coords(b)[0] < 20:
            # if (world.height / 2 - w_porte) < interface.coords(b)[1] < (world.height / 2 + w_porte) - 20:
            #     p[i].vx, p[i].vy = [-1, 0]
            #     p[i].color = "green"
            #     if p[i] not in part_out:
            #         part_out.append(p[i])
            # else:
            p[i].vx = -p[i].vx

        ## Not Useful anymore :
        # # le mur
        # if p[i].CollisionObstacle([100, world.height / 2]) < p[i].radius + 5:
        #     if (world.height / 2 - w_porte) - 20 < interface.coords(b)[1] < (world.height / 2 + w_porte):
        #         p[i].vx, p[i].vy = [-p[i].vx, p[i].vy]

    Simulation.after(20, chilling)


def collision(p):
    ### Check for collisions between the balls ####
    for i in range(0, len(p)):

        # le mur
        if 100 < (p[i].xcenter - p[i].radius) < 105:
            if (world.height / 2 - w_porte) - 20 < (p[i].ycenter - p[i].radius) < (world.height / 2 + w_porte):
                if p[i].Distance([100, (world.height / 2 - w_porte)]) > p[i].Distance(
                        [100, (world.height / 2 + w_porte)]):
                    [p[i].vx, p[i].vy] = [0, -(p[i].vy + p[i].vx)]
                    p[i].color = "black"
                else:
                    [p[i].vx, p[i].vy] = [0, +(p[i].vy + p[i].vx)]
                    p[i].color = "blue"

        # collision with all obstacles
        p[i].CollisionObstacle2(ListObstacles)

        ## So that they still continue to go through the door
        p[i].xcenter = p[i].xcenter + p[i].vx
        p[i].ycenter = p[i].ycenter + p[i].vy

        for j in range(i + 1, len(ListPart)):
            # Check for collision
            if p[i].distance_collision(p[j]) < (p[i].radius + p[j].radius):
                # We keep in memory the first speed
                vx1 = p[i].vx
                vy1 = p[i].vy
                vx2 = p[j].vx
                vy2 = p[j].vy

                nx = p[i].xcenter - p[j].xcenter
                ny = p[i].ycenter - p[j].ycenter
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

            # else:
            #     if (p[i].xcenter - p[j].ycenter) > p[i].radius+p[j].radius +30: #Trying to create inertia
            #         # p[j].ComputeTraj([0, height / 2])


##### Old Version to use to work

#     particles = CreaPart((int)(interface.getvar(name="Nbr_particles")))  # The idea after is to put here interface.getvar(name="Nbr_particles") to obtain the real value entered by the user
#     print("It works hereeeee")
#     ListPart = CreaCrowd(particles)
#     deplacement() #Take off the comment to simplify

# On lance la boucle principale:

Simulation.mainloop()
