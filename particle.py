from line import Line
import math


class Particle(Object):
    def __init__(self, pos, fov=math.pi / 6, numOfRays=100, heading=0):
        self.pos = pos
        self.heading = heading  # should be an agle in radians
        self.fov = fov  # should be in radians
        self.numOfRays = numOfRays  # should ba an int

    def see(self, enviroment):
        lineOfSight = []
        oldLine = Line(0,0,0,2048)
        for line in range(fov):
           closes = math.inf
           oldLine = Line()
           for item in enviroment:
               Line(0, 0, 0, 2048).rotateLine()
        return lineOfSight
