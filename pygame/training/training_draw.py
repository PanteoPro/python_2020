import pygame
from pygame.draw import *
from pygame.surface import *
from pygame.image import *
from pygame.transform import *
import math

RED = (255,0,0)

def draw_simple_shapes(screen):
    """
        In module draw of pygame means there are 9 simple shapes like:
        1) pygame.draw.rect - прямоугольник
        2) pygame.draw.polygon - многоугольник
        3) pygame.draw.circle - круг
        4) pygame.draw.ellipse - Эллипс
        5) pygame.draw.arc - дуга
        6) pygame.draw.line - линия
        7) pygame.draw.lines - линии 
        8) pygame.draw.aaline
        9) pygame.draw.aalines
    """

    rect(screen, RED, (10,10, 100, 40), border_radius=10)
    polygon(screen, RED, ((130, 10), (140, 50), (180, 30), (160, 10)))
    circle(screen, RED, (210,30), 20, 0, True, False, True)
    ellipse(screen, RED, (240,10, 50, 120))
    arc(screen, RED, (300, 10, 50, 120), 0, 8*math.pi/12)
    arc(screen, RED, (300, 10, 50, 120), math.pi, -4*math.pi/12)
    line(screen, RED, (360,10), (400, 50), 10)
    line(screen, RED, (400,50), (360, 90), 10)
    lines(screen, RED, False, ((410,10), (450, 50), (410, 90), (450, 90)), 10)
    lines(screen, RED, True, ((410+60,10), (450+60, 50), (410+60, 90), (450+60, 90)), 10)


def draw_surfaces(screen):
    ball_image1 = load("pygame/training/images/ball.jpg").convert() # Load Not alpha images
    ball_image2 = load("pygame/training/images/ball.png").convert() # BAD LOAD
    ball_image3 = load("pygame/training/images/ball.png").convert_alpha() # Loads PNG

    simple_surface = Surface((100,100))
    rect(simple_surface, RED, (10,10,80,100), 10)

    screen.blit(simple_surface, (10,100))
    screen.blits(( (simple_surface, (10, 210)), (simple_surface, (110, 210)) ))

    screen.blit(ball_image1, (10, 320))
    screen.blit(ball_image2, (150, 320))
    screen.blit(ball_image3, (450, 320))

    copy_simple_surface = Surface.copy(simple_surface)
    rect(copy_simple_surface, (0,255,0), (40,40,20,20))
    screen.blit(copy_simple_surface, (110, 100))

    copy_simple_surface.fill((0,0,0))
    ellipse(copy_simple_surface, RED, (10, 10, 200, 80), 10)
    screen.blit(copy_simple_surface, (10, 450))
    copy_simple_surface.set_colorkey((0,0,0)) # MAke PNG hahpa, create alpha
    screen.blit(copy_simple_surface, (10, 560))
    rect_surface = copy_simple_surface.get_rect()
    rect_surface = rect_surface.move(100,100)
    screen.blit(ball_image1, rect_surface)




# pygame.draw.rect => rect()

SIZE = (800, 800)
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

ball_image3 = load("pygame/training/images/ball.png").convert_alpha()
ball_rect = ball_image3.get_rect()
ball_rect2 = ball_image3.get_rect()
ball_rect2 = ball_rect2.move(500,0)

angle = 0


finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill((25,25,25))
    angle += 1

    draw_simple_shapes(screen)
    draw_surfaces(screen)
    ball_rect = ball_rect.move(1,1)
    ball_rect2 = ball_rect2.move(-1,1)
    new_image = flip(ball_image3, 0, 1)
    new_image = rotate(new_image, angle)
    screen.blit(ball_image3, ball_rect)
    screen.blit(new_image, ball_rect2)

    pygame.display.update()
pygame.quit()
# pylint: enable=no-member