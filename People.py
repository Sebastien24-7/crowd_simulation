

###############################

class People:
    """
    Defines the particle to represent and interact with (ex: an animal / a human being)

    ------
    Attributes :
    name: string
        name of the people/particle
    color: string
        particles are represented as yellow

    """

    def __init__(self, name, color,xcoord, ycoord, radius,vx, vy):
        """
        Constructor of a Particle object
        """
        self.name = name
        self.color = color
        self.xcoord, self.ycoord = [xcoord, ycoord]  # They are the coordinates of the center of the particle
        self.radius = radius
        self.vx=vx
        self.vy=vy

    def __str__(self):
        """
        Print this Particle object
        """
        return "--> Goal: " \
               + "\n    name : " + str(self.name) \
               + "\n    color : " + str(self.color) \
               + "\n    xcoord : " + str(self.xcoord) \
               + "\n    ycoord : " + str(self.ycoord) \
               + "\n    vx: " + str(self.vx) \
               + "\n    vy: " + str(self.vy) \
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
        xcoord_sortie=200
        ycoord_sortie=0
