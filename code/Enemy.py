#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = 1
        self._speed_multiplier = 1

    @property
    def speed_multiplier(self):
        return 2 if self.direction == 1 and self.name == 'Enemy3' else 1

    def move(self):
        speed = ENTITY_SPEED[self.name]
        self.rect.centerx -= speed

        if self.name == 'Enemy3':
            if self.rect.bottom >= WIN_HEIGHT:
                self.direction = -1
            elif self.rect.top <= 0:
                self.direction = 1

            self.rect.y += speed * self.direction * self.speed_multiplier



    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
