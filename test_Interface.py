import math
import random
from datetime import datetime
from time import *
from timeit import default_timer
from tkinter import *

import pyautogui
from csv import writer, DictWriter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from analyse import analyse
from environment import *
import numpy as np
from matplotlib import pyplot as plt

from People import *
from environment import *
from theory import theory

### VARIABLES
w_porte = 50
X_obstacle = 500
w_obstacle = 50
# parameters = [""]
# Will contains [Nbr particules, Nbr part_out, Temps d'evac, Temps Théorique, Type Pop, Setup Pop, Position Obstacle x puis y]
dict_param = {}

part_out = []
ListPart = []
world = Room()  # The aim is to use it for everything linked to the creation of the room etc
ListObstacles = Room().ListObstacles
coord_sortie = [0, world.height / 2]
coord_obstacle = [X_obstacle, (int)(world.height / 2)]
Dsortie = 0.0
start = 0.0
str_time = ''
double_time = 0.0
timeTheory = 0.0
t_sortie = 0.0
dt = 0.01
BOO = False

##SETUP
# On cree une fenetre et un canevas:

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

interface = Canvas(Simulation, width=world.width, height=world.height, bd=0, bg="white", cursor="cross")
interface.grid(row=1, column=1)

interface2 = Canvas(Simulation, width=world.width / 2, height=world.height / 2, bd=0, bg="white", cursor="cross")
interface2.grid(row=1, column=2)

##### Trying to set up the screen of simulation
Frame2 = Frame(Simulation, borderwidth=5, relief=SUNKEN, height=50, width=100)
Frame2.grid(row=2, column=1)

##Variables attached to Simulation
example = StringVar(Frame2, name="example")
example.set('Choisissez le Nombre de Particules :')
result = StringVar(Frame2, name="result")
result.set('Nombre de Particules sorties :')
varDisplay = StringVar(Frame2, name="varDisplay")

crowd_selec = StringVar(Frame2, name="crowd_selec")
crowd_selec.set('Choisissez la position de la Population :')
crowd_setup = StringVar(Frame2, name="crowd_setup", value="Aléatoire")  # Value =1 enables to unchecked the radiobutton

crowd_selec2 = StringVar(Frame2, name="crowd_selec2")
crowd_selec2.set('Choisissez le type de Population :')
crowd_type = StringVar(Frame2, name="crowd_type", value="Homogène")  # Value =1 enables to unchecked the radiobutton

Bool_obs = StringVar(Frame2, name="Bool_obs")
Bool_obs.set("Choississez la présence ou non d'un obstacle :")
Bool_obstacle = BooleanVar(Frame2, name="Bool_obstacle", value="True")

Nbr_particles = IntVar(interface, name="Nbr_particles")  # Variable who will contain the input Number
Nbr_part_out = IntVar(interface, name="Nbr_part_out")

## Label d'affichage et setup de leur positions
examplelabel = Label(Frame2, textvariable=example, width=52)
resultlabel = Label(Frame2, textvariable=result)
chronolabel = Label(Frame2, text="TEMPS", fg="black", font="Verdana 15 bold")
varialabel = Label(Frame2, textvariable=varDisplay, font="Verdana 8 bold")

examplelabel.grid(row=2, column=1)
resultlabel.grid(row=3, column=1)
chronolabel.grid(row=1, column=1)
varialabel.grid(row=1, column=0)

sp = Spinbox(Frame2, from_=0, to_=100, width=10)
sp.grid(row=2, column=2)


def graph():
    fig = Figure()
    global ListPart
    l = 0
    k = 0
    j = 0

    if (str)(interface.getvar(name="crowd_type")) == "Hétérogène":
        for i in range(0, len(ListPart)):
            if ListPart[i].name == "Enfant":
                k = k + 1
            if ListPart[i].name == "Adulte":
                j = j + 1
            if ListPart[i].name == "Ancien":
                l = l + 1
        print(k)
        t = ("Enfant", "Adulte", "Ancien")
        Y = (k, j, l)
        fig.add_subplot(111).plot(t, Y)
        canvas = FigureCanvasTkAgg(fig, master=Simulation)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=2)
    else:
        pass
        ## Because in this case we have a pop which is Homogeneous

    # analyse()


# Function to display some data
def lancer():
    ##To get the value
    global ListPart

    interface.setvar(name="Nbr_particles", value=sp.get())
    example.set("Nombre d'individus :" + interface.getvar(name="Nbr_particles"))
    print("Nombre d'individus", interface.getvar(name="Nbr_particles"))
    particles = People.CreaPart((int)(interface.getvar(name="Nbr_particles")), world.width, world.height,
                                (str)(interface.getvar(name="crowd_type")))

    ListPart = People.CreaCrowd(particles, (str)(interface.getvar(name="crowd_setup")), world.width, world.height)
    chilling()  # Particles move in every direction
    graph()
    # # Get the real value of the number of particles
    # if (int)(sp.get()) != 0:
    #     start = default_timer()  # NEED TO STAY HERE, so as to neglect the initialisation
    #     deplacement()


def evacuate():
    ## Create an alert and makes everyone move towards the exit
    global start
    global BOO

    start = default_timer()
    BOO = True  # States that the evacuation is occurring

    # Launch the evacuation
    deplacement()
    # Display some parameters
    varDisplay.set("Paramètres : " + '\n' "- Position de l'obstacle (x,y) : " + str(X_obstacle) + ' , ' + str(
        (int)(world.height / 2))
                   + '\n'  "| Type =" + (str)(interface.getvar(name="crowd_type")) + " | Setup =" + (str)(
        interface.getvar(name="crowd_setup")))

def screen():
    # Take automatic screenshot
    if 5.0 < double_time < 5.1:
        print("It's past 3 seconds")
        im = pyautogui.screenshot(region=(5, 80, (world.width / 2), world.height))
        ## To modify if you wants to take screens automaticcally into your documents
        im.save(
            r'C:\Users\sebas\Documents\INSA\3A\S2\PST\Screens_Modele\Without_Obst\Hétérogènes\Selfish\Evac_Social_Ordered_N' + str(
                len(ListPart)) + '.png')


def screenShoot():
    print("I took a screen at :" + str(double_time))
    im = pyautogui.screenshot(region=(5, 80, (world.width / 2), world.height + 70))
    ## To modify if you wants to take screens automaticcally into your documents
    im.save(
        r'C:\Users\sebas\Documents\INSA\3A\S2\PST\Screens_Modele\Without_Obst\Hétérogènes\Selfish\Evac_Social_Ordered_N' + str(
            len(ListPart)) + '_manual' + '.png')


def refresh():
    ## To update the screen of display

    global timeTheory

    interface.setvar(name="Nbr_part_out", value=len(part_out))
    result.set("Nombre d'individus sorties :" + (str)(
        interface.getvar(name="Nbr_part_out")))  # Don't know why we need to concatenate
    print("Nombre d'individus sorties :", interface.getvar(name="Nbr_part_out"))
    timeTheory = theory(interface.getvar(name="Nbr_particles"), w_porte, world.width, world.height, ListPart, Dsortie)

    ###Doesn't Work....####
    # fig1 = Figure()
    # Y = []
    # X = []
    # newY = []
    # for i in range(len(part_out)):
    #     # print(part_out[i].time)
    #     # if i > 1 and (part_out[i].time) == (part_out[i - 1].time) :
    #     #     Y.__setitem__(i - 1, Y[i - 1] + 1)
    #     # else:
    #         Y.append(1)
    #         X.append(int(part_out[i].time))
    #
    # # for i in range(len(X)):
    # #     X_int = list(map(int, X))
    # #     if i>1 and X_int[i-1]==X_int[i] and len(X)==len(Y) :
    # #         X_int.pop(i)
    # #         Y[i-1] += 1
    # #         Y.pop(i)
    #
    # Tab = [X, Y]
    # print(Tab)
    #
    # fig1.add_subplot(111).plot(X, Y)
    # canvas = FigureCanvasTkAgg(fig1, master=Simulation)  # A tk.DrawingArea.
    # canvas.draw()
    # canvas.get_tk_widget().grid(row=1, column=2)

    ### This part can be useful don't erase it : Shows how to write in an external document
    # with open('test.csv','w',newline='') as f :
    #     for i in range(len(X)):
    #         writer = csv.writer(f)
    #         writer.writerows(Tab)


def select():
    print(Bool_obstacle.get())
    print(crowd_setup.get())
    print(crowd_type.get())


##Creation of RadioButton to select how to study the room evacuation :
obs_label = Label(Frame2, textvariable=Bool_obs)
Robs1 = Radiobutton(Frame2, text="Non", variable=Bool_obstacle, value="False", command=select)
Robs2 = Radiobutton(Frame2, text="Oui", variable=Bool_obstacle, value="True", command=select)
obs_label.grid(row=4, column=0)
Robs1.grid(row=4, column=1, padx=(10, 0))
Robs2.grid(row=4, column=2)

