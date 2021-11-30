import pygame
from models import Pokemon

class Gengar(Pokemon):
    """ Represents a Charmander. Inherits from Pokemon. """
    def __init__(self, nickname, hp=60, attack=65, defense=60, spattack=130, spdefense=75, speed=110, type1='ghost', type2='poison', species='Gengar'):
        super().__init__(nickname, hp, attack, defense, spattack, spdefense, speed, type1, type2=None)
        if species == nickname:
            self.nickname = species
        else:
            self.nickname = nickname
        self.species = species
        self.front = pygame.image.load('sprites\geng_front.png')
        self.back = pygame.image.load('sprites\geng_back.png')