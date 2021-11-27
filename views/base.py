from abc import ABC, abstractmethod

import pygame
import pygame.font

class PygameView(ABC):
    """ Abstract class for a basic Pygame view """

    def __init__(self, window):
        """ Constructor receives a window (where everything will be displayed) """
        self.window = window

    def render_text_surface(self, text):
        """ Utility function to render a text surface """
        rby = pygame.font.Font('../fonts/PKMN RBYGSC.ttf', 24)
        text_surface = rby.render(text, True, (0, 0, 0))

        return text_surface

    @abstractmethod
    def draw(self):
        """ Child classes must implement the draw method """
        raise NotImplementedError

    def update(self):
        """ Update the screen """
        pygame.display.flip()