import pygame
import pygame.locals
from views import PokemonSelectView
from .base import PygameController
from pokemon_classes import Charmander, Bulbasaur

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

        if event.type == pygame.locals.MOUSEBUTTONDOWN:
            if (
                event.pos[0] >= 30
                and event.pos[0] <= 330
                and event.pos[1] >= 200
                and event.pos[1] <= 300
            ):
                char = Charmander('Charmander')
                self.trainer.pokemon_list.append(char)
                return False
            elif (
                event.pos[0] >= 650
                and event.pos[0] <= 950
                and event.pos[1] >= 200
                and event.pos[1] <= 300
            ):
                bulb = Bulbasaur('Bulbasaur')
                self.trainer.pokemon_list.append(bulb)
                return False

        return True

