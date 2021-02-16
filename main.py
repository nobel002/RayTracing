import pygame
from line import Line
from particle import Particle
from enviroment import Enviroment
from math import sin, cos
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024, 512))
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
running = 1
particle = Particle([256, 256])
enviroment = Enviroment()
enviroment + Line(-1, 256, 256, 512)

def drawParticle(particle):
    scale = 25
    pygame.draw.circle(screen, BLUE, particle.pos, 5)
    pygame.draw.aaline(screen, RED,particle.pos, [particle.pos[0] + scale * cos(particle.heading), particle.pos[1] + scale * sin(particle.heading)])

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        else:
            pass
    screen.fill((255, 255, 255))
    for item in enviroment.array:
        pygame.draw.aaline(screen, BLACK, item.points[0], item.points[1])
    drawParticle(particle)
    pygame.draw.line(screen, BLACK, [512, 0], [512, 512], 5)
    pygame.display.flip()

pygame.quit()
