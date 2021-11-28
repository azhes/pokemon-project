import pygame
from views import PokemonSelectView
from .base import PygameController

class PokemonSelectController(PygameController):
    """ When the player click on a button next to a pokemon, it adds
    that pokemon to the player's team. Buttons disappear and new button
    appears asking player if they want to start the battle. """

    def __init__(self, trainer, view, window):
        super().__init__(view)
        self.trainer = trainer
        self.window = window
        self.view = view

    def process(self, event):
        running = super().process(event)

        if running is False:
            return False

        return True

