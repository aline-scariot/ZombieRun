#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Obstacle import Obstacle
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Bg{i}', (0,0)))
                    list_bg.append(Background(f'Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, 275))
            case 'Obstacle':
                list_obstacle = []
                for i in range(3):
                    list_obstacle.append(Obstacle(f'Obstacle{i}', (270 + i*25, 275)))
                return list_obstacle


            #case 'Obstacle':
            #   return Obstacle(f'Obstacle1', (290, 275))
            #case 'Obstacle':
            #   return Obstacle(f'Obstacle2', (300, 275))


