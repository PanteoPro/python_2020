import pygame
from pygame.draw import *

# pygame.draw.rect => rect()

SIZE = (400, 400)
FPS = 30
# pylint: disable=no-member
pygame.init()
# pylint: enable=no-member

# Create window
screen = pygame.display.set_mode(SIZE)

# Draw figures there



# end draw

# Then we should be update display to representation image
pygame.display.update()
# This command need repeat to update display image



# set fps
clock = pygame.time.Clock()

# main loop where all events, while event.type not pygame.QUIT
# pylint: disable=no-member
finished = False
while finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
# pylint: enable=no-member