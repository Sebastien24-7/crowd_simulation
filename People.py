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
    def __init__(self,xcoord,ycoord,vx,vy):
        """
        Constructor of a Particle object
        """
        self.name = "Particle"
        colors = ["red", "orange", "yellow", "green", "blue", "violet"]
        #self.color = random.choice(colors)
        self.color ="#{:06x}".format(random.randint(0, 0xffffff))
        self.xcoord, self.ycoord = [xcoord, ycoord]  # They are the coordinates of the center of the particle
        self.touched = 0
        self.masse = 1
        self.vx,self.vy = (vx,vy)
        self.radius = 1
        self.out = False

    def __str__(self):
        """
        Print this Particle object
        """
        return "--> Je suis un objet People " \
               + "\n    name: " + str(self.name) \
               + "\n    color: " + str(self.color) \
               + "\n    xcoord: " + str(self.xcoord) \
               + "\n    ycoord: " + str(self.ycoord) \
               + "\n    touched: " + str(self.touched) \
 \
            ############
    def people_wall_distance(self):
        """
        Determines the distance between of all the particles and their nearest walls
        """

    def people_target_distance(self):
        """
        Determines the distance for all the particles between them and their targets
        """
        coord_sortie=[0,-20]
        D=[self.xcoord-coord_sortie[0],self.ycoord-coord_sortie[1]]
        D_norm=D/numpy.linalg.norm(D)
        return D_norm