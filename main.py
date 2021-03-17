from tkinter import *
from tkinter.messagebox import showinfo

import tk as tk

fenetre = Tk()
fenetre.title("Crow Simulation")

Nbr_particles = IntVar(fenetre, name="Nbr_particles")


####

def alert():
    showinfo("alerte", "Bravo!")


menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

####
fenetre['bg'] = 'white'

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE, height=500, width=500)
Frame1.pack(side=TOP, padx=100, pady=100)

# frame 2
Frame2 = Frame(Frame1, borderwidth=2, relief=GROOVE, height=50, width=500)
Frame2.pack(side=BOTTOM, padx=100, pady=100)

# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)

example = StringVar()
examplelabel = Label(Frame2, textvariable=example)
examplelabel.pack()


#####
def recupere():
    ##To get the value
    fenetre.setvar(name="Nbr_particles", value=s.get())
    example.set("Nombre d'individus" + fenetre.getvar(name="Nbr_particles"))
    print("Nombre d'individus", fenetre.getvar(name="Nbr_particles"))


value = StringVar()
value.set("Valeur")
entree = Entry(Frame1, textvariable=value, width=30)
entree.pack()

bouton = Button(Frame1, text="Valider", command=recupere)
bouton.pack(padx=10, pady=10)

s = Spinbox(Frame2, from_=10, to_=100)
s.pack()

bouton2 = Button(Frame2, text="Valider", command=recupere)
bouton2.pack(padx=10, pady=10)

fenetre.config(menu=menubar)
fenetre.mainloop()

# ##### Trying to set up the screen of simulation
# s = Spinbox(Simulation, from_=10, to_=100, text='Choisis le Nombre de Particules', width=10)
# s.pack()
# example = StringVar()
# examplelabel = Label(Simulation,text='Hello' , textvariable=example, width=10)
# examplelabel.pack()
# # ##To get the value
# # interface.setvar(name="int", value=s.get())
# # interface.pack()
