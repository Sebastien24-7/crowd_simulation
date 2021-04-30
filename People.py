import math
import sys
import random
import matplotlib
import numpy
from PIL import Image
from PIL import ImageDraw


###############################

class People():
    """
    Defines the particle to represent and interact with (ex: an animal / a human being)
    ------
    Attributes :
    name: string
        name of the people/particle
    color: string
        particles are represented as yellow
    xcoord: float
    ycoord: float
    radius: int

    """

    def __init__(self, xcenter, ycenter, vx, vy, type):
        """
        Constructor of a Particle object
        """

        colors = ["red", "orange", "yellow", "green", "blue", "violet"]
        # self.color = random.choice(colors)
        self.color = "#{:06x}".format(random.randint(0, 0xffffff))
        self.xcenter, self.ycenter = [xcenter, ycenter]  # Used for computing distance between particles
        # self.xcoord, self.ycoord = [xcenter - 8, ycenter - 8]  # They are the coordinates of the center of the particle

        #### To create a random crowd with every kind of people
        if type == "kid":
            self.xcoord, self.ycoord = [xcenter - 7,
                                        ycenter - 7]  # They are the coordinates of the center of the particle
            self.masse = 0.5
            self.speed = 2
            self.name = "Enfant"
            self.color = "green"
        if type == "adult":
            self.xcoord, self.ycoord = [xcenter - 8,
                                        ycenter - 8]  # They are the coordinates of the center of the particle
            self.masse = 1
            self.speed = 1
            self.name = "Adulte"
            self.color = "purple"
        if type == "old":
            self.xcoord, self.ycoord = [xcenter - 10,
                                        ycenter - 10]  # They are the coordinates of the center of the particle
            self.masse = 1.5
            self.speed = 0.7
            self.name = "Ancien"
            self.color = "yellow"
        ####

        self.radius = math.sqrt(math.pow(self.xcenter - self.xcoord, 2) + math.pow(self.ycenter - self.ycoord, 2))

        self.touched = 0
        self.masse = 1
        self.angle = 0
        self.vx, self.vy = (self.speed * vx, self.speed * vy)
        self.vit = math.sqrt(vx ** 2 + vy ** 2)
        # self.theta = self.vx / self.vit
        self.good_pos = False
        self.time = 0

    def __str__(self):
        """
        Print this Particle object
        """
        return "--> Je suis un objet People " \
               + "\n    name: " + str(self.name) \
               + "\n    color: " + str(self.color) \
               + "\n    mon centre xcenter: " + str(self.xcenter) \
               + "\n    mon centre ycenter: " + str(self.ycenter) \
               + "\n    xcoord: " + str(self.xcoord) \
               + "\n    ycoord: " + str(self.ycoord) \
               + "\n    touched: " + str(self.touched) \
               + "\n    mon rayon : " + str(self.radius) \
               + "\n    je suis sortie en :" + str(self.time) \
 \
            ############

    # Creation of the list of people
    def CreaPart(number, W_width, W_height, crowd_type):
        my_particles = []
        possible_types = ["kid", "adult", "old"]
        for i in range(number):
            xcenter = (W_width - 200) * random.random() + 100
            ycenter = (W_height - 200) * random.random() + 100

            # D = [xcenter - coord_sortie[0], ycenter - coord_sortie[1]]
            # D_norm=D/math.sqrt((xcoord - coord_sortie[0]) ** 2 + (ycoord - coord_sortie[1]) ** 2)
            # print(D)

            # vx = 1 * (coord_sortie[0] - xcenter) / math.sqrt(
            #     (xcenter - coord_sortie[0]) ** 2 + (ycenter - coord_sortie[1]) ** 2)
            # vy = 1 * (coord_sortie[1] - ycenter) / math.sqrt(
            #     (xcenter - coord_sortie[0]) ** 2 + (ycenter - coord_sortie[1]) ** 2)

            vx = random.random() * 2 - 1
            vy = random.random() * 2 - 1
            # vx, vy = [0, 0]

            ### To Produce a Population with various Type
            if crowd_type == "Hétérogène":
                ## To produce a Gaussian repartition of the population
                k = random.random()
                if k < 0.6:
                    type = possible_types[1]
                if 0.6 < k < 0.8:
                    type = possible_types[0]
                if 0.8 < k < 1.0:
                    type = possible_types[2]
            else:
                ### Produce a Population with only adults
                type = possible_types[1]

            p = People(xcenter, ycenter, vx, vy, type)

            my_particles.append(p)
        return my_particles

    ##Deal with the overlapping at the creation of the particles
    def CreaCrowd(p, type, W_width, W_height):
        ### RANDOM CROWD ####
        for i in range(len(p)):
            for j in range(len(p)):
                while True:
                    p[i].xcenter = (W_width - 100) * random.random() + 50
                    p[j].xcenter = (W_width - 100) * random.random() + 50
                    p[i].ycenter = (W_height - 100) * random.random() + 50
                    p[j].ycenter = (W_height - 100) * random.random() + 50
                    if (abs(p[i].xcenter - p[j].xcenter) < 40) | (abs(p[i].ycenter - p[i].ycenter) < 40):
                        break

        # if (str)(interface.getvar(name="crowd_type")) == "Aléatoire":
        #     for i in range(len(my_particles)):
        #         # Check it is inside the room (but not functional)
        #         if my_particles[i].xcenter < (25 - my_particles[i].radius) or my_particles[i].xcenter > (
        #                 width - 25 + my_particles[i].radius):
        #             my_particles[i].xcenter = (width - 80) * random.random() + 30
        #             # print(" I was going outside")
        #         if my_particles[i].ycenter < (25 - my_particles[i].radius) or my_particles[i].ycenter > (
        #                 height - 25 + my_particles[i].radius):
        #             my_particles[i].ycenter = (height - 80) * random.random() + 30
        #             # print(" I was going outside")

        # if i!=0 and  my_particles[i].distance_collision(my_particles[i-1]) < (my_particles[i].radius + my_particles[i-1].radius):
        #     my_particles[i].xcenter = (world.width - 50) * random.random() + 30
        #     my_particles[i].ycenter = (world.height - 50) * random.random() + 30
        #     print(" I was going over a friend")

        # # Checking the overlapping between particles
        # for j in range(len(p)):
        #     # if my_particles[i].distance_collision(my_particles[j]) < (
        #     #         my_particles[i].radius + my_particles[j].radius):
        #     #     my_particles[i].xcenter = (world.width - 50) * random.random() + 30
        #     #     my_particles[i].ycenter = (world.height - 50) * random.random() + 30
        #     #     print(" I was going over a friend")
        #     #
        #     #     if my_particles[i].distance_collision(my_particles[j]) < (
        #     #             my_particles[i].radius + my_particles[j].radius):
        #     #          print(" I 'm still going over a friend")
        #     # print("I do my work")
        #     while my_particles[j].xcenter - my_particles[j].radius <= my_particles[i].xcenter <= my_particles[
        #         j].xcenter:
        #         my_particles[i].xcenter -= my_particles[j].radius - 25
        #         my_particles[i].ycenter -= my_particles[j].radius - 25
        #     while my_particles[j].xcenter + my_particles[j].radius >= my_particles[i].xcenter >= my_particles[
        #         j].xcenter:
        #         my_particles[i].xcenter += my_particles[j].radius + 25
        #         my_particles[i].ycenter += my_particles[j].radius + 25

        ## ORDERED CROWD ####
        if type == "Ordonnée":

            # Initialisation des particules sur forme de grille
            i = 0
            j = 4
            for k in range(len(p)):
                # my_particles[k].vx , my_particles[k].vy = 0 , 0
                # my_particles[k].xcenter , my_particles[k].ycenter = 40 , 40
                if 40 * i <= 420:
                    i = i + 1
                    p[k].xcenter = 40 * i
                    p[k].ycenter = 40 * j
                else:
                    i = 1
                    j = j + 1
                    p[k].xcenter = 40
                    p[k].ycenter = 40 * j

        return p

    def distance_collision(self, particle):
        """
        Determines the distance between of all the particles
        """
        # the ** is the operator for square
        distance = math.sqrt(((particle.xcenter + particle.radius) - (self.xcenter + self.radius)) ** 2 +
                             ((particle.ycenter + particle.radius) - (self.ycenter + self.radius)) ** 2)
        return distance

    def people_target_distance(self):
        """
        Determines the distance for all the particles between them and their targets
        """
        coord_sortie = [0, -20]
        D = [self.xcenter - coord_sortie[0], self.ycenter - coord_sortie[1]]
        D_norm = D / numpy.linalg.norm(D)

        return D_norm

    def ComputeTraj(self, coord_sortie):
        self.vx = (coord_sortie[0] - self.xcenter) / math.sqrt(
            (self.xcenter - coord_sortie[0]) ** 2 + (self.ycenter - coord_sortie[1]) ** 2)
        self.vy = (coord_sortie[1] - self.ycenter) / math.sqrt(
            (self.xcenter - coord_sortie[0]) ** 2 + (self.ycenter - coord_sortie[1]) ** 2)

    def Distance(self, coord):
        delta_x = coord[0] - self.xcenter
        delta_y = coord[1] - self.ycenter
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

    def CollisionObstacle(self, coord):

        delta = math.sqrt(((coord[0]) - (self.xcenter + self.radius)) ** 2 +
                          ((coord[1]) - (self.ycenter + self.radius)) ** 2)
        return delta

    def CollisionObstacle2(self, ListObstacles, bool):

        for i in range(len(ListObstacles)):

            delta = math.sqrt(
                ((ListObstacles[i].xcenter + ListObstacles[i].radius) - (self.xcenter + self.radius)) ** 2 +
                ((ListObstacles[i].ycenter + ListObstacles[i].radius) - (self.ycenter + self.radius)) ** 2)

            if delta < self.radius + ListObstacles[i].radius:
                # To detect collision is working
                if not bool:  # Si chilling les particules rebondissent sur les obstacles
                    self.color = "brown"
                    [self.vx, self.vy] = [-self.vx, -self.vy]
                else:
                    # if (ListObstacles[i].xcenter - ListObstacles[i].radius < (self.xcenter) <ListObstacles[i].xcenter + ListObstacles[i].radius ):
                    #     if (self.vy < 0 and (self.ycenter-self.radius) > ListObstacles[i].ycenter + ListObstacles[i].radius) or (self.vy > 0 and (self.ycenter+self.radius) < ListObstacles[i].ycenter - ListObstacles[i].radius):
                    #         if self.Distance([ListObstacles[i].ycenter - ListObstacles[i].radius, ListObstacles[i].xcenter - ListObstacles[i].radius]) >\
                    #                 self.Distance([ListObstacles[i].ycenter - ListObstacles[i].radius,ListObstacles[i].xcenter + ListObstacles[i].radius]):
                    #             [self.vx, self.vy] = [-(self.vy + self.vx), 0]
                    #         else :
                    #             [self.vx, self.vy] = [+(self.vy + self.vx), 0]
                    #
                    # if (ListObstacles[i].ycenter - ListObstacles[i].radius < (self.ycenter) < ListObstacles[i].ycenter + ListObstacles[i].radius):
                    #     if (self.vx < 0 and (self.xcenter-self.radius) > ListObstacles[i].xcenter + ListObstacles[i].radius) or (self.vx > 0 and (self.xcenter+self.radius) < ListObstacles[i].xcenter - ListObstacles[i].radius):
                    #         if self.Distance([ListObstacles[i].xcenter + ListObstacles[i].radius, ListObstacles[i].ycenter - ListObstacles[i].radius]) \
                    #                 > self.Distance([ListObstacles[i].xcenter + ListObstacles[i].radius,ListObstacles[i].ycenter + ListObstacles[i].radius]):
                    #             [self.vx, self.vy] = [0, +(self.vy + self.vx)]
                    #         else:
                    #             [self.vx, self.vy] = [0, -(self.vy + self.vx)]
                    #
                    #     # Interaction with all the sides of the obstacles

                    if (ListObstacles[i].ycenter - ListObstacles[i].radius - self.radius) < (self.ycenter) < (
                            ListObstacles[i].ycenter + ListObstacles[i].radius + self.radius):
                        # Right of the Obstacle
                        if self.vx < 0 and (self.xcenter) > (
                                ListObstacles[i].xcenter + ListObstacles[i].radius + self.radius):  # va vers la gauche
                            # (côté haut est plus loin que celui du bas)
                            if self.Distance([ListObstacles[i].xcenter + ListObstacles[i].radius,
                                              ListObstacles[i].ycenter - ListObstacles[i].radius]) > self.Distance(
                                [ListObstacles[i].xcenter + ListObstacles[i].radius,
                                 ListObstacles[i].ycenter + ListObstacles[i].radius]):
                                [self.vx, self.vy] = [0, (self.vy + self.vx)]
                                self.color = "yellow"
                            else:
                                [self.vx, self.vy] = [0, -(self.vy + self.vx)]
                                self.color = "yellow"

                        # Left of the Obstacle
                        if self.vx > 0 and (self.xcenter) < (
                                ListObstacles[i].xcenter - ListObstacles[i].radius - self.radius):  # va vers la droite
                            # (côté haut est plus loin que celui du bas)
                            if self.Distance([ListObstacles[i].xcenter - ListObstacles[i].radius,
                                              ListObstacles[i].ycenter - ListObstacles[i].radius]) > self.Distance(
                                [ListObstacles[i].xcenter - ListObstacles[i].radius,
                                 ListObstacles[i].ycenter + ListObstacles[i].radius]):
                                [self.vx, self.vy] = [0, (self.vy + self.vx)]
                                self.color = "yellow"
                            else:
                                [self.vx, self.vy] = [0, -(self.vy + self.vx)]
                                self.color = "yellow"

                    # if (ListObstacles[i].xcenter - ListObstacles[i].radius - self.radius) < (self.xcenter) < (
                    #         ListObstacles[i].xcenter + ListObstacles[i].radius + self.radius):
                    #     ##Top of the obstacle
                    #     if self.vy > 0 and (self.ycenter) < (
                    #             ListObstacles[i].ycenter - ListObstacles[i].radius - self.radius):  # Redescend
                    #         # (côté gauche est plus loin que celui de droite)
                    #         if self.Distance([ListObstacles[i].ycenter - ListObstacles[i].radius,
                    #                           ListObstacles[i].xcenter - ListObstacles[i].radius]) > self.Distance(
                    #             [ListObstacles[i].ycenter - ListObstacles[i].radius,
                    #              ListObstacles[i].xcenter + ListObstacles[i].radius]):
                    #             [self.vx, self.vy] = [-(self.vx + self.vy), 0]
                    #             self.color = "blue"
                    #         else:
                    #             [self.vx, self.vy] = [+(self.vx + self.vy), 0]
                    #             self.color = "blue"
                    #
                    #     ##Bottom of the obstacle
                    #     if self.vy < 0 and (self.ycenter) > (
                    #             ListObstacles[i].ycenter + ListObstacles[i].radius + self.radius):  # Remonte
                    #         # (côté gauche est plus loin que celui de droite)
                    #         if self.Distance([ListObstacles[i].ycenter + ListObstacles[i].radius,
                    #                           ListObstacles[i].xcenter - ListObstacles[i].radius]) > self.Distance(
                    #             [ListObstacles[i].ycenter + ListObstacles[i].radius,
                    #              ListObstacles[i].xcenter + ListObstacles[i].radius]):
                    #             [self.vx, self.vy] = [-(self.vx + self.vy), 0]
                    #             self.color = "blue"
                    #         else:
                    #             [self.vx, self.vy] = [+(self.vx + self.vy), 0]
                    #             self.color = "blue"

    def col(self, p):

        N = [self.xcenter - p.xcenter, self.ycenter - p.ycenter]
        alpha = math.tan(N[0] / N[1])

        v1 = self.vit
        th1 = self.theta
        v2 = p.vit
        th2 = p.theta

        theta11 = math.atan((v2 / v1) * (math.sin(th2) / math.cos(th1)))
        v11 = math.sqrt((v2 * math.sin(th2)) ** 2 + (v1 * math.cos(th1)) ** 2)

        theta22 = math.atan((v1 / v2) * (math.sin(th1) / math.cos(th2)))
        v22 = math.sqrt((v1 * math.sin(th1)) ** 2 + (v2 * math.cos(th2)) ** 2)
        # il faut projeter sur le repere xy de l'affichage et modif vx et vy

        self.vx = v11 * ((math.cos(theta11)*math.cos(alpha) - math.sin(theta11)*math.sin(alpha)) + (-math.sin(theta11)*math.cos(alpha)+math.cos(theta11)*math.sin(alpha)))
        self.vy = v11 * ((-math.sin(theta11)*math.sin(alpha) + math.cos(alpha)*math.cos(theta11)) + (math.cos(theta11)*math.sin(alpha)+math.cos(alpha)*math.sin(theta11)))

        p.vx = v22 * ((math.cos(theta22)*math.cos(alpha) - math.sin(theta22)*math.sin(alpha)) + (-math.sin(theta22)*math.cos(alpha)+math.cos(theta22)*math.sin(alpha)))
        p.vy = v22 * ((-math.sin(theta22)*math.sin(alpha) + math.cos(alpha)*math.cos(theta22)) + (math.cos(theta22)*math.sin(alpha)+math.cos(alpha)*math.sin(theta22)))


