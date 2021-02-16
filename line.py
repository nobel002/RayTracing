from math import cos, sin, pi

class Line(object):
    def __init__(self, rico, offset, beginX, endX):
        self.rico = rico
        self.offset = offset
        self.beginX = beginX
        self.endX = endX
        self.pygameMode = True  # this is set to true cause i use this here in a pygame enviroment sow
        if self.rico != None and self.offset != None:
            self.beginPoints = [(self.beginX, self.beginX * self.rico + self.offset),
                                (self.endX, self.endX * self.rico + self.offset)]

    def calcIntersect(self, other):
        xIntersect = (other.offset - self.offset) / (self.rico - other.rico)
        yIntersect = self.rico * xIntersect + self.offset

        absXbegin = self.beginX if self.beginX < other.beginX else other.beginX
        absXend = self.endX if self.endX > other.endX else other.endX

        coords = [None, None]
        if xIntersect >= absXbegin and xIntersect <= absXend:
            coords = [xIntersect, yIntersect]

        beginPos = [self.beginX, self.rico * self.beginX + self.offset]

        distance = None
        if coords != (None, None):
            distane = ((beginPos[0] - coords[0]) ** 2 + (beginPos[1] - coords[1]) ** 2) ** 0.5
        coords[1] = -coords[1] if self.pygameMode and coords != (None, None) else coords[1]
        returnObj = {"begin": beginPos,
                     "intersect": coords,
                     "distance": distance}
        return returnObj

    def drawCoords(self):
        beginPos = [self.beginX, self.rico * self.beginX + self.offset]
        endPos = [self.endX, self.rico * self.endX + self.offset]
        return (beginPos, endPos)

    def fromTwoPoints(self, point1, point2):
        self.rico = point2[1]-point1[1]/point2[0]-point1[0]
        self.offset = point1[0] * (point2[1] - point1[1] / point2[0] - point1[0]) + point1[1]
        
    def rotateLine(self, angle=pi / 6, origin=(0, 0)):
        #fist subtract the origin vector from the point vectors
        p1 = [self.beginPoints[0][0] - origin[0], self.beginPoints[0][1] - origin[1]]
        p2 = [self.beginPoints[1][0] - origin[0], self.beginPoints[1][1] - origin[1]]
        #rotate set points
        xAccentPOne = self.beginPoints[0][0] * cos(angle) - self.beginPoints[0][1] * sin(angle)
        yAccentPOne = self.beginPoints[0][1] * cos(angle) + self.beginPoints[0][0] * sin(angle)

        xAccentPTwo = self.beginPoints[1][0] * cos(angle) - self.beginPoints[1][1] * sin(angle)
        yAccentPTwo = self.beginPoints[1][1] * cos(angle) + self.beginPoints[1][0] * sin(angle)

        #add the origin vector to the newly rotated points this has to happen in this order to prevent distortion
        p1 = [xAccentPOne + origin[0], yAccentPOne + origin[1]]
        p2 = [xAccentPTwo + origin[0], yAccentPTwo + origin[1]]
        self.fromTwoPoints(p1, p2)
        #return the updated line
        return self

if __name__ == "__main__":
    line = Line(None, None, -1000000, 1000000)
    line.fromTwoPoints((0, -3), (1, 7))
    print(line)
    pass
