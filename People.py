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
        self.xcoord, self.ycoord = [xcenter - 8, ycenter - 8]  # They are the coordinates of the center of the particle

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
            self.xcoord, self.ycoord = [xcenter - 9,
                                        ycenter - 9]  # They are the coordinates of the center of the particle
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
        self.theta = self.vx / self.vit
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

    def CollisionObstacle2(self, ListObstacles):

        for i in range(len(ListObstacles)):

            delta = math.sqrt(
                ((ListObstacles[i].xcenter + ListObstacles[i].radius) - (self.xcenter + self.radius)) ** 2 +
                ((ListObstacles[i].ycenter + ListObstacles[i].radius) - (self.ycenter + self.radius)) ** 2)

            if delta < self.radius + ListObstacles[i].radius:
                # To detect collision is working
                self.color = "brown"

                # Interaction with all the sides of the obstacles

                # Right of the Obstacle
                if self.Distance([ListObstacles[i].xcenter + ListObstacles[i].radius,
                                  ListObstacles[i].ycenter - ListObstacles[i].radius]) > self.Distance(
                    [ListObstacles[i].xcenter + ListObstacles[i].radius,
                     ListObstacles[i].ycenter + ListObstacles[i].radius]):
                    [self.vx, self.vy] = [0, +(self.vy + self.vx)]
                    self.color = "black"
                else:
                    [self.vx, self.vy] = [0, -(self.vy + self.vx)]
                    self.color = "black"

                # Left of the Obstacle
                if self.Distance([ListObstacles[i].xcenter - ListObstacles[i].radius,
                                  ListObstacles[i].ycenter - ListObstacles[i].radius]) > self.Distance(
                    [ListObstacles[i].xcenter - ListObstacles[i].radius,
                     ListObstacles[i].ycenter + ListObstacles[i].radius]):
                    [self.vx, self.vy] = [0, +(self.vy + self.vx)]
                    self.color = "black"
                else:
                    [self.vx, self.vy] = [0, -(self.vy + self.vx)]
                    self.color = "black"

                ##Top of the obstacle
                if self.Distance([ListObstacles[i].ycenter - ListObstacles[i].radius,
                                  ListObstacles[i].xcenter - ListObstacles[i].radius]) > self.Distance(
                    [ListObstacles[i].ycenter - ListObstacles[i].radius,
                     ListObstacles[i].xcenter + ListObstacles[i].radius]):
                    [self.vx, self.vy] = [+(self.vy + self.vx), 0]
                    self.color = "blue"
                else:
                    [self.vx, self.vy] = [-(self.vy + self.vx), 0]
                    self.color = "blue"

                ##Bottom of the obstacle
                if self.Distance([ListObstacles[i].ycenter + ListObstacles[i].radius,
                                  ListObstacles[i].xcenter - ListObstacles[i].radius]) > self.Distance(
                    [ListObstacles[i].ycenter + ListObstacles[i].radius,
                     ListObstacles[i].xcenter + ListObstacles[i].radius]):
                    [self.vx, self.vy] = [+(self.vy + self.vx), 0]
                    self.color = "blue"
                else:
                    [self.vx, self.vy] = [-(self.vy + self.vx), 0]
                    self.color = "blue"

    def col(self, p):

        v1 = self.vit
        th1 = self.theta
        v2 = p.vit
        th2 = p.theta

        theta11 = math.atan((v2 / v1) * (math.sin(th2) / math.cos(th1)))
        v11 = math.sqrt((v2 * math.sin(th2)) ** 2 + (v1 * math.cos(th1)) ** 2)

        theta22 = math.atan((v1 / v2) * (math.sin(th1) / math.cos(th2)))
        v22 = math.sqrt((v1 * math.sin(th1)) ** 2 + (v2 * math.cos(th2)) ** 2)
        # il faut projeter sur le repere xy de l'affichage et modif vx et vy

        self.vx = v11 * math.cos(theta11)
        self.vy = v11 * math.sin(theta11)

        p.vx = v22 * math.sin(theta22)
        p.vy = v22 * math.sin(theta22)
