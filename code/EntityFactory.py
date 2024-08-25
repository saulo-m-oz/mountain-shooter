#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT, LEVELS_BACKGROUND_COUNT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        if entity_name in LEVELS_BACKGROUND_COUNT:
            list_bg = []
            for i in range(LEVELS_BACKGROUND_COUNT[entity_name]):
                list_bg.append(Background(f'{entity_name}{i}', (0, 0)))
                list_bg.append(Background(f'{entity_name}{i}', (WIN_WIDTH, 0)))
            return list_bg
        else:
            match entity_name:
                case 'Player1':
                    return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
                case 'Player2':
                    return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
                case 'Enemy1':
                    return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
                case 'Enemy2':
                    return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
                case 'Enemy3':
                    return Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
