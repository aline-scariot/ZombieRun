#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pygame.image
from abc import ABC, abstractmethod
from code.Const import WIN_HEIGHT


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(os.path.join( './asset/' + name + '.png')).convert_alpha()
        self.rect = self.surf.get_rect(bottomleft=(0, 275))
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
    def update(self):
        self.move()
        
