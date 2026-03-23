#C
import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (255, 233, 78)
COLOR_GRAY = (152, 173, 176)


#E
EVENT_OBSTACLE = pygame.USEREVENT + 1

ENT_HEALTH = {
    'Player': 100,
    'Obstacle0': 1000,
    'Obstacle1': 1000,
    'Obstacle2': 1000,
    'Bg0': 1000,
    'Bg1': 1000,
    'Bg2': 1000,
    'Bg3': 1000,
    'Bg4': 1000,
}

ENT_DAMAGE = { 'Player': 1,
        'Obstacle0': 1,
        'Obstacle1': 1,
        'Obstacle2': 1,
        'Bg0': 0,
        'Bg1': 0,
        'Bg2': 0,
        'Bg3': 0,
        'Bg4': 0,
         }

ENT_SPEED = {'Bg0': 0,
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