crowdlabel = Label(Frame2, textvariable=crowd_selec)
Rpos1 = Radiobutton(Frame2, text="Population Ordonnée", variable=crowd_setup, value="Ordonnée", command=select)
Rpos2 = Radiobutton(Frame2, text="Population Aléatoire", variable=crowd_setup, value="Aléatoire", command=select)
crowdlabel.grid(row=5, column=0)
Rpos1.grid(row=5, column=1, padx=(10, 0))
Rpos2.grid(row=5, column=2)

crowdlabel2 = Label(Frame2, textvariable=crowd_selec2)
Rtype1 = Radiobutton(Frame2, text="Population Hétérogène", variable=crowd_type, value="Hétérogène", command=select)
Rtype2 = Radiobutton(Frame2, text="Population Homogène", variable=crowd_type, value="Homogène", command=select)
crowdlabel2.grid(row=6, column=0)
Rtype1.grid(row=6, column=1, padx=(10, 0))
Rtype2.grid(row=6, column=2)

# Creation of a Button "Launch":
Bouton_Lancer = Button(Frame2, text='Lancer', command=lancer, activebackground="RED")
Bouton_Lancer.grid(row=7, column=0)  # We add the button to the display of interface tk

# Creation of a Button "Evacuate":
Bouton_Lancer = Button(Frame2, text='Evacuer', command=evacuate, activebackground="RED")
Bouton_Lancer.grid(row=7, column=1)  # We add the button to the display of interface tk

# Creation of a Button "Refresh":
Bouton_Refresh = Button(Frame2, text='Rafraîchir', command=refresh, activebackground="RED")
Bouton_Refresh.grid(row=7, column=2)  # We add the button to the display of interface tk

Bouton_Graph = Button(Frame2, text='Graphique', command=graph, activebackground="RED")
Bouton_Graph.grid(row=8, column=1)  # We add the button to the display of interface tk

# Creation of a Button "Refresh":
Bouton_Screen = Button(Frame2, text='Screenshot', command=screenShoot, activebackground="RED")
Bouton_Screen.grid(row=8, column=0)  # We add the button to the display of interface tk


###########
# Function to take the time needed to get out of the room
def updateTime():
    global str_time
    global double_time
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = '%d:%02d:%02d' % (hours, minutes, seconds)
    chronolabel['text'] = str_time

    # To have a double of the time
    time_converter = seconds + minutes * 60 + hours * 3600
    double_time = float("{:.3f}".format(time_converter))
    # print("This is the time in double :" + str(double_time) + " en secondes ")

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


# Compute and give the adapted speed for the particles to reach the door
def ComputeTraject(my_particles):
    global Dsortie
    for i in range(0, len(my_particles)):
        # Compute the distance
        Dsortie = [my_particles[i].xcenter - coord_sortie[0], my_particles[i].ycenter - coord_sortie[1]]
        # print(D)

        # Give the adapted speed to each particle
        my_particles[i].vx = my_particles[i].speed * (coord_sortie[0] - my_particles[i].xcenter) / math.sqrt(
            (my_particles[i].xcenter - coord_sortie[0]) ** 2 + (my_particles[i].ycenter - coord_sortie[1]) ** 2)
        my_particles[i].vy = my_particles[i].speed * (coord_sortie[1] - my_particles[i].ycenter) / math.sqrt(
            (my_particles[i].xcenter - coord_sortie[0]) ** 2 + (my_particles[i].ycenter - coord_sortie[1]) ** 2)


