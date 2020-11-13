import pygame
from pygame.draw import *

SIZE = (500,500)
CENTER = (int(SIZE[0]/2), int(SIZE[1]/2))
FPS = 30


EYE_Y = CENTER[1] - 70
EYE_SPACE = 80

LEFT_EYE = (CENTER[0]-EYE_SPACE, EYE_Y)
RIGHT_EYE = (CENTER[0]+EYE_SPACE, EYE_Y)


YELLOW = (255,255,0)
RED = (255,0,0)
BLACK = (0,0,0)
LIGHT_GREY = (210,210,210)


pygame.init()

screen = pygame.display.set_mode(SIZE)

rect(screen, LIGHT_GREY, (0,0,SIZE[0],SIZE[1]))

circle(screen, YELLOW, CENTER, 200)
circle(screen, BLACK, CENTER, 200, 2)

rect(screen, BLACK, (CENTER[0]-80, CENTER[1]+110, 160, 30))

circle(screen, RED, LEFT_EYE, 40)
circle(screen, BLACK, LEFT_EYE, 40, 2)
circle(screen, BLACK, LEFT_EYE, 15)

circle(screen, RED, RIGHT_EYE, 30)
circle(screen, BLACK, RIGHT_EYE, 30, 2)
circle(screen, BLACK, RIGHT_EYE, 15)

polygon(screen, BLACK, [(74, 80), (98, 53), (244, 157), (230, 177)])
polygon(screen, BLACK, [(295, 169), (277, 157), (388, 54), (395, 66)])




pygame.display.update()
clock = pygame.time.Clock()
finished = False

# pylint: disable=no-member
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

pygame.quit()
# pylint: enable=no-member
