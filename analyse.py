from numpy import *
import math
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import xlrd
import pandas as pd


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

    ### USE PANDAS
    # # Reading an excel file using Python
    # # Give the location of the file
    # path = (r"C:\Users\sebas\PycharmProjects\crowd_simulation\crowd_data.csv")
    # # To open Workbook
    # data = pd.read_csv(path)
    # # For row 0 and column 0
    # print(str(data.values[0][0]) +"Case numéro 1")
    #
    # for i in range(1, len(data)):
    #     if str(data.values[i][6]) == "Oui" :  # Avec Obstacle 'o'
    #         if str(data.values[i][4]) == "Homogène":  # Population Homogène
    #             if str(data.values[i][5]) == "Aléatoire":
    #                 xNbr_Obs_Ho_Al.append(data.values[i][0])
    #                 yT_Obs_Ho_Al.append(data.values[i][2])
    #
    #                 print(str(data.values[i][2]) + " Trying to plot a graph")
    #                 plt.plot(xNbr_Obs_Ho_Al, yT_Obs_Ho_Al, 'ob')
    #
    #             elif data.values[i][5] == "Ordonnée":
    #                 xNbr_Obs_Ho_Ord.append(data.values[i][0])
    #                 yT_Obs_Ho_Ord.append(data.values[i][2])
    #
    #                 plt.plot(xNbr_Obs_Ho_Ord, yT_Obs_Ho_Ord, 'og')
    #
    #         elif data.values[i][4] == "Hétérogène":  # Population Hétérogène
    #             if data.values[i][5] == "Aléatoire":
    #                 xNbr_Obs_Het_Al.append(data.values[i][0])
    #                 yT_Obs_Het_Al.append(data.values[i][2])
    #
    #                 plt.plot(xNbr_Obs_Het_Al, yT_Obs_Het_Al, 'oy')
    #
    #             elif data.values[i][5] == "Ordonnée":
    #                 xNbr_Obs_Het_Ord.append(data.values[i][0])
    #                 yT_Obs_Het_Ord.append(data.values[i][2])
    #
    #                 plt.plot(xNbr_Obs_Het_Ord, yT_Obs_Het_Ord, 'or')
    #
    #     elif data.values[i][6] == "Non":  # Sans Obstacle 'v'
    #         if data.values[i][4] == "Homogène":  # Population Homogène
    #             if data.values[i][5] == "Aléatoire":
    #                 xNbr_Wo_Ho_Al.append(data.values[i][0])
    #                 yT_Wo_Ho_Al.append(data.values[i][2])
    #
    #                 plt.plot(xNbr_Wo_Ho_Al, yT_Wo_Ho_Al, 'vb')
    #
    #             elif data.values[i][5] == "Ordonnée":
    #                 xNbr_Wo_Ho_Ord.append(data.values[i][0])
    #                 yT_Wo_Ho_Ord.append(data.values[i][2])
    #
    #                 plt.plot(xNbr_Wo_Ho_Ord, yT_Wo_Ho_Ord, 'vg')
    #
    #         elif data.values[i][4] == "Hétérogène":  # Population Hétérogène
    #             if data.values[i][5] == "Aléatoire":
    #                 xNbr_Wo_Het_Al.append(data.values[i][0])
    #                 yT_Wo_Het_Al.append(data.values[i][2])
    #
    #                 plt.plot(xNbr_Wo_Het_Al, yT_Wo_Het_Al, 'vy')
    #
    #             elif data.values[i][5] == "Ordonnée":
    #                 xNbr_Wo_Het_Ord.append(data.values[i][0])
    #                 yT_Wo_Het_Ord.append(data.values[i][2])
    #
    #                 plt.plot(xNbr_Wo_Het_Ord, yT_Wo_Het_Ord, 'vr')

    ## USE XLRD
    # Reading an excel file using Python
    # Give the location of the file
    loc = (r"C:\Users\sebas\PycharmProjects\crowd_simulation\crowd_analysis.xls")
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    # For row 0 and column 0
    print(str(sheet.cell_value(0, 0)) + " Using xlrd")

    for i in range(1, sheet.nrows):
        if str(sheet.cell_value(i, 6)) == "Oui":  # Avec Obstacle 'o'
            if str(sheet.cell_value(i, 4)) == "Homogène":  # Population Homogène
                if str(sheet.cell_value(i, 5)) == "Aléatoire":
                    xNbr_Obs_Ho_Al.append(sheet.cell_value(i, 0))
                    yT_Obs_Ho_Al.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Obs_Ho_Al, yT_Obs_Ho_Al, 'ob--', label="Obstacle-Homogène-Aléatoire")
                    Obs_Ho_Al_patch = mlines.Line2D([], [], color="blue", marker='o', markersize=8,
                                                    label="Obstacle-Homogène-Aléatoire")

                    print(str(xNbr_Obs_Ho_Al) + " Using xlrd it works")

                elif sheet.cell_value(i, 5) == "Ordonnée":
                    xNbr_Obs_Ho_Ord.append(sheet.cell_value(i, 0))
                    yT_Obs_Ho_Ord.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Obs_Ho_Ord, yT_Obs_Ho_Ord, 'og--', label="Obstacle-Homogène-Ordonnée")
                    Obs_Ho_Ord_patch = mlines.Line2D([], [], color="green", marker='o', markersize=10,
                                                     label="Obstacle-Homogène-Ordonnée")

            elif sheet.cell_value(i, 4) == "Hétérogène":  # Population Hétérogène
                if sheet.cell_value(i, 5) == "Aléatoire":
                    xNbr_Obs_Het_Al.append(sheet.cell_value(i, 0))
                    yT_Obs_Het_Al.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Obs_Het_Al, yT_Obs_Het_Al, 'oy--', label="Obstacle-Hétérogène-Aléatoire")
                    Obs_Het_Al_patch = mlines.Line2D([], [], color="yellow", marker='o', markersize=10,
                                                     label="Obstacle-Hétérogène-Aléatoire")


                elif sheet.cell_value(i, 5) == "Ordonnée":
                    xNbr_Obs_Het_Ord.append(sheet.cell_value(i, 0))
                    yT_Obs_Het_Ord.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Obs_Het_Ord, yT_Obs_Het_Ord, 'or--', label="Obstacle-Hétérogène-Ordonnée")
                    Obs_Het_Ord_patch = mlines.Line2D([], [], color="red", marker='o', markersize=10,
                                                      label="Obstacle-Hétérogène-Ordonnée")


        elif sheet.cell_value(i, 6) == "Non":  # Sans Obstacle 'v'
            if sheet.cell_value(i, 4) == "Homogène":  # Population Homogène
                if sheet.cell_value(i, 5) == "Aléatoire":
                    xNbr_Wo_Ho_Al.append(sheet.cell_value(i, 0))
                    yT_Wo_Ho_Al.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Wo_Ho_Al, yT_Wo_Ho_Al, 'vb--', label="SansObstacle-Homogène-Aléatoire")
                    Sobs_Ho_Al_patch = mlines.Line2D([], [], color="blue", marker='v', markersize=10,
                                                     label="SansObstacle-Homogène-Aléatoire")


                elif sheet.cell_value(i, 5) == "Ordonnée":
                    xNbr_Wo_Ho_Ord.append(sheet.cell_value(i, 0))
                    yT_Wo_Ho_Ord.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Wo_Ho_Ord, yT_Wo_Ho_Ord, 'vg--', label="SansObstacle-Homogène-Ordonnée")
                    Sobs_Ho_Ord_patch = mlines.Line2D([], [], color="green", marker='v', markersize=10,
                                                      label="SansObstacle-Homogène-Ordonnée")


            elif sheet.cell_value(i, 4) == "Hétérogène":  # Population Hétérogène
                if sheet.cell_value(i, 5) == "Aléatoire":
                    xNbr_Wo_Het_Al.append(sheet.cell_value(i, 0))
                    yT_Wo_Het_Al.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Wo_Het_Al, yT_Wo_Het_Al, 'vy--', label="SansObstacle-Hétérogène-Aléatoire")
                    Sobs_Het_Al_patch = mlines.Line2D([], [], color="yellow", marker='v', markersize=10,
                                                      label="SansObstacle-Hétérogène-Aléatoire")


                elif sheet.cell_value(i, 5) == "Ordonnée":
                    xNbr_Wo_Het_Ord.append(sheet.cell_value(i, 0))
                    yT_Wo_Het_Ord.append(sheet.cell_value(i, 2))

                    plt.plot(xNbr_Wo_Het_Ord, yT_Wo_Het_Ord, 'vr--', label="SansObstacle-Hétérogène-Ordonnée")
                    Sobs_Het_Ord_patch = mlines.Line2D([], [], color="red", marker='v', markersize=10,
                                                       label="SansObstacle-Hétérogène-Ordonnée")

    # plt.legend(loc="upper right")
    plt.legend(handles=[Obs_Ho_Al_patch, Obs_Ho_Ord_patch, Obs_Het_Al_patch, Obs_Het_Ord_patch], loc="upper right")
    # For next time just to put above : ,Sobs_Ho_Al_patch,Sobs_Ho_Ord_patch,Sobs_Het_Al_patch,Sobs_Het_Ord_patch
    plt.show()
