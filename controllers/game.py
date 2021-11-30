import pygame
import pygame.locals
import random

from views import PokemonSelectView, BattleView
from models import Trainer
from pokemon_classes import Charmander, Bulbasaur, Squirtle, Pikachu
from .pokemon_select import PokemonSelectController
from .battle import BattleController

class Game:
    """ Main game controller """

    def __init__(self):
        """ Constructor - sets variables """
        pass

    def add_moves(self, pokemon_list):
        """ Adds moves to pokemon based on the species """
        trainer_pokemon = pokemon_list[0]
        if trainer_pokemon.species == "Charmander":
            trainer_pokemon.add_move("Scratch")
            trainer_pokemon.add_move("Ember")
        if trainer_pokemon.species == "Bulbasaur":
            trainer_pokemon.add_move("Tackle")
            trainer_pokemon.add_move("Vine Whip")
        if trainer_pokemon.species == "Squirtle":
            trainer_pokemon.add_move("Tackle")
            trainer_pokemon.add_move("Water Gun")
        if trainer_pokemon.species == "Pikachu":
            trainer_pokemon.add_move("Thunder Shock")
            trainer_pokemon.add_move("Quick Attack")
        if trainer_pokemon.species == "Gengar":
            trainer_pokemon.add_move("Shadow Ball")
            trainer_pokemon.add_move("Sludge Bomb")

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
        
        # Add moves to the player's pokemon
        self.add_moves(trainer.pokemon_list)

        trainer_pokemon = trainer.pokemon_list[0]

        # Create opponent trainer instance
        rival = Trainer()

        # Give opponent a random pokemon
        opponent_pokemon = [Charmander('Burny'), Bulbasaur('Leafy'), Squirtle('Shelly'), Pikachu('Zappy')]
        rival.pokemon_list.append(random.choice(opponent_pokemon))
        rival_pokemon = rival.pokemon_list[0]

        # Add moves to opponent's pokemon
        self.add_moves(rival.pokemon_list)

        # Create battle view and controller - run battle
        battle_view = BattleView(window, font, trainer_pokemon, rival_pokemon)
        battle_controller = BattleController(battle_view, window, trainer_pokemon, rival_pokemon)
        battle_controller.run()