import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (225, 149, 73)
GREEN = (0, 136, 31)
WHITE = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode([1000, 600])

pygame.display.set_caption("Picture 6 (panda)")

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(ORANGE)

    pi = 3.14

#Большое дерево 

    #Большое дерево: ствол
    pygame.draw.line(screen, GREEN, [440, 440], [440, 330], 28)
    pygame.draw.line(screen, GREEN, [440, 315], [440, 205], 28)

    surface = pygame.Surface([50, 75], pygame.SRCALPHA)
    pygame.draw.line(surface, GREEN, [0, 0], [0, 75], 40)
    surface_rot = pygame.transform.rotate(surface, 345)
    screen.blit(surface_rot, [425, 113])

    surface = pygame.Surface([25, 100], pygame.SRCALPHA)
    pygame.draw.line(surface, GREEN, [0, 0], [0, 100], 25)
    surface_rot = pygame.transform.rotate(surface, 340)
    screen.blit(surface_rot, [440, 1])
    

    #Большое дерево: листья
    #верхняя правая ветка большого дерева
    
    pygame.draw.arc(screen, GREEN, (470, 1, 480, 350), pi - 200*pi/480, pi - 60*pi/480, 4)
    surface = pygame.Surface([85, 120], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, GREEN, (7, 0, 85, 9))
    pygame.draw.ellipse(surface, GREEN, (0, 21, 85, 9))
    pygame.draw.ellipse(surface, GREEN, (6, 36, 85, 9))
    pygame.draw.ellipse(surface, GREEN, (0, 51, 85, 9))
    pygame.draw.ellipse(surface, GREEN, (1, 66, 85, 9))
    surface_rot = pygame.transform.rotate(surface, 113)
    screen.blit(surface_rot, [560, 0])
    
    #нижняя правая ветка большого дерева

    surface = pygame.Surface([210, 190], pygame.SRCALPHA)
    pygame.draw.arc(surface, GREEN, (0, 0, 200, 180), pi/20, 11*pi/20, 4)
    surface_rot = pygame.transform.rotate(surface, 60)
    screen.blit(surface_rot, [440, 120])
 
    surface = pygame.Surface([75, 120], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, GREEN, (0, 0, 70, 9))
    pygame.draw.ellipse(surface, GREEN, (5, 17, 70, 9))
    pygame.draw.ellipse(surface, GREEN, (0, 34, 70, 9))
    surface_rot = pygame.transform.rotate(surface, 110)
    screen.blit(surface_rot, [530, 137])


    #верхняя левая ветка большого дерева

    pygame.draw.arc(screen, GREEN, (-100, 40, 520, 350), pi/8, pi/2, 4)
    
    surface = pygame.Surface([95, 120], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, GREEN, (7, 0, 85, 9))
    pygame.draw.ellipse(surface, GREEN, (0, 17, 85, 9))
    pygame.draw.ellipse(surface, GREEN, (6, 34, 85, 9))
    pygame.draw.ellipse(surface, GREEN, (0, 51, 85, 9))
    pygame.draw.ellipse(surface, GREEN, (1, 74, 85, 9))
    surface_rot = pygame.transform.rotate(surface, 79)
    screen.blit(surface_rot, [180, 44])

    #нижняя левая ветка большого дерева

    pygame.draw.arc(screen, GREEN, (200, 220, 210, 170), 2*pi/20, 12*pi/20, 3)

    surface = pygame.Surface([75, 120], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, GREEN, (0, 0, 70, 9))
    pygame.draw.ellipse(surface, GREEN, (5, 17, 70, 9))
    pygame.draw.ellipse(surface, GREEN, (0, 34, 70, 9))
    surface_rot = pygame.transform.rotate(surface, 75)
    screen.blit(surface_rot, [288, 220])



 #Маленькое дерево, первое слева (дерево -1)

    #маленькое дерево -1: ствол
    pygame.draw.line(screen, GREEN, [263, 494], [263, 410], 14)
    pygame.draw.line(screen, GREEN, [263, 401], [263, 315], 14)

    surface = pygame.Surface([80, 100], pygame.SRCALPHA)
    pygame.draw.line(surface, GREEN, [20, 20], [65, 70], 12)
    surface_rot = pygame.transform.rotate(surface, 134)
    screen.blit(surface_rot, [206, 203])

    surface = pygame.Surface([100, 100], pygame.SRCALPHA)
    pygame.draw.line(surface, GREEN, [20, 20], [60, 85], 9)
    surface_rot = pygame.transform.rotate(surface, 135)
    screen.blit(surface_rot, [196, 111])

#Панда
    #Тело
    pygame.draw.ellipse(screen, WHITE, (600, 340, 240, 120))

    #Задняя лапа
    surface = pygame.Surface([70, 120], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, BLACK, (0, 0, 60, 125))
    surface_rot = pygame.transform.rotate(surface, 330)
    screen.blit(surface_rot, [740, 390])
    
    surface = pygame.Surface([25, 50], pygame.SRCALPHA)
    pygame.draw.circle(surface, BLACK, (25, 25), 25)
    surface_rot = pygame.transform.rotate(surface, 20)
    screen.blit(surface_rot, [735, 468])

    #передняя лапа 1
    pygame.draw.polygon(screen, BLACK, [[680, 490], [740, 340], [740, 460], [730, 510], [700, 530]])
    
    surface = pygame.Surface([45, 55], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, BLACK, (0, 0, 120, 60)) 
    surface_rot = pygame.transform.rotate(surface, 10)
    screen.blit(surface_rot, [650, 477])

    #передняя лапа 2
    pygame.draw.polygon(screen, BLACK, [[650, 400], [650, 490], [620, 520], [600, 500], [600, 400]])
    
    surface = pygame.Surface([30, 140], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, BLACK, (0, 0, 60, 200))
    surface_rot = pygame.transform.rotate(surface, 0)
    screen.blit(surface_rot, [590, 360])
    
    surface = pygame.Surface([40, 38], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, BLACK, (0, 0, 40, 100))
    surface_rot = pygame.transform.rotate(surface, 65)
    screen.blit(surface_rot, [584, 471])
   
    #морда
    pygame.draw.ellipse(screen, WHITE, (605, 300, 130, 140)) 
    pygame.draw.ellipse(screen, WHITE, (620, 290, 100, 140))
   
    surface = pygame.Surface([110, 150], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, WHITE, (0, 0, 100, 140))
    surface_rot = pygame.transform.rotate(surface, 160)
    screen.blit(surface_rot, [580, 280])

    pygame.draw.ellipse(screen, BLACK, (610, 412, 34, 22))
    pygame.draw.ellipse(screen, BLACK, (603, 358, 25, 35))
    pygame.draw.circle(screen, BLACK, [668, 386], 16)

    surface = pygame.Surface([55, 26], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, BLACK, (0, 0, 80, 40))
    surface_rot = pygame.transform.rotate(surface, 40)
    screen.blit(surface_rot, [595, 286])
 
    surface = pygame.Surface([25, 26], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, BLACK, (0, 0, 50, 27))
    surface_rot = pygame.transform.rotate(surface, 200)
    screen.blit(surface_rot, [636, 280])
 
    surface = pygame.Surface([55, 26], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, BLACK, (0, 0, 80, 40))
    surface_rot = pygame.transform.rotate(surface, 300)
    screen.blit(surface_rot, [690, 286])

    surface = pygame.Surface([30, 25], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, BLACK, (0, 0, 50, 30))
    surface_rot = pygame.transform.rotate(surface, 100)
    screen.blit(surface_rot, [713, 330])




    pygame.display.flip()


pygame.quit()