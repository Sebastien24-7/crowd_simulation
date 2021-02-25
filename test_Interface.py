import random
from tkinter import *
from People import People

#On cree une fenetre et un canevas:
Simulation = Tk()
width=500
height=500
interface = Canvas(Simulation,width = width, height = height, bd=0, bg="white")
interface.pack(padx=100,pady=100)
interface.create_rectangle(10,10,width-10,height-10)


#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(Simulation, text ='Quitter', command = Simulation.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

def CreaBalle():
    xcoord = (width-30) * random.random()+10
    ycoord = (height-30) * random.random()+10

    return People(0,'Yellow',xcoord,ycoord,1,10 * random.random(),10 * random.random())

b=CreaBalle()
print(b)
b1=interface.create_oval(b.xcoord,b.ycoord,b.xcoord+20,b.ycoord+20,fill=b.color)

dx = b.vx
dy = b.vy

def deplacement():

        global dx, dy
        if interface.coords(b1)[3] > height-10:
            dy=-dy
        if interface.coords(b1)[3] < 30:
            dy=-dy
        if interface.coords(b1)[2] > width-10:
            dx=-dx
        if interface.coords(b1)[2] < 30:
            dx=-dx

        #On deplace la balle :
        interface.move(b1,dx,dy)
        #On repete cette fonction
        Simulation.after(30,deplacement)



#On cree une balle:
#il faut connecter cette partie avec la classe People
deplacement()
#On lance la boucle principale:
Simulation.mainloop()

