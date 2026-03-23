    #!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(700, 520))

    def run(self, ):
        pass

        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()
            #        quit() #end pygame

