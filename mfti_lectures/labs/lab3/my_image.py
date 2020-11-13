import pygame
from pygame.draw import *

SIZE = (1600, 800)
FPS = 30

BG1 = (254,213,162)
BG2 = (254,213,196)
BG3 = (254,213,148)
BG4 = (179,134,148)
YELLOW = (252,238,33)
MOUNT_BACK = (252,152,49)
MOUNT_FRONT = (172,67,52)


def draw_background():
    pass

def draw_sun():
    pass

def draw_mount_back():
    pass

def draw_mount_front():
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    # Drawing

    draw_background()
    draw_sun()
    draw_mount_back()
    draw_mount_front()

    # End Drawing

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    pygame.quit()


if __name__ == "__main__":
    main()