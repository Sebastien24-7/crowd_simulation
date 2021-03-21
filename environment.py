from numpy import *
import scipy as sp
import sys
import random
import matplotlib
import matplotlib.pyplot as plt
import self

from matplotlib.patches import Ellipse, Circle, Rectangle, Polygon
from matplotlib.lines import Line2D
import PIL
from PIL import Image
from PIL import ImageDraw

###############################
from numpy.ma import shape


class Goal():
    """
    Defines the goals to reach for the particles or the people (ex: a door)

    ------
    Attributes :
    name: string
        name of the destination
    colors: list
       List of colors ``[ [r,g,b],... ]`` drawing the destination.
       For example, a door can be represented by a blue line

    """

    def _init_(self, name, colors, pixel_size=1.0,
               xcoord=50.0, width=10,
               ycoord=0.0, height=5):
        """
        Constructor of a Goal object
        """
        self.name = name
        self.colors = colors

    def _str_(self):
        """
        Print this Goal object
        """
        return "--> Goal: " \
               + "\n    name: " + str(self.name) \
               + "\n    colors: " + str(self.colors) \
 \
 \
###############################

class Room():
    """
    Setup the place where the people will interact
    To define the computational domain:
     * a background: empty (white) or a PNG image which only
       contains the colors white, blue (for the doors) and black
       (for the walls/obstacles)
     * supplementary doors represented by matplotlib shapes:
        ``line2D``
     * supplementary walls/obstacles represented by matplotlib shapes: (will be added thanks to Obstacle class
        ``line2D``, ``circle``, ``ellipse``, ``rectangle`` or ``polygon``
    To compute the obstacle distances and the desired velocities

    -------
    Attributes :

    """

    def __init__(self, name='Room', background='White', pixel_size=1.0,
                 xmin=0.0, width=500,
                 ymin=0.0, height=500,
                 wall_colors=[[0, 0, 0]], ):
        """
        Constructor of a Room object

        Parameters
        ----------
        name: string
            domain name (default: 'Room')
        background: string
            name of the background image (default: 'White', no image)
        pixel_size: float
            size of a pixel in meters (default: 1.0)
        xmin: float
            x coordinate of the origin, bottom left corner (default: 0.0)
        ymin: float
            y coordinate of the origin, bottom left corner (default: 0.0)
        width: int
            width of the background image (default: 100 pixels)
        height: int
            height of the background image (default: 100 pixels)
        """
        self.name = name
        self.__background = background
        self.pixel_size = pixel_size
        self.wall_colors = wall_colors  # walls are black by default
        self.xmin, self.ymin = [xmin, ymin]
        self.width, self.height = [width, height]
        self.xmax = self.xmin + self.width * pixel_size
        self.ymax = self.ymin + self.height * pixel_size

    def __str__(self):
        """
        Print this Room object
        """
        return "--> Je suis un objet Pièce " \
               + "\n    name: " + str(self.name) \
               + "\n    background: " + str(self.__background) \
               + "\n    xmin: " + str(self.xmin) \
               + "\n    ymin: " + str(self.ymin) \
               + "\n    xmax: " + str(self.xmax) \
               + "\n    ymax: " + str(self.ymax) \
               + "\n    width: " + str(self.width) \
               + "\n    height: " + str(self.height) \
 \
 \
###############################

class Obstacle():
    """
    * supplementary walls/obstacles represented by matplotlib shapes: (will be added thanks to Obstacle class
    ``line2D``, ``circle``, ``ellipse``, ``rectangle`` or ``polygon``
    To compute the obstacle distances and the desired velocities

    -------
    Attributes :

    """

    def __init__(self, name='Goal', background='Black', pixel_size=1.0,
                 xcoord=0.0, width=50,
                 ycoord=0.0, height=50):
        """
        Constructor of an Obstacle object
        """
        self.__shapes = []
        self.__outline_color_shapes = []
        self.__fill_color_shapes = []
        self.__image_filename = ''
        self.name = name
        self.__background = background
        self.destinations = None
        self.pixel_size = pixel_size
        self.xcoord, self.ycoord = [xcoord, ycoord]
        self.width, self.height = [width, height]

    pass

    def __str__(self):
        """
        Print this Room object
        """
        return "--> Je suis un objet Obstacle " \
               + "\n    name: " + str(self.name) \
               + "\n    background: " + str(self.__background) \
               + "\n    xcoord: " + str(self.xcoord) \
               + "\n    ycoord: " + str(self.ycoord) \
               + "\n    width: " + str(self.width) \
               + "\n    height: " + str(self.height) \
 \
            ############

    def add_shape(self, shape, outline_color=[0, 0, 0], fill_color=[255, 255, 255]):
        """To add a matplotlib shape:
        ``line2D``, ``circle``, ``ellipse``, ``rectangle`` or ``polygon``
        Parameters
        ----------
        shape: matplotlib shape
            line2D, circle, ellipse, rectangle or polygon
        outline_color: list
            rgb color
        fill_color: list
            rgb color
        """
        self.__shapes.append(shape)
        self.__outline_color_shapes.append(outline_color)
        self.__fill_color_shapes.append(fill_color)
        self.image = Image.open(self.__background)
        self.draw = ImageDraw.Draw(self.image)

        if (isinstance(shape, Circle) or isinstance(shape, Ellipse) or
                isinstance(shape, Rectangle) or isinstance(shape, Polygon)):
            xy = shape.get_verts() / self.pixel_size
            xy[:, 1] = self.height - xy[:, 1]
            self.draw.polygon(sp.around(xy.flatten()).tolist(),
                              outline="rgb(" + str(outline_color[0]) + "," +
                                      str(outline_color[1]) + "," +
                                      str(outline_color[2]) + ")",
                              fill="rgb(" + str(fill_color[0]) + "," +
                                   str(fill_color[1]) + "," +
                                   str(fill_color[2]) + ")")
            linewidth = shape.get_linewidth()
            self.draw.line(sp.around(xy.flatten()).tolist(),
                           width=int(linewidth),
                           fill="rgb(" + str(outline_color[0]) + "," +
                                str(outline_color[1]) + "," +
                                str(outline_color[2]) + ")")
        elif isinstance(shape, Line2D):
            linewidth = shape.get_linewidth()
            xy = shape.get_xydata() / self.pixel_size
            xy[:, 1] = self.height - xy[:, 1]
            self.draw.line(sp.around(xy.flatten()).tolist(),
                           width=int(linewidth),
                           fill="rgb(" + str(outline_color[0]) + "," +
                                str(outline_color[1]) + "," +
                                str(outline_color[2]) + ")")
