import pygame
from models import Pokemon

class Pikachu(Pokemon):
    """ Represents a Pikachu. Inherits from Pokemon. """
    def __init__(self, nickname, hp=35, attack=55, defense=30, spattack=50, spdefense=40, speed=90, type1='electric', type2=None, species='Pikachu'):
        super().__init__(nickname, hp, attack, defense, spattack, spdefense, speed, type1, type2=None)
        if species == nickname:
            self.nickname = species
        else:
            self.nickname = nickname
        self.species = species
        self.front = pygame.image.load('sprites\pika_front.png')
        self.back = pygame.image.load('sprites\pika_back.png')