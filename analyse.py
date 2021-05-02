from numpy import *
import math
import matplotlib.pyplot as plt
import xlrd


# Variables

def analyse():
    # Variables avec Obstacle
    xNbr_Obs_Ho_Al = []
    yT_Obs_Ho_Al = []

    xNbr_Obs_Ho_Ord = []
    yT_Obs_Ho_Ord = []

    xNbr_Obs_Het_Al = []
    yT_Obs_Het_Al = []

    xNbr_Obs_Het_Ord = []
    yT_Obs_Het_Ord = []

    # Variables sans Obstacle

    xNbr_Wo_Ho_Al = []
    yT_Wo_Ho_Al = []

    xNbr_Wo_Ho_Ord = []
    yT_Wo_Ho_Ord = []

    xNbr_Wo_Het_Al = []
    yT_Wo_Het_Al = []

    xNbr_Wo_Het_Ord = []
    yT_Wo_Het_Ord = []

    plt.title("Graphique des différentes modélisation (Temps en fonction Nbr)")
    plt.grid(True)
    plt.xlabel("Population (Nombre d'individus)")
    plt.ylabel("Temps d'évacuation")

    # Reading an excel file using Python
    # Give the location of the file
    loc = (r"C:\Users\sebas\PycharmProjects\crowd_simulation\crowd_data.csv")
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    # For row 0 and column 0
    print(sheet.cell_value(0, 0))

    for i in range(1, sheet.nrows):
        if sheet.cell_value(i, 6) == True:  # Avec Obstacle 'o'
            if sheet.cell_value(i, 4) == "Homogène":  # Population Homogène
                if sheet.cell_value(i, 5) == "Aléatoire":
                    xNbr_Obs_Ho_Al.append(sheet.cell_value(i, 0))
                    yT_Obs_Ho_Al.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Obs_Ho_Al, yT_Obs_Ho_Al, 'ob')

                elif sheet.cell_value(i, 5) == "Ordonnée":
                    xNbr_Obs_Ho_Ord.append(sheet.cell_value(i, 0))
                    yT_Obs_Ho_Ord.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Obs_Ho_Ord, yT_Obs_Ho_Ord, 'og')

            elif sheet.cell_value(i, 4) == "Hétérogène":  # Population Hétérogène
                if sheet.cell_value(i, 5) == "Aléatoire":
                    xNbr_Obs_Het_Al.append(sheet.cell_value(i, 0))
                    yT_Obs_Het_Al.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Obs_Het_Al, yT_Obs_Het_Al, 'oy')

                elif sheet.cell_value(i, 5) == "Ordonnée":
                    xNbr_Obs_Het_Ord.append(sheet.cell_value(i, 0))
                    yT_Obs_Het_Ord.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Obs_Het_Ord, yT_Obs_Het_Ord, 'or')

        elif sheet.cell_value(i, 6) == False:  # Sans Obstacle 'v'
            if sheet.cell_value(i, 4) == "Homogène":  # Population Homogène
                if sheet.cell_value(i, 5) == "Aléatoire":
                    xNbr_Wo_Ho_Al.append(sheet.cell_value(i, 0))
                    yT_Wo_Ho_Al.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Wo_Ho_Al, yT_Wo_Ho_Al, 'vb')

                elif sheet.cell_value(i, 5) == "Ordonnée":
                    xNbr_Wo_Ho_Ord.append(sheet.cell_value(i, 0))
                    yT_Wo_Ho_Ord.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Wo_Ho_Ord, yT_Wo_Ho_Ord, 'vg')

            elif sheet.cell_value(i, 4) == "Hétérogène":  # Population Hétérogène
                if sheet.cell_value(i, 5) == "Aléatoire":
                    xNbr_Wo_Het_Al.append(sheet.cell_value(i, 0))
                    yT_Wo_Het_Al.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Wo_Het_Al, yT_Wo_Het_Al, 'vy')

                elif sheet.cell_value(i, 5) == "Ordonnée":
                    xNbr_Wo_Het_Ord.append(sheet.cell_value(i, 0))
                    yT_Wo_Het_Ord.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Wo_Het_Ord, yT_Wo_Het_Ord, 'vr')

    plt.show()
