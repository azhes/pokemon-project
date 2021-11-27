import pygame
import pygame_textinput
from .base import PygameView
from models import drawText

class NameView(PygameView):
    """ Inherits from PygameView.
    Uses pygame_textinput to draw a text input space on the screen.
    The player enters their name. """

    def __init__(self, window, font):
        super().__init__(window)
        self.window = window
        self.font = font
        # Create TextInput object
        self.textinput = pygame_textinput.TextInputVisualizer(font_object=font)

    def draw(self):
        name_surface = pygame.Surface((1000, 1000))
        pygame.Surface.fill(name_surface, (255, 255, 255))

        events = pygame.event.get()
        self.textinput.update(events)   
        name_surface.blit(self.textinput.surface, (400, 400))

        self.window.blit(name_surface, (0, 0))
        drawText(self.window, f'Please enter your name and press Enter:', (0, 0, 0), (300, 300, 480, 200), self.font)

