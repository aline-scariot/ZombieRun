#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import event

import pygame.key
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_force = -10
        self.on_ground = False

    def move(self ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_SPACE] and self.on_ground: # Jump
            self.velocity_y = self.jump_force
            self.on_ground = False

        self.velocity_y += self.gravity # Gravity
        self.rect.y += self.velocity_y

        floor = 265
        if self.rect.bottom >= floor: #floor limited
            self.rect.bottom = floor
            self.velocity_y = 0
            self.on_ground = True
        pass
