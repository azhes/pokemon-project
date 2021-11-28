import pygame
from models import Pokemon

class Squirtle(Pokemon):
    """ Represents a Squirtle. Inherits from Pokemon. """
    def __init__(self, nickname, hp=44, attack=48, defense=65, spattack=50, spdefense=64, speed=43, type1='water', type2=None, species='Squirtle'):
        super().__init__(nickname, hp, attack, defense, spattack, spdefense, speed, type1, type2=None)
        if species == nickname:
            self.nickname = species
        else:
            self.nickname = nickname
        self.species = species
        self.front = pygame.image.load('sprites\squirt_front.png')
        self.back = pygame.image.load('sprites\squirt_back.png')