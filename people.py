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

    """

    def _init_(self, name, color='Yellow',
               xcoord=50.0, ycoord=0.0, radius=1):
        """
        Constructor of a Goal object
        """
        self.name = name
        self.color = color
        self.xcoord, self.ycoord = [xcoord, ycoord]  # They are the coordinates of the center of the particle
        self.radius = radius
        Circle((xcoord, ycoord), radius)

    def _str_(self):
        """
        Print this Goal object
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
