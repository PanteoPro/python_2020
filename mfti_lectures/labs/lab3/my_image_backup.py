import pygame
from pygame.draw import *
import math

SIZE = (1600, 800)
FPS = 30

BG1 = (254,213,162)
BG2 = (254,213,196)
BG3 = (254,213,148)
BG4 = (179,134,148)
YELLOW = (252,238,33)
MOUNT_BACK = (252,152,49)
MOUNT_FRONT = (172,67,52)
MOUNT_FRONT_FIRST = (48,16,38)
BIRD_COLOR = (66,33,11)


class Entity:
    """
    Object has x,y
    """
    def __init__(self, pos:tuple, color:tuple):
        self.x = pos[0];
        self.y = pos[1];
        self.color = color
    

class Rectangle(Entity):
    """
    
    """
    def __init__(self, pos:tuple, color:tuple, size:tuple, width=0):
        self.size_x = size[0]
        self.size_y = size[1]
        self.width = width
        super().__init__(pos, color)


class RectangleBlockMenu(Rectangle):
    """
    """
    def __init__(self, pos:tuple, color:tuple, size:tuple, width:int, background_color:tuple, text:str, figure:str):
        self.background_color = background_color
        self.text = text
        self.figure = figure # rect, line, circle
        self.select = False 
        super().__init__(pos,color, size, width)
    

    def draw(self, screen):
        surface = pygame.Surface([self.size_x, self.size_y], pygame.SRCALPHA)
        rect(surface, self.background_color, (0, 0, self.size_x, self.size_y))
        rect(surface, self.color, (0, 0, self.size_x, self.size_y), self.width)
        
        if self.figure == "rect":
            rect(surface, MOUNT_FRONT, (20, int(self.size_y/2) - int(self.size_y/5), self.size_x - 40, int(self.size_y/5)), 5)
        elif self.figure == "line":
            line(surface, MOUNT_FRONT, (20, int(self.size_y/2)), (self.size_x - 20,self.size_y/2), 5)
        elif self.figure == "circle":
            print(int(self.size_x/5))
            circle(surface, MOUNT_FRONT, (self.size_x/2, self.size_y/2), int(self.size_x/5), 5)

        font = pygame.font.Font(None, 20)
        text = font.render(self.text, True, YELLOW)
        place = text.get_rect(center=(self.x + (self.size_x/2), self.y + (self.size_y-20)))
        screen.blit(surface, (self.x,self.y))
        screen.blit(text, place)

    def clicked(self, x, y):
        if x >= self.x and x <= self.x + self.size_x and y >= self.y and y <= self.y + self.size_y:
            print("clicked on " + self.figure)


menus = []

menus.append(RectangleBlockMenu((10,10),BIRD_COLOR, (100,100), 10, BG4, "draw line", "line"))
menus.append(RectangleBlockMenu((120,10),BIRD_COLOR, (100,100), 10, BG4, "draw rect", "rect"))
menus.append(RectangleBlockMenu((230,10),BIRD_COLOR, (100,100), 10, BG4, "draw circle", "circle"))


def draw_background(screen):
    rect(screen, BG1, (0, 0, SIZE[0], SIZE[1]/5))
    rect(screen, BG2, (0, SIZE[1]/5, SIZE[0], SIZE[1]/5))
    rect(screen, BG3, (0, SIZE[1]/5*2, SIZE[0], SIZE[1]/5))
    rect(screen, BG4, (0, SIZE[1]/5*3, SIZE[0], SIZE[1]/5*2))

def draw_sun(screen):
    circle(screen, YELLOW, (SIZE[0]/2 - 80, SIZE[1]/5), 70)

def draw_bird(screen, x, y, size):
    pass

def draw_mount_front_first(screen):
    polygon(screen, MOUNT_FRONT_FIRST, [
        (0, 374),
        (106, 398),
        (160, 441),
        (457, 713),
        (460, 721),
        (466, 732),
        (481, 742),
        (496, 750),
        (518, 759),
        (541, 766),
        (567, 772),
        (593, 772),
        (642, 774),
        (662, 774),
        (683, 774),
        (700, 773),
        (970, 634),
        (1035, 668),
        (1050, 679),
        (1063, 691),
        (1073, 700),
        (1088, 710),
        (1112, 717),
        (1134, 721),
        (1156, 721),
        (1179, 719),
        (1201, 709),
        (1218, 695),
        (1234, 680),
        (1247, 664),
        (1264, 659),
        (1271, 651),
        (1289, 641),
        (1300, 627),
        (1313, 606),
        (1323, 590),
        (1600, 590),
        (1600, 800),
        (0, 800),  
    ])  

    # surface = pygame.Surface([500, 100], pygame.SRCALPHA)
    # pygame.draw.ellipse(surface, BG4, (0, 0, 550, 700))
    # surface_rot = pygame.transform.rotate(surface, -150)
    # screen.blit(surface_rot, (1000, 500))

