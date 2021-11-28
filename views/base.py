from abc import ABC, abstractmethod

import pygame
import pygame.font

class PygameView(ABC):
    """ Abstract class for a basic Pygame view """

    def __init__(self, window):
        """ Constructor receives a window (where everything will be displayed) """
        self.window = window

    @abstractmethod
    def draw(self):
        """ Child classes must implement the draw method """
        raise NotImplementedError

    def update(self):
        """ Update the screen """
        pygame.display.flip()