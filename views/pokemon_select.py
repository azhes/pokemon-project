import pygame
from .base import PygameView
from models import drawText

class PokemonSelectView(PygameView):
    """ Shows the player a list of available pokemon.
    The player selects up to 3 pokemon for their team.
    draw() method displays sprites of the available pokemon and a
    selection box next to each. """

    def __init__(self, name, window):
        super().__init__(window)
        self.window = window
        self.name = name

    def draw(self):
        pokemon_surface = pygame.Surface((1000, 1000))
        pygame.Surface.fill(pokemon_surface, (255, 255, 255))

        self.window.blit(pokemon_surface, (0, 0))

