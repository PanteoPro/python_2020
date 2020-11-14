import pygame
from pygame.draw import *

SIZE = (1000, 800)
FPS = 30
# pylint: disable=no-member
pygame.init()
# pylint: enable=no-member

BLACK = (0,0,0)

screen = pygame.display.set_mode(SIZE)

rect(screen, (233,230,200), (0,0,1000,800))

# pygame.transform.rotate(surface, 330)
# surface = pygame.Surface([70, 120], pygame.SRCALPHA)
# screen.blit(surface_rot, [196, 111])


# pygame.draw.polygon(screen, BLACK, [[650, 400], [650, 490], [620, 520], [600, 500], [600, 400]])

# surface = pygame.Surface([30, 140], pygame.SRCALPHA)
# pygame.draw.ellipse(surface, BLACK, (0, 0, 60, 200))
# surface_rot = pygame.transform.rotate(surface, 0)
# screen.blit(surface_rot, [590, 360])

surface = pygame.Surface([180, 340], pygame.SRCALPHA)
pygame.draw.ellipse(surface, BLACK, (0, 0, 180, 700))
surface_rot = pygame.transform.rotate(surface, -10)
screen.blit(surface_rot, [20, 471])



pygame.display.update()
clock = pygame.time.Clock()
end = False
# pylint: disable=no-member
while not end:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
pygame.quit()
# pylint: enable=no-member