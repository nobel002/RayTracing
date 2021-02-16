from line import Line
import math
from math import sin, cos


class Particle(Object):
    def __init__(self, pos, fov=math.pi / 6, numOfRays=100, heading=0):
        self.pos = pos
        self.heading = heading  # should be an agle in radians
        self.fov = fov  # should be in radians
        self.numOfRays = numOfRays  # should ba an int
        self.deltaAngle = fov/numOfRays

    def see(self, enviroment):
        lineOfSight = []
        oldLine = Line(0, 0, 0, 2048)
        oldLine.fromTwoPoints(self.pos, (self.pos[0] + cos(self.heading), self.pos[1] + sin(self.heading)))
        for line in range(fov):
           closes = math.inf
           closestIntersectPoint = oldLine
           relativeIndex = fov/2 - line 
           oldLine.rotateLine(relativeIndex-self.deltaAngle)
           for item in enviroment:
               if oldLine.calcIntersect(item)["distance"] <= closes:
                    closes = oldLine.calcIntersect(item)["distance"]
                    closestIntersectPoint = oldLine.calcIntersect(item)["intersect"]
           lineOfSight.append(closestIntersectPoint)
        return lineOfSight
