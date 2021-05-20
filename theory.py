import matplotlib.pyplot as plt
from numpy import mean, double

from People import *


# ### MODELE DE TOGAWA ###
# N = interface.getvar(name="Nbr_particles")  # Nombre de Particules
# W = w_porte * 2  # Width of the door
# D = (int(N) / ((width * height) / 3779))  # Density of people by meter square (1 meter = 3779 pixels don't from where)
#
# v0 = 1.3  # (m/s) vitesse de marche par défaut et sans effet de foule
# vT = v0 * math.pow(D, -0.8)
#
# v = []  # speed of the individuals
# for i in range(len(ListPart)):
#     v.append(ListPart[i].speed)
# vAverage = mean(v)
#
# F = vAverage * W * D  # Flux de personne (débit de pers / sec à l'ouverture)
# Fspe = vAverage * D  # Flux de personne (débit spécifique en m^-1.s^-1 )
#
# tevac = []
# L = []
# for i in range(len(ListPart)):
#     L.append(Dsortie)
#     tevac.append((float(N) / (float(Fspe) * float(W))) + (L[i] / vT))  # Temps d'évacuation
#
# t_total = max(tevac)  # Temps total de l'évacuation correspond à la valeur la plus élevée d'évacuation
# print("Temps total théorique nécessaire pour sortir : " + str(t_total) + "secondes")
### Modèle revisité ###
def theory(N, w_porte, W_width, W_height, ListParticles, coord_sortie):
    ### MODELE DE TOGAWA ###
    W = w_porte * 2  # Width of the door
    D = (int(N) / (
            (W_width / 3779) * (
            W_height / 3779)))  # Density of people by meter square (1 meter = 3779 pixels don't know from where)

    v0 = 1.3  # (m/s) vitesse de marche par défaut et sans effet de foule
    vT = v0 * math.pow(D, -0.8)

    v = []  # speed of the individuals
    tevac = []
    L = []  # Distance de sortie normée
    Dsortie = []  # Distance de sortie
    Fspe = []
    F = []

    for i in range(len(ListParticles)):
        v.append(ListParticles[i].vit)
    # vAverage = mean(v)

    for i in range(len(ListParticles)):
        F.append(v[i] * (W / 3779) * D)  # Flux de personne (débit de pers / sec à l'ouverture)
        Fspe.append(v[i] * D)  # Flux de personne (débit spécifique en m^-1.s^-1 )
        Dsortie.append(
            ListParticles[i].Distance(coord_sortie))  # Pour obtenir la distance de sortie pour chaque particle

        L.append(Dsortie[i] / 3779)
        tevac.append(((float(N) / (float(Fspe[i]) * float(W / 3779))) + (
                L[i] / vT)))  # Temps d'évacuation

    t_total = double(
        "{:.2f}".format(max(tevac)))  # Temps total de l'évacuation correspond à la valeur la plus élevée d'évacuation

    print("Temps total théorique nécessaire pour sortir : " + str(t_total) + "secondes")
    # result.set("Nombre d'individus sorties :", str(interface.getvar(name="Nbr_part_out"))
    #            + '\n' "Temps total théorique nécessaire pour sortir : " '\n' + str(t_total) + "secondes")
    return t_total

###Ancien Modèle###
# def theory(N, w_porte, W_width, W_height, ListParticles, Dsortie):
#     ### MODELE DE TOGAWA ###
#     W = w_porte * 2  # Width of the door
#     D = (int(N) / (
#             (W_width / 3779) * (
#             W_height / 3779)))  # Density of people by meter square (1 meter = 3779 pixels don't know from where)
#
#     v0 = 1.3 / 3779  # (m/s) vitesse de marche par défaut et sans effet de foule
#     vT = v0 * math.pow(D, -0.8)
#
#     v = []  # speed of the individuals
#     for i in range(len(ListParticles)):
#         v.append(ListParticles[i].speed)
#     vAverage = mean(v)
#
#     F = vAverage * (W / 3779) * D  # Flux de personne (débit de pers / sec à l'ouverture)
#     Fspe = vAverage * D  # Flux de personne (débit spécifique en m^-1.s^-1 )
#
#     tevac = []
#     L = []
#     for i in range(len(ListParticles)):
#         L.append(Dsortie / 3779)
#         tevac.append(((float(N) / (float(Fspe) * float(W / 3779))) + (
#                 L[i] / vT)) * 10)  # Temps d'évacuation # LE FOIS 10 NE DOIT PAS ETRE LA
#
#     t_total = double(
#         "{:.2f}".format(max(tevac)))  # Temps total de l'évacuation correspond à la valeur la plus élevée d'évacuation
#
#     print("Temps total théorique nécessaire pour sortir : " + str(t_total) + "secondes")
#     # result.set("Nombre d'individus sorties :", str(interface.getvar(name="Nbr_part_out"))
#     #            + '\n' "Temps total théorique nécessaire pour sortir : " '\n' + str(t_total) + "secondes")
#     return t_total


### MODELE DE FORCE SOCIALE D'HELBING ###
# Force sociale :
# -Terme attractif : Vitesse prévue
# -Terme répulsif : Forces d'Interaction'
