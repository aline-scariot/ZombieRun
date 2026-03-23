#C
import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (255, 233, 78)
COLOR_GRAY = (152, 173, 176)


#E
EVENT_OBSTACLE = pygame.USEREVENT + 1

ENT_SPEED={'Bg0': 0,
           'Bg1': 1,
           'Bg2': 2,
           'Bg3': 3,
           'Bg4': 4,
           'Obstacle0': 4,
           'Obstacle1': 2,
           'Obstacle2': 6,
           }

#M
MENU_OPT = ('NEW GAME',
            'EXIT')
#W
WIN_WIDTH = 576
WIN_HEIGHT = 324