import pygame
import pygame.locals
import pygame_textinput
from .base import PygameController

class NameController(PygameController):
    def __init__(self, view, window):
        self.view = view
        self.window = window

    def process(self, event):
        running = super().process(event)

        if running is False:
            return False

        if event.type == pygame.locals.KEYDOWN:
            key_pressed = pygame.key.name(event.key)
            if key_pressed == 'enter':
                return False

        return True

        
