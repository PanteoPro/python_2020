import pygame
from pygame.draw import *

SIZE = (400,300)
FPS = 30

WHITE = (255,255,255)

pygame.init()
screen = pygame.display.set_mode(SIZE)


x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
rect(screen, WHITE, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, WHITE, (x, y1), (x, y2))
    x += h


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()