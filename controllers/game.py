import pygame
import pygame.locals

from .name import NameController
from views import NameView
from views import PokemonSelectView

class Game():
    """ Main game controller """

    def __init__(self):
        """ Constructor - sets variables """
        self.name = ''

    def run(self, window):
        """ Runs the game """
        # Create the font
        font = pygame.font.Font('fonts\PKMN RBYGSC.ttf', 24)

        # Name view and controller are created - player enters their name and presses "enter"
        name_view = NameView(window, font)
        name_controller = NameController(name_view, window)
        name_controller.run()
        self.name = name_view.textinput.value
        print(self.name)

        # Pokemon list view and controller are created - player selects their pokemon team
        pokemon_select_view = PokemonSelectView(self.name, window)


        return True