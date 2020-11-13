import pygame
from pygame.draw import *

# pylint: disable=no-member
pygame.init()
# pylint: enable=no-member

FPS = 30
SIZE = (400,400)

screen = pygame.display.set_mode(SIZE)


rect(screen, (255,0,255), (100,100,200,200))
rect(screen, (0,0,255), (100,100,200,200),5)
polygon(screen, (255,255,0), [(100,100), (200,50), 
                              (300,100), (100,100)])
polygon(screen, (0,0,255), [(100,100), (200,50), 
                            (300,100), (100,100)], 5)
circle(screen, (0,255,0), (200,175), 50)
circle(screen, (255,255,255), (200,175), 50, 5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()