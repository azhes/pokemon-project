import pygame
from models import Pokemon

class Bulbasaur(Pokemon):
    """ Represents a Bulbasaur. Inherits from Pokemon. """
    def __init__(self, nickname, hp=45, attack=49, defense=49, spattack=65, spdefense=65, speed=45, type1='Grass', type2='Poison', name='Bulbasaur'):
        super().__init__(nickname, hp, attack, defense, spattack, spdefense, speed, type1, type2=None)
        if name == nickname:
            self.nickname = name
        else:
            self.nickname = nickname
        self.front = pygame.image.load('sprites\\bulb_front.png')
        self.back = pygame.image.load('sprites\\bulb_back.png')