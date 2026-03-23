#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame.display
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_BLACK, COLOR_WHITE, EVENT_OBSTACLE
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 30000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.entity_list.extend(EntityFactory.get_entity('Obstacle'))
        pygame.time.set_timer(EVENT_OBSTACLE, 20000)


    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(40)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # end pygame
                if event.type == EVENT_OBSTACLE:
                    choice = random.choice(('Obstacle0', 'Obstacle1', 'Obstacle2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))


            self.level_text(15, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_BLACK, (470, 10))
            self.level_text(15, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (470, 300))
            self.level_text(14, f'Entity: {len(self.entity_list)}', COLOR_WHITE, (470, 280))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text:str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Baron", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
        

