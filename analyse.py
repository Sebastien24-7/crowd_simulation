# from numpy import *
import math
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import xlrd
import pandas as pd


# Variables

def analyse():
    xObs_Pos = []
    yObs_Pos = []
    Theo_yObs_Pos = []
    xObs_Pos2 = []
    yObs_Pos2 = []
    Theo_yObs_Pos2 = []
    xObs_Pos3 = []
    yObs_Pos3 = []
    Theo_yObs_Pos3 = []
    xObs_Pos4 = []
    yObs_Pos4 = []
    Theo_yObs_Pos4 = []

    # # Variables avec Obstacle
    # xNbr_Obs_Ho_Al = []
    # yT_Obs_Ho_Al = []
    # Theo_yT_Obs_Ho_Al = []
    #
    # xNbr_Obs_Ho_Ord = []
    # yT_Obs_Ho_Ord = []
    # Theo_yT_Obs_Ho_Ord = []
    #
    # xNbr_Obs_Het_Al = []
    # yT_Obs_Het_Al = []
    # Theo_yT_Obs_Het_Al = []
    #
    # xNbr_Obs_Het_Ord = []
    # yT_Obs_Het_Ord = []
    # Theo_yT_Obs_Het_Ord = []
    #
    # ### Variables sans Obstacle ###
    #
    # xNbr_Wo_Ho_Al = []
    # yT_Wo_Ho_Al = []
    # Theo_yT_Wo_Ho_Al = []
    #
    # xNbr_Wo_Ho_Ord = []
    # yT_Wo_Ho_Ord = []
    # Theo_yT_Wo_Ho_Ord = []
    #
    # xNbr_Wo_Het_Al = []
    # yT_Wo_Het_Al = []
    # Theo_yT_Wo_Het_Al = []
    #
    # xNbr_Wo_Het_Ord = []
    # yT_Wo_Het_Ord = []
    # Theo_yT_Wo_Het_Ord = []

    plt.title(
        "Graphique des différentes modélisation (Temps en fonction Nbr)" '\n' "Avec Obstacle - Egoïste - N20 à 70" '\n' "Variation taille de la porte et population")
    plt.grid(True)
    plt.xlabel("Taille de la porte")
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
    sheet = wb.sheet_by_index(3)

    # For row 0 and column 0
    print(str(sheet.cell_value(0, 0)) + " Using xlrd")

    for i in range(1, sheet.nrows):

        if str(sheet.cell_value(i, 10)) == "Taille Porte":  # Variations Positions
            if str(sheet.cell_value(i, 5)) == "Aléatoire":
                if sheet.cell_value(i, 8) == 1:
                    xObs_Pos.append(sheet.cell_value(i, 9))
                    yObs_Pos.append(sheet.cell_value(i, 2))
                    Theo_yObs_Pos.append(sheet.cell_value(i, 3))

                    plt.plot(xObs_Pos, yObs_Pos, 'or-', label="Temps Simulation N=50")
                    Obs_Pos_patch = mlines.Line2D([], [], color="red", marker='o', markersize=8,
                                                  label="Temps Simulation N=50")
                    plt.plot(xObs_Pos, Theo_yObs_Pos, 'xr--', label="Temps Théorique N=50")
                    Theo_Obs_Pos_patch = mlines.Line2D([], [], color="red", marker='x', markersize=8,
                                                       label="Temps Théorique N=50")
                if sheet.cell_value(i, 8) == 2:
                    xObs_Pos2.append(sheet.cell_value(i, 9))
                    yObs_Pos2.append(sheet.cell_value(i, 2))
                    Theo_yObs_Pos2.append(sheet.cell_value(i, 3))

                    plt.plot(xObs_Pos2, yObs_Pos2, 'ob-', label="Temps Simulation N=20")
                    Obs_Pos2_patch = mlines.Line2D([], [], color="blue", marker='o', markersize=8,
                                                   label="Temps Simulation N=20")
                    plt.plot(xObs_Pos2, Theo_yObs_Pos2, 'xb--', label="Temps Théorique N=20")
                    Theo_Obs_Pos2_patch = mlines.Line2D([], [], color="blue", marker='x', markersize=8,
                                                        label="Temps Théorique N=20")
                if sheet.cell_value(i, 8) == 3:
                    xObs_Pos3.append(sheet.cell_value(i, 9))
                    yObs_Pos3.append(sheet.cell_value(i, 2))
                    Theo_yObs_Pos3.append(sheet.cell_value(i, 3))

                    plt.plot(xObs_Pos3, yObs_Pos3, 'oy-', label="Temps Simulation N=40")
                    Obs_Pos3_patch = mlines.Line2D([], [], color="yellow", marker='o', markersize=8,
                                                   label="Temps Simulation N=40")
                    plt.plot(xObs_Pos3, Theo_yObs_Pos3, 'xy--', label="Temps Théorique N=40")
                    Theo_Obs_Pos3_patch = mlines.Line2D([], [], color="yellow", marker='x', markersize=8,
                                                        label="Temps Théorique N=40")
                if sheet.cell_value(i, 8) == 4:
                    xObs_Pos4.append(sheet.cell_value(i, 9))
                    yObs_Pos4.append(sheet.cell_value(i, 2))
                    Theo_yObs_Pos4.append(sheet.cell_value(i, 3))

                    plt.plot(xObs_Pos4, yObs_Pos4, 'og-', label="Temps Simulation N=70")
                    Obs_Pos4_patch = mlines.Line2D([], [], color="green", marker='o', markersize=8,
                                                   label="Temps Simulation N=70")
                    plt.plot(xObs_Pos4, Theo_yObs_Pos4, 'xg--', label="Temps Théorique N=70")
                    Theo_Obs_Pos4_patch = mlines.Line2D([], [], color="green", marker='x', markersize=8,
                                                        label="Temps Théorique N=70")

        # if str(sheet.cell_value(i, 4)) == "Homogène":  # Population Homogène
        #     if str(sheet.cell_value(i, 5)) == "Aléatoire":
        #         xNbr_Obs_Ho_Al.append(sheet.cell_value(i, 9))
        #         yT_Obs_Ho_Al.append(sheet.cell_value(i, 2))
        #         Theo_yT_Obs_Ho_Al.append(sheet.cell_value(i, 3))
        #
        #         plt.plot(xNbr_Obs_Ho_Al, yT_Obs_Ho_Al, 'ob--', label="Obstacle-Homogène-Aléatoire")
        #         Obs_Ho_Al_patch = mlines.Line2D([], [], color="blue", marker='o', markersize=8,
        #                                         label="Obstacle-Homogène-Aléatoire")
        #         plt.plot(xNbr_Obs_Ho_Al, Theo_yT_Obs_Ho_Al, 'xb-', label="Théorique-Obs-Homogène-Aléatoire")
        #         Theo_Obs_Ho_Al_patch = mlines.Line2D([], [], color="blue", marker='x', markersize=5,
        #                                         label="Théorique-Obs-Homogène-Aléatoire")
        #
        #
        #         print(str(xNbr_Obs_Ho_Al) + " Using xlrd it works")
        #
        #     elif sheet.cell_value(i, 5) == "Ordonnée":
        #         xNbr_Obs_Ho_Ord.append(sheet.cell_value(i, 9))
        #         yT_Obs_Ho_Ord.append(sheet.cell_value(i, 2))
        #         Theo_yT_Obs_Ho_Ord.append(sheet.cell_value(i, 3))
        #
        #         plt.plot(xNbr_Obs_Ho_Ord, yT_Obs_Ho_Ord, 'og--', label="Obstacle-Homogène-Ordonnée")
        #         Obs_Ho_Ord_patch = mlines.Line2D([], [], color="green", marker='o', markersize=8,
        #                                          label="Obstacle-Homogène-Ordonnée")
        #         plt.plot(xNbr_Obs_Ho_Ord, Theo_yT_Obs_Ho_Ord, 'xg-', label="Théorique-Obs-Homogène-Ordonnée")
        #         Theo_Obs_Ho_Ord_patch = mlines.Line2D([], [], color="green", marker='x', markersize=5,
        #                                         label="Théorique-Obs-Homogène-Ordonnée")
        #
        # elif sheet.cell_value(i, 4) == "Hétérogène":  # Population Hétérogène
        #     if sheet.cell_value(i, 5) == "Aléatoire":
        #         xNbr_Obs_Het_Al.append(sheet.cell_value(i, 9))
        #         yT_Obs_Het_Al.append(sheet.cell_value(i, 2))
        #         Theo_yT_Obs_Het_Al.append(sheet.cell_value(i, 3))
        #
        #         plt.plot(xNbr_Obs_Het_Al, yT_Obs_Het_Al, 'oy--', label="Obstacle-Hétérogène-Aléatoire")
        #         Obs_Het_Al_patch = mlines.Line2D([], [], color="yellow", marker='o', markersize=8,
        #                                          label="Obstacle-Hétérogène-Aléatoire")
        #
        #         plt.plot(xNbr_Obs_Het_Al, Theo_yT_Obs_Het_Al, 'xy-', label="Théorique-Obs-Hétérogène-Aléatoire")
        #         Theo_Obs_Het_Al_patch = mlines.Line2D([], [], color="yellow", marker='x', markersize=5,
        #                                         label="Théorique-Obs-Hétérogène-Aléatoire")
        #
        #
        #     elif sheet.cell_value(i, 5) == "Ordonnée":
        #         xNbr_Obs_Het_Ord.append(sheet.cell_value(i, 9))
        #         yT_Obs_Het_Ord.append(sheet.cell_value(i, 2))
        #         Theo_yT_Obs_Het_Ord.append(sheet.cell_value(i, 3))
        #
        #         plt.plot(xNbr_Obs_Het_Ord, yT_Obs_Het_Ord, 'or--', label="Obstacle-Hétérogène-Ordonnée")
        #         Obs_Het_Ord_patch = mlines.Line2D([], [], color="red", marker='o', markersize=8,
        #                                           label="Obstacle-Hétérogène-Ordonnée")
        #
        #         plt.plot(xNbr_Obs_Het_Ord, Theo_yT_Obs_Het_Ord, 'xr-', label="Théorique-Obs-Hétérogène-Ordonnée")
        #         Theo_Obs_Het_Ord_patch = mlines.Line2D([], [], color="red", marker='x', markersize=5,
        #                                         label="Théorique-Obs-Hétérogène-Ordonnée")

        # if sheet.cell_value(i, 9) == "Laisse passer":  # Sans Obstacle 'v'
        #     if sheet.cell_value(i, 4) == "Homogène":  # Population Homogène
        #         if sheet.cell_value(i, 5) == "Aléatoire":
        #             xNbr_Wo_Ho_Al.append(sheet.cell_value(i, 0))
        #             yT_Wo_Ho_Al.append(sheet.cell_value(i, 2))
        #             Theo_yT_Wo_Ho_Al.append(sheet.cell_value(i, 3))
        #
        #             plt.plot(xNbr_Wo_Ho_Al, yT_Wo_Ho_Al, 'vb--', label="SansObstacle-Homogène-Aléatoire")
        #             Sobs_Ho_Al_patch = mlines.Line2D([], [], color="blue", marker='v', markersize=10,
        #                                              label="SansObstacle-Homogène-Aléatoire")
        #
        #             plt.plot(xNbr_Wo_Ho_Al, Theo_yT_Wo_Ho_Al, 'xb-', label="Théorique-SansObs-Homogène-Aléatoire")
        #             Theo_yT_Wo_Ho_Al_patch = mlines.Line2D([], [], color="blue", marker='x', markersize=5,
        #                                              label="Théorique-SansObs-Homogène-Aléatoire")
        #
        #
        #         elif sheet.cell_value(i, 5) == "Ordonnée":
        #             xNbr_Wo_Ho_Ord.append(sheet.cell_value(i, 0))
        #             yT_Wo_Ho_Ord.append(sheet.cell_value(i, 2))
        #             Theo_yT_Wo_Ho_Ord.append(sheet.cell_value(i, 3))
        #
        #             plt.plot(xNbr_Wo_Ho_Ord, yT_Wo_Ho_Ord, 'vg--', label="SansObstacle-Homogène-Ordonnée")
        #             Sobs_Ho_Ord_patch = mlines.Line2D([], [], color="green", marker='v', markersize=10,
        #                                               label="SansObstacle-Homogène-Ordonnée")
        #
        #             plt.plot(xNbr_Wo_Ho_Ord, Theo_yT_Wo_Ho_Ord, 'xg-', label="Théorique-SansObs-Homogène-Ordonnée")
        #             Theo_yT_Wo_Ho_Ord_patch = mlines.Line2D([], [], color="green", marker='x', markersize=5,
        #                                              label="Théorique-SansObs-Homogène-Ordonnée")
        #
        #
        #     elif sheet.cell_value(i, 4) == "Hétérogène":  # Population Hétérogène
        #         if sheet.cell_value(i, 5) == "Aléatoire":
        #             xNbr_Wo_Het_Al.append(sheet.cell_value(i, 0))
        #             yT_Wo_Het_Al.append(sheet.cell_value(i, 2))
        #             Theo_yT_Wo_Het_Al.append(sheet.cell_value(i, 3))
        #
        #
        #             plt.plot(xNbr_Wo_Het_Al, yT_Wo_Het_Al, 'vy--', label="SansObstacle-Hétérogène-Aléatoire")
        #             Sobs_Het_Al_patch = mlines.Line2D([], [], color="yellow", marker='v', markersize=10,
        #                                               label="SansObstacle-Hétérogène-Aléatoire")
        #
        #             plt.plot(xNbr_Wo_Het_Al, Theo_yT_Wo_Het_Al, 'xy-', label="Théorique-SansObs-Hétérogène-Aléatoire")
        #             Theo_yT_Wo_Het_Al_patch = mlines.Line2D([], [], color="yellow", marker='x', markersize=5,
        #                                              label="Théorique-SansObs-Hétérogène-Aléatoire")
        #
        #
        #         elif sheet.cell_value(i, 5) == "Ordonnée":
        #             xNbr_Wo_Het_Ord.append(sheet.cell_value(i, 0))
        #             yT_Wo_Het_Ord.append(sheet.cell_value(i, 2))
        #             Theo_yT_Wo_Het_Ord.append(sheet.cell_value(i, 3))
        #
        #             plt.plot(xNbr_Wo_Het_Ord, yT_Wo_Het_Ord, 'vr--', label="SansObstacle-Hétérogène-Ordonnée")
        #             Sobs_Het_Ord_patch = mlines.Line2D([], [], color="red", marker='v', markersize=10,
        #                                                label="SansObstacle-Hétérogène-Ordonnée")
        #
        #             plt.plot(xNbr_Wo_Het_Ord, Theo_yT_Wo_Het_Ord, 'xr-', label="Théorique-SansObs-Hétérogène-Ordonnée")
        #             Theo_yT_Wo_Het_Ord_patch = mlines.Line2D([], [], color="red", marker='x', markersize=5,
        #                                              label="Théorique-SansObs-Hétérogène-Ordonnée")

    # plt.legend(loc="upper right")
    plt.legend(handles=[Obs_Pos_patch, Theo_Obs_Pos_patch, Obs_Pos2_patch, Theo_Obs_Pos2_patch, Obs_Pos3_patch,
                        Theo_Obs_Pos3_patch, Obs_Pos4_patch, Theo_Obs_Pos4_patch], loc="best")

    # plt.errorbar(x, y, xerr=0.1 * x, yerr=5.0 + 0.75 * y)
    # For next time just to put above :
    #                         ,Sobs_Ho_Al_patch,Sobs_Ho_Ord_patch,Sobs_Het_Al_patch,Sobs_Het_Ord_patch,
    #                         Theo_yT_Wo_Ho_Al_patch,Theo_yT_Wo_Ho_Ord_patch,Theo_yT_Wo_Het_Al_patch,Theo_yT_Wo_Het_Ord_patch
    #
    #   Obs_Ho_Al_patch, Obs_Ho_Ord_patch, Obs_Het_Al_patch, Obs_Het_Ord_patch,
    #   Theo_Obs_Ho_Al_patch, Theo_Obs_Ho_Ord_patch, Theo_Obs_Het_Al_patch, Theo_Obs_Het_Ord_patch

    plt.autoscale(enable=True, axis='both', tight=None)
    ###
    plt.show()
