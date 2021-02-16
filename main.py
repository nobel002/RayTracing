import pygame
from line import Line
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024, 512))

running = 1


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        else:
            pass
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), [512, 0], [512, 512], 5)
    pygame.display.flip()

pygame.quit()
