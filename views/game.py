import pygame

from .base import PygameView

class GameView(PygameView):
    """ Main view for the game """

    def draw(self):
        self.window.fill((255, 255, 255))
