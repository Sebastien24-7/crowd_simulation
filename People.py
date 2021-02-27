import numpy as np
import scipy as sp
import sys
import random
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.patches import Circle, Rectangle, Polygon
import PIL
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

    def _init_(self):
        """
        Constructor of a Particle object
        """
        self.name = "Particle"
        self.color = "Yellow"
        self.xcoord, self.ycoord = [50.0, 50.0]  # They are the coordinates of the center of the particle
        self.radius = 1
        return (self.xcoord, self.ycoord, self.radius, self.color, self.name)

    def _str_(self):
        """
        Print this Particle object
        """
        return "--> Goal: " \
               + "\n    name: " + str(self.name) \
               + "\n    color: " + str(self.color) \
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
