import matplotlib.pyplot as plt
from test_Interface import *
from People import *

### MODELE DE TOGAWA ###
N = interface.getvar(name="Nbr_particles")  # Nombre de Particules
W = w_porte * 2  # Width of the door
D = (N / ((width * height) / 3779))  # Density of people by meter square (1 meter = 3779 pixels don't from where)

v0 = 1.3  # (m/s) vitesse de marche par défaut et sans effet de foule
vT = v0 * math.pow(D, -0.8)

v = []  # speed of the individuals
for i in range(ListPart):
    v.append(ListPart[i].speed)
vAverage = mean(v)

F = vAverage * W * D  # Flux de personne (débit de pers / sec à l'ouverture)
Fspe = vAverage * D  # Flux de personne (débit spécifique en m^-1.s^-1 )

tevac = []
L = []
for i in range(ListPart):
    L.append(Dsortie)
    tevac.append((N / (Fspe * W)) + (L[i] / vT))  # Temps d'évacuation

t_total = max(tevac)  # Temps total de l'évacuation correspond à la valeur la plus élevée d'évacuation

### MODELE DE FORCE SOCIALE D'HELBING ###
# Force sociale :
# -Terme attractif : Vitesse prévue
# -Terme répulsif : Forces d'Interaction'