# Create the environment
def CreateEnv():
    # Create the room
    interface.create_rectangle(20, 20, world.width - 20, world.height - 20, outline="red", width=5)
    interface.grid()
    # Create the door
    interface.create_line(20, ((world.height - w_porte) / 2), 20, ((world.height + w_porte) / 2), fill="green", width=5)
    interface.create_line(X_obstacle, (world.height / 2 - w_obstacle), X_obstacle, (world.height / 2 + w_obstacle),
                          fill="black",
                          width=5)
    ## Create the wall
    interface.create_rectangle(0, (world.height / 2 - w_porte), 20, (world.height / 2 + w_porte), fill="green", width=5)
    interface.grid()

    ## Add obstacles to the room (they are created in the class Room)
    for i in range(len(ListObstacles)):
        ## Just to see if it is working
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

    global t_sortie

    p = ListPart
    # ComputeTraject(p)
    updateTime()  # So as to get the real time
    CreateEnv()
    collision(p, BOO)

    for i in range(0, len(p)):

        b = interface.create_oval((p[i].xcenter - p[i].radius), (p[i].ycenter - p[i].radius),
                                  (p[i].xcenter + p[i].radius), (p[i].ycenter + p[i].radius), fill=p[i].color)

        interface.create_line(p[i].xcenter, p[i].ycenter, p[i].xcenter + p[i].vx, p[i].ycenter + p[i].vy,
                              fill='black', arrow="last", width=5)
        # interface.grid()

        p[i].ComputeTraj([0, random.random() * (w_porte) / 2 + (world.height - w_porte) / 2])

        if (p[i].Distance([0, (world.height - w_porte) / 2])) < p[i].Distance([0, (world.height + w_porte) / 2]):
            p[i].ComputeTraj([0, random.random() * (w_porte) / 2 + (world.height - w_porte) / 2])
        else:
            p[i].ComputeTraj([0, random.random() * (w_porte) / 2 + (world.height) / 2])

        # Check for bouncing on the walls or going through the door

        # Speed reduced to 0 outside of the room
        # if (interface.coords(b)[0]< 25) & ((world.height / 2 - w_porte) < p[i].ycenter < (world.height / 2 + w_porte)):
        #     p[i].vx, p[i].vy = [-1, 0]
        #
        # if interface.coords(b)[3] > world.height - 25:
        #     p[i].vy = -p[i].vy
        #
        # if interface.coords(b)[1] < 25:
        #     p[i].vy = -p[i].vy
        #
        # if interface.coords(b)[2] > world.width - 25:
        #     p[i].vx = -p[i].vx
        #
        # if interface.coords(b)[0] < 20:
        #     if (world.height / 2 - w_porte) < interface.coords(b)[1] < (world.height / 2 + w_porte) - 20:
        #         p[i].vx, p[i].vy = [-1, 0]
        #         p[i].color = "green"
        #         p[i].time = str_time[-2:]
        #         # print(p[i].name + "sorti en : " + p[i].time)
        #         if p[i] not in part_out:
        #             part_out.append(p[i])
        #     else:
        #         p[i].vx = -p[i].vx

        # le mur
        # if 100 < interface.coords(b)[0] < 105:
        #     if (world.height / 2 - w_obstacle) - 20 < interface.coords(b)[1] < (world.height / 2 + w_obstacle):
        #         if p[i].Distance([100, (world.height / 2 - w_obstacle)]) > p[i].Distance(
        #                 [100, (world.height / 2 + w_obstacle)]):
        #             [p[i].vx, p[i].vy] = [0, -(p[i].vy + p[i].vx)]
        #             p[i].color = "black"
        #         else:
        #             [p[i].vx, p[i].vy] = [0, +(p[i].vy + p[i].vx)]
        #             p[i].color = "blue"

        ###FOR ME
        ## Was used to compute the old speed
        # p[i].xcenter = p[i].xcenter + p[i].vx
        # p[i].ycenter = p[i].ycenter + p[i].vy

        # ## Check for collisions between the balls ####
        # for j in range(0, len(ListPart)):
        #     # Check for collision
        #     if (p[i].distance_collision(p[j]) <= 20):
        #         if (p[i].Distance([0, world.height / 2]) <= p[j].Distance([0, world.height / 2])):
        #             if p[i].xcoord<0:
        #                 break
        #             p[i].xcenter = p[i].xcenter + p[i].vx
        #             p[i].ycenter = p[i].ycenter + p[i].vy
        #             print(p[i].vy)
        #             p[j].xcoord = p[j].xcoord  # Stays behind the particle closer to the door
        #             p[j].ycoord = p[j].ycoord
        #             # p[i].color = "Red"
        #             # if p[i].distance_collision(p[j]) > 20:
        #             #     print("It's finished")
        #             #     break
        #         else:
        #             if p[i].xcenter < 0:
        #                 break
        #             p[j].xcenter = p[j].xcenter + p[j].vx
        #             p[j].ycenter = p[j].ycenter + p[j].vy
        #             p[i].xcenter = p[i].xcenter
        #             p[i].ycenter = p[i].ycenter
        #             p[j].color = "Blue"

        # ### Check for collisions between the balls ####
        # for j in range(i + 1, len(ListPart)):
        # #     # Check for collision
        #     if p[i].distance_collision(p[j]) < (p[i].radius + p[j].radius):
        #         ### AVEC CES DEUX LIGNES ON RETROUVE UN MODELE SIMPLE DE COLLISION FONCTIONNANT###
        #         p[i].vx, p[j].vx = p[j].vx, p[i].vx
        #         p[i].vy, p[j].vy = p[j].vy, p[i].vy
        #
        #         p[i].touched += 1
        #         p[j].touched += 1
        #         # Start of relfexion about visualizing the gradient of contact (to modify)
        #         if p[i].touched == 1:
        #             p[i].color = "Yellow"
        #         if p[j].touched == 1:
        #             p[j].color = "Yellow"
        #         if p[i].touched > 1:
        #             p[i].color = "Orange"
        #         if p[j].touched > 1:
        #             p[j].color = "Orange"
        #         if p[i].touched >= 5:
        #             p[i].color = "Red"
        #         if p[j].touched >= 5:
        #             p[j].color = "Red"
        #     else:
        #         if (p[i].xcenter - p[j].ycenter) > p[i].radius+p[j].radius +30: #Trying to create inertia
        #             p[j].ComputeTraj([0, height / 2])
        ###ABOVE FOR ME

        ### MODELE EGOISTE (enlever) LAISSER PASSER (laisser) ###
        ## Check for collisions between the balls ####
        # for j in range(0, len(ListPart)):
        #     # Check for collision
        #     if (p[i].distance_collision(p[j]) <= p[i].radius + p[j].radius):
        #         if (p[i].Distance([0, world.height / 2]) <= p[j].Distance([0, world.height / 2])):
        #             if p[i].xcenter < 20:
        #                 break
        #             p[i].xcenter = p[i].xcenter + p[i].vx * dt
        #             p[i].ycenter = p[i].ycenter + p[i].vy * dt
        #             # print(p[i].vy)
        #             p[j].xcenter = p[j].xcenter # Stays behind the particle closer to the door
        #             p[j].ycenter = p[j].ycenter
        #             p[i].color = "Red"
        #             if p[i].distance_collision(p[j]) > 20:  # To stop computing when they're afar
        #                 break
        #         else:
        #             if p[i].xcenter < 20:
        #                 break
        #             p[j].xcenter = p[j].xcenter + p[j].vx * dt
        #             p[j].ycenter = p[j].ycenter + p[j].vy * dt
        #             p[i].xcenter = p[i].xcenter
        #             p[i].ycenter = p[i].ycenter
        #             p[j].color = "Blue"

    # To reduce the speed of simulation
    Simulation.after(1000, deplacement)
    screen()

    # Stop the code if everyone is out
    if len(part_out) == len(p):

        if t_sortie == 0.0:  # Afin de n'avoir qu'une seule fois le temps final et pas de mise à jour
            t_sortie = double_time

            refresh()  ## Définit le timeTheory
            print("Temps Théorique redef")

            ### Writing of the parameters in Excel
            # parameters.extend([
            #     str(len(p)), str(len(part_out)),
            #     str(t_sortie), str(timeTheory),
            #     str(interface.getvar(name="crowd_type")), str(interface.getvar(name="crowd_setup")),
            #     str(coord_obstacle[0]), str(coord_obstacle[1])
            # ])
            field_names = ['Nbr particules', 'Nbr part_out', "Temps d'evac", 'Temps Théorique', 'Type Pop', 'Setup Pop',
                           'Obstacle', 'Position Obstacle (x,y)']
            dict_param = {'Nbr particules': len(p), 'Nbr part_out': len(part_out), "Temps d'evac": str(t_sortie),
                          'Temps Théorique': str(timeTheory), 'Type Pop': str(interface.getvar(name="crowd_type")),
                          'Setup Pop': str(interface.getvar(name="crowd_setup")),
                          'Obstacle': str(interface.getvar(name="Bool_obstacle")),
                          'Position Obstacle (x,y)': coord_obstacle}

            with open('crowd_data.csv', 'a') as f:
                # writer_object = writer(f)
                # writer_object.writerow(dict)

                # You will get a object of DictWriter
                dictwriter_object = DictWriter(f, fieldnames=field_names)
                # Pass the dictionary as an argument to the Writerow()
                dictwriter_object.writerow(dict_param)

                f.close()

            ####

        print("And all of them get out in " + (str)(str_time) + "seconds and to be more precise :" + str(
            t_sortie) + "seconds")

        example.set(
            "Tout le monde est sorti, avec N =" + str(interface.getvar(name="Nbr_particles"))
            + '\n' "En " + str(t_sortie) + "seconds")
        result.set("Nombre d'individus sorties :" + str(interface.getvar(name="Nbr_part_out"))
                   + '\n' "Temps total théorique nécessaire pour sortir : " '\n' + str(timeTheory) + "secondes")
        Frame2.update()  # To refresh the display and see the changes

        # exit()


