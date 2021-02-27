import sys
import random
import matplotlib

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

    def __init__(self,xcoord,ycoord):
        """
        Constructor of a Particle object
        """
        self.name = "Particle"
        self.color = "Yellow"
        self.xcoord, self.ycoord = [xcoord, ycoord]  # They are the coordinates of the center of the particle
        self.radius = 1

    def __str__(self):
        """
        Print this Particle object
        """
        return "--> Je suis un objet People " \
               + "\n    name: " + str(self.name) \
               + "\n    color: " + str(self.color) \
               + "\n    xcoord: " + str(self.xcoord) \
               + "\n    ycoord: " + str(self.ycoord) \
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
