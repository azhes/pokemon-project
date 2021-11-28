from controllers.pokemon_select import PokemonSelectController
import pygame
import pygame.locals

from views import PokemonSelectView
from models import Trainer

class Game():
    """ Main game controller """

    def __init__(self):
        """ Constructor - sets variables """
        pass

    def run(self, window):
        """ Runs the game """
        # Create the font
        font = pygame.font.Font('fonts\PKMN RBYGSC.ttf', 24)

        # Create a trainer instance
        trainer = Trainer()

        # Pokemon list view and controller are created - player selects their pokemon team
        pokemon_select_view = PokemonSelectView(window, font)
        pokemon_select_controller = PokemonSelectController(trainer, pokemon_select_view, window)
        pokemon_select_controller.run()

        return True