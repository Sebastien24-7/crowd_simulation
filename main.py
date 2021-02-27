from tkinter import *
from tkinter.messagebox import showinfo

fenetre = Tk()
fenetre.title("Crow Simulation")


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

# frame 3 dans frame 2
Frame3 = Frame(Frame1, bg="white", borderwidth=2, relief=GROOVE, height=500, width=50)
Frame3.pack(side=RIGHT, padx=5, pady=5)

# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3", bg="white").pack(padx=10, pady=10)


#####
def recupere():
    showinfo("Alerte", entree.get())


value = StringVar()
value.set("Valeur")
entree = Entry(Frame1, textvariable=value, width=30)
entree.pack()

bouton = Button(Frame1, text="Valider", command=recupere)
bouton.pack()

fenetre.config(menu=menubar)
fenetre.mainloop()
