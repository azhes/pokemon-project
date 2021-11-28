import pygame
from models import Pokemon

class Squirtle(Pokemon):
    """ Represents a Squirtle. Inherits from Pokemon. """
    def __init__(self, nickname, hp=44, attack=48, defense=65, spattack=50, spdefense=64, speed=43, type1='Water', type2=None, name='Squirtle'):
        super().__init__(nickname, hp, attack, defense, spattack, spdefense, speed, type1, type2=None)
        if name == nickname:
            self.nickname = name
        else:
            self.nickname = nickname
        self.front = pygame.image.load('sprites\squirt_front.png')
        self.back = pygame.image.load('sprites\squirt_back.png')