def draw_mount_front(screen):
    polygon(screen, MOUNT_FRONT, [
        (1600, 513),
        (1600, 261),
        (1518, 347),
        (1441, 325),
        (1389, 385),
        (1313, 346),
        (1236, 415),
        (1178, 399),
        (1170, 392),
        (1164, 386),
        (1158, 379),
        (1153, 374),
        (1142, 361),
        (1133, 351),
        (1127, 342),
        (1120, 334),
        (1113, 324),
        (1105, 311),
        (1101, 305),
        (1090, 298),
        (1076, 294),
        (1063, 287),
        (1050, 283),
        (1028, 282),
        (1013, 282),
        (1007, 282),
        (994, 286),
        (981, 289),
        (970, 294),
        (961, 298),
        (946, 304),
        (931, 313),
        (917, 320),
        (906, 328),
        (898, 334),
        (887, 342),
        (872, 350),
        (864, 356),
        (726, 389),
        (573, 330),
        (496, 284),
        (447, 380),
        (373, 333),
        (297, 440),
        (297, 435),
        (295, 425),
        (292, 410),
        (289, 395),
        (286, 382),
        (284, 368),
        (279, 346),
        (275, 337),
        (269, 317),
        (265, 308),
        (255, 292),
        (246, 279),
        (238, 272),
        (234, 265),
        (228, 259),
        (211, 255),
        (199, 254),
        (182, 254),
        (172, 254),
        (165, 256),
        (153, 261),
        (145, 267),
        (136, 277),
        (127, 289),
        (122, 301),
        (114, 315),
        (108, 326),
        (104, 336),
        (98, 349),
        (91, 365),
        (85, 372),
        (83, 373),
        (79, 371),
        (53, 355),
        (40, 341),
        (24, 330),
        (0, 324),
        (0, 560),
    ])



    surface = pygame.Surface([180, 240], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, MOUNT_FRONT, (0, 0, 180, 700))
    surface_rot = pygame.transform.rotate(surface, 5)
    screen.blit(surface_rot, (120, 251))

def draw_mount_back(screen):
    polygon(screen, MOUNT_BACK, [
        (16, 356),
        (22, 285),
        (27, 285),
        (44, 283),
        (56, 280),
        (68, 277),
        (94, 271),
        (114, 265),
        (131, 256),
        (146, 247),
        (161, 239),
        (175, 230),
        (188, 219),
        (204, 207),
        (221, 195),
        (233, 185),
        (244, 177),
        (252, 168),
        (264, 156),
        (270, 147),
        (327, 162),
        (341, 196),
        (462, 279),
        (587, 263),
        (665, 319),
        (740, 264),
        (800, 291),
        (885, 234),
        (897, 235),
        (929, 241),
        (949, 243),
        (979, 243),
        (998, 242),
        (1014, 240),
        (1028, 239),
        (1046, 232),
        (1062, 222),
        (1088, 205),
        (1108, 188),
        (1124, 170),
        (1138, 152),
        (1149, 131),
        (1164, 113),
        (1171, 108),
        (1186, 113),
        (1195, 123),
        (1196, 131),
        (1196, 144),
        (1287, 225),
        (1381, 189),
        (1436, 232),
        (1519, 193),
        (1600, 262),
    ])

def draw_menu(screen):
    
    for block in menus:
        block.draw(screen)

    # surface = pygame.Surface([100,100], pygame.SRCALPHA)
    # rect(surface, BG4, (0, 0, 100, 100))
    # rect(surface, MOUNT_FRONT_FIRST, (0, 0, 100, 100), 20)
    # circle(surface, MOUNT_FRONT, (50,50), 23, 5)
    # font = pygame.font.Font(None, 20)
    # text = font.render("draw circle", True, YELLOW)
    # place = text.get_rect(center=(280,90))
    # screen.blit(surface, (230,10))
    # screen.blit(text, place)

def write_circle(screen, start_pos, now_pos):
    a = abs(start_pos[0] - now_pos[0])
    b = abs(start_pos[1] - now_pos[1])
    diag = int(math.sqrt(a**2 + b **2))
    circle(screen, BG4, (start_pos[0], start_pos[1]), diag)
    pygame.display.update()



def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SIZE)

    # Drawing

    draw_background(screen)
    draw_sun(screen)
    draw_mount_back(screen)
    draw_mount_front(screen)
    draw_mount_front_first(screen)
    draw_menu(screen)

    # End Drawing

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    draw = False

    position_draw_circle = ()

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("({}, {}), ".format(event.pos[0], event.pos[1]))
                # draw = True
                # position_draw_circle = event.pos
                print("mouse down")
            if event.type == pygame.MOUSEMOTION and draw:
                # write_circle(screen, position_draw_circle, event.pos)
                print("mouse drawing")
            if event.type == pygame.MOUSEBUTTONUP:
                # for button in menus:
                #     button.clicked(event.pos[0], event.pos[1])
                draw = False
                print("mouse up")
    pygame.quit()
    pygame.font.quit()


if __name__ == "__main__":
    main()