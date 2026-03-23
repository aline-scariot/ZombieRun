#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, MENU_OPT, COLOR_BLACK, COLOR_GRAY
from pygame import Surface, Rect
from pygame.font import Font


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Bg1.png')
        self.rect = self.surf.get_rect(left=0, top=0)



    def run(self,):
        menu_opt = 0
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1) # loop play the music
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "Zombie Run", COLOR_WHITE, (WIN_WIDTH / 2, 140))

            for i in range(len(MENU_OPT)):
                if i == menu_opt:
                    self.menu_text(20, MENU_OPT[i], COLOR_GRAY, ((WIN_WIDTH / 2), 210 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPT[i], COLOR_BLACK, ((WIN_WIDTH / 2), 210 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit() #end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_opt < len(MENU_OPT) - 1:
                            menu_opt +=1
                        else:
                            menu_opt = 0
                    if event.key == pygame.K_UP:
                        if menu_opt > 0:
                            menu_opt -=1
                        else:
                            menu_opt = len(MENU_OPT) - 1
                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPT[menu_opt]


    def menu_text(self, text_size: int, text:str, text_color: tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name="Baron", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



