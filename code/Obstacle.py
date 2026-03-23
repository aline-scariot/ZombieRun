#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from code.Const import ENT_SPEED, WIN_WIDTH


class Obstacle(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self, ):
        self.rect.centerx -= ENT_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass
