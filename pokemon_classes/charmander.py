import pygame
from models import Pokemon

class Charmander(Pokemon):
    """ Represents a Charmander. Inherits from Pokemon. """
    def __init__(self, nickname, hp=39, attack=52, defense=43, spattack=60, spdefense=50, speed=65, type1='Fire', type2=None, name='Charmander'):
        super().__init__(nickname, hp, attack, defense, spattack, spdefense, speed, type1, type2=None)
        if name == nickname:
            self.nickname = name
        else:
            self.nickname = nickname
        self.front = pygame.image.load('sprites\char_front.png')
        self.back = pygame.image.load('sprites\char_back.png')