def suppr():
    interface.delete('all')


# GOAL : Create an environnement before the alert
def chilling():
    interface.delete('all')

    p = ListPart
    # ComputeTraject(p)

    CreateEnv()
    collision(p, BOO)

    for i in range(0, len(p)):
        b = interface.create_oval((p[i].xcenter - p[i].radius), (p[i].ycenter - p[i].radius),
                                  (p[i].xcenter + p[i].radius), (p[i].ycenter + p[i].radius), fill=p[i].color)
        interface.create_line(p[i].xcenter, p[i].ycenter, p[i].xcenter + p[i].radius * p[i].vx,
                              p[i].ycenter + p[i].radius * p[i].vy,
                              fill='Black', arrow="last", width=2)
        interface.grid()

        # p[i].ComputeTraj([world.width/2, world.height / 2])

        # Check for bouncing on the walls or going through the door

        # Speed reduced to 0 outside of the room
        # if (p[i].xcenter < 25) & ((world.height / 2 - w_porte) < p[i].ycenter < (world.height / 2 + w_porte)):
        #     p[i].vx, p[i].vy = [0, 0]
        #
        # if (p[i].ycenter + p[i].radius) > world.height - 30:
        #     p[i].vy = -p[i].vy
        #
        # if (p[i].ycenter - p[i].radius) < 30:
        #     p[i].vy = -p[i].vy
        #
        # if (p[i].xcenter + p[i].radius) > world.width - 30:
        #     p[i].vx = -p[i].vx
        #
        # if (p[i].xcenter - p[i].radius) < 30:
        #     if (world.height / 2 - w_porte) < interface.coords(b)[1] < (world.height / 2 + w_porte) - 20:
        #         p[i].vx, p[i].vy = [-1, 0]
        #         p[i].color = "green"
        #         if p[i] not in part_out:
        #             part_out.append(p[i])
        #     else:
        #         p[i].vx = -p[i].vx

        ## Not Useful anymore :
        # # le mur
        # if p[i].CollisionObstacle([100, world.height / 2]) < p[i].radius + 5:
        #     if (world.height / 2 - w_porte) - 20 < interface.coords(b)[1] < (world.height / 2 + w_porte):
        #         p[i].vx, p[i].vy = [-p[i].vx, p[i].vy]

    Simulation.after(20, chilling)


def collision(p, bool):
    ### Check for collisions between the balls ####
    for i in range(len(p)):
        dans_la_porte = (p[i].xcenter - p[i].radius) < 50 & (
                (world.height / 2 - w_porte) < p[i].ycenter < (world.height / 2 + w_porte))
        dans_la_salle = (p[i].ycenter + p[i].radius < world.height - 25) | (p[i].ycenter - p[i].radius > 25) | (
                p[i].xcenter + p[i].radius < world.width - 25) | (p[i].xcenter - p[i].radius > 25)
        if dans_la_porte == 1:
            p[i].color = 'green'
            p[i].vx = -1
            p[i].vy = 0
        if dans_la_salle == 0:
            p[i].ComputeTraject([width / 2, height / 2])
            p[i].xcenter, p[i].ycenter = [0, 0]
        else:
            if (p[i].xcenter < 25) & ((world.height / 2 - w_porte) < p[i].ycenter < (world.height / 2 + w_porte)):
                p[i].vx, p[i].vy = [-p[i].vx, p[i].vy]

            if (p[i].ycenter + p[i].radius) > world.height - 30:
                p[i].vy = -p[i].vy

            if (p[i].ycenter - p[i].radius) < 30:
                p[i].vy = -p[i].vy

            if not bool:
                if (p[i].xcenter + p[i].radius) > world.width - 30:
                    p[i].vx = -p[i].vx

            if (p[i].xcenter - p[i].radius) < 30:
                if (world.height / 2 - w_porte) < (p[i].ycenter - p[i].radius) < (world.height / 2 + w_porte) - 20:
                    if bool:
                        p[i].vx, p[i].vy = [-1, 0]
                        p[i].color = "green"
                        if p[i] not in part_out:
                            part_out.append(p[i])
                else:
                    p[i].vx = -p[i].vx

            # # BAS
            # if p[i].ycenter + p[i].radius > world.height - 25:
            #     p[i].ComputeTraj([(world.width / 2), (world.height / 2)])
            # # HAUT
            # if p[i].ycenter - p[i].radius < 25:
            #     p[i].ComputeTraj([(world.width / 2), (world.height / 2)])
            # # GAUCHE
            # if p[i].xcenter + p[i].radius > world.width - 25:
            #     p[i].ComputeTraj([(world.width / 2), (world.height / 2)])
            # # DROIT
            # if p[i].xcenter - p[i].radius < 25:
            #     if (world.height / 2 - w_porte) < p[i].ycenter - p[i].radius < (world.height / 2 + w_porte) - 20:
            #         p[i].vx, p[i].vy = [-1, 0]
            #         p[i].color = "green"
            #         p[i].time = str_time[-2:]
            #         # print(p[i].name + "sorti en : " + p[i].time)
            #         if p[i] not in part_out:
            #             part_out.append(p[i])
            #     else:
            #         p[i].ComputeTraj([(world.width / 2), (world.height / 2)])

        # le mur
        if not bool:
            if (X_obstacle < (p[i].xcenter - p[i].radius) < X_obstacle + 5 and p[i].vx < 0) or (
                    X_obstacle - 5 < (p[i].xcenter + p[i].radius) < X_obstacle and p[i].vx > 0):
                if (world.height / 2 - w_obstacle) - 20 < (p[i].ycenter - p[i].radius) < (
                        world.height / 2 + w_obstacle):
                    if p[i].Distance([X_obstacle, (world.height / 2 - w_obstacle)]) > p[i].Distance(
                            [X_obstacle, (world.height / 2 + w_obstacle)]):
                        [p[i].vx, p[i].vy] = [-p[i].vx, p[i].vy]
                        # [p[i].vx, p[i].vy] = [0, -(p[i].vy + p[i].vx)]
                        p[i].color = "Pink"
                    else:  ### Fais rebondir dans les deux cas
                        [p[i].vx, p[i].vy] = [-p[i].vx, p[i].vy]
                        # [p[i].vx, p[i].vy] = [0, +(p[i].vy + p[i].vx)]
                        p[i].color = "blue"
        else:
            if (X_obstacle < (p[i].xcenter - p[i].radius) < X_obstacle + 5 and p[i].vx < 0) or (
                    X_obstacle - 5 < (p[i].xcenter + p[i].radius) < X_obstacle and p[i].vx > 0):
                if (world.height / 2 - w_obstacle) - 20 < (p[i].ycenter - p[i].radius) < (
                        world.height / 2 + w_obstacle):
                    if p[i].Distance([X_obstacle, (world.height / 2 - w_obstacle)]) > p[i].Distance(
                            [X_obstacle, (world.height / 2 + w_obstacle)]):
                        [p[i].vx, p[i].vy] = [0, -(p[i].vy + p[i].vx)]
                        p[i].color = "Pink"
                    else:
                        [p[i].vx, p[i].vy] = [0, (p[i].vy + p[i].vx)]
                        p[i].color = "blue"

        ## So that they still continue to go through the door
        p[i].xcenter = p[i].xcenter + p[i].vx
        p[i].ycenter = p[i].ycenter + p[i].vy



        for j in range(i + 1, len(ListPart)):
            # Check for collision
            # if dans_la_porte==0:

            ## collision with all obstacles
            p[i].CollisionObstacle2(ListObstacles, bool)  # , p[j].CollisionObstacle2(ListObstacles, bool)

            if (p[i].distance_collision(p[j]) < (p[i].radius + p[j].radius)) & (
                    p[j].distance_collision(p[i]) < (p[j].radius + p[i].radius)):
                ### AVEC CES DEUX LIGNES ON RETROUVE UN MODELE SIMPLE DE COLLISION FONCTIONNANT###
                p[i].vx, p[j].vx = p[j].vx, p[i].vx
                p[i].vy, p[j].vy = p[j].vy, p[i].vy

                # # We keep in memory the first speed
                # vx1 = p[i].vx
                # vy1 = p[i].vy
                # vx2 = p[j].vx
                # vy2 = p[j].vy
                #
                # nx = p[i].xcenter - p[j].xcenter
                # ny = p[i].ycenter - p[j].ycenter
                # nx1 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * nx
                # ny1 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * ny
                # nx2 = ((vx2 * nx + vy2 * ny) / (nx * nx + ny * ny)) * nx
                # ny2 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * ny
                # tx1 = vx1 - nx1
                # ty1 = vy1 - ny1
                # tx2 = vx2 - nx2
                # ty2 = vy2 - ny2
                #
                # # Change the speed between particles
                # if tx1 + nx2 != 0:
                #     p[j].vx = (tx1 + nx2) / math.sqrt(tx1 ** 2 + nx2 ** 2)
                # if ty1 + ny2 != 0:
                #     p[j].vy = (ty1 + ny2) / math.sqrt(ty1 ** 2 + ny2 ** 2)
                # if tx2 + nx1 != 0:
                #     p[i].vx = (tx2 + nx1) / math.sqrt(tx2 ** 2 + nx1 ** 2)
                # if ty2 + ny1 != 0:
                #     p[i].vy = (ty2 + ny1) / math.sqrt(ty2 ** 2 + ny1 ** 2)
                #
                # # p[i].xcenter = p[i].xcenter + p[i].vx
                # # p[i].ycenter = p[i].ycenter + p[i].vy
                #
                # p[j].xcenter = p[j].xcenter + p[j].vx
                # p[j].ycenter = p[j].ycenter + p[j].vy
                #
                # p[i].touched += 1
                # p[j].touched += 1
                #
                # #### Start of relfexion about visualizing the gradient of contact (to modify)
                # We keep in memory the first speed
                # vx1 = p[i].vx
                # vy1 = p[i].vy
                # vx2 = p[j].vx
                # vy2 = p[j].vy

                # 1ere methode
                # nx = p[i].xcenter - p[j].xcenter
                # ny = p[i].ycenter - p[j].ycenter
                # nx1 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * nx
                # ny1 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * ny
                # nx2 = ((vx2 * nx + vy2 * ny) / (nx * nx + ny * ny)) * nx
                # ny2 = ((vx1 * nx + vy1 * ny) / (nx * nx + ny * ny)) * ny
                # tx1 = vx1 - nx1
                # ty1 = vy1 - ny1
                # tx2 = vx2 - nx2
                # ty2 = vy2 - ny2
                #
                # # Change the speed between particles
                # if tx1 + nx2 != 0:
                #     p[j].vx = (tx1 + nx2) / math.sqrt(tx1 ** 2 + nx2 ** 2)
                # if ty1 + ny2 != 0:
                #     p[j].vy = (ty1 + ny2) / math.sqrt(ty1 ** 2 + ny2 ** 2)
                # if tx2 + nx1 != 0:
                #     p[i].vx = (tx2 + nx1) / math.sqrt(tx2 ** 2 + nx1 ** 2)
                # if ty2 + ny1 != 0:
                #     p[i].vy = (ty2 + ny1) / math.sqrt(ty2 ** 2 + ny1 ** 2)

                # p[i].xcenter = p[i].xcenter + p[i].vx
                # p[i].ycenter = p[i].ycenter + p[i].vy

                # 2eme methode
                # p[i].col(p[j])

                p[j].xcenter = p[j].xcenter + p[j].vx
                p[j].ycenter = p[j].ycenter + p[j].vy

                p[i].touched += 1
                p[j].touched += 1

                # Start of relfexion about visualizing the gradient of contact (to modify)
                # if p[i].touched == 1:
                #     p[i].color = "Yellow"
                # if p[j].touched == 1:
                #     p[j].color = "Yellow"
                #
                # if p[i].touched > 1:
                #     p[i].color = "Orange"
                # if p[j].touched > 1:
                #     p[j].color = "Orange"
                #
                # if p[i].touched >= 5:
                #     p[i].color = "Red"
                # if p[j].touched >= 5:
                #     p[j].color = "Red"

                #####
                # # Trying to create the collision angle to reset properly the direction
                # converter = math.pi / 180  # to convert degrees in radians
                # if nx == 0:
                #     p[j].angle = math.pi / 2
                # else:
                #     p[j].angle = math.atan(ny / nx)

            # else:
        #     if (p[i].xcenter - p[j].ycenter) > p[i].radius+p[j].radius +30: #Trying to create inertia
        #         # p[j].ComputeTraj([0, height / 2])

# On lance la boucle principale:
Simulation.mainloop()
