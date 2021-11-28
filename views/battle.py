import pygame
from .base import PygameView
from models import drawText

class BattleView(PygameView):
    """ Represents a battle between player and AI opponent. 
    Constructor takes a window, font, the player's pokemon, and the
    opponent's pokemon.
    """

    def __init__(self, window, font, trainer_pokemon, rival_pokemon):
        super().__init__(window)
        self.window = window
        self.font = font
        self.trainer_pokemon = trainer_pokemon
        self.rival_pokemon = rival_pokemon
        self.battle_surface = pygame.Surface((1000, 1000))

    def write_dialogue(self, text):
        """ Writes text into the dialogue box on the screen """
        drawText(self.battle_surface, text, (0, 0, 0), (50, 750, 400, 300), self.font)

    def clear_dialogue(self):
        """ Clears the dialogue box """
        pygame.draw.rect(self.battle_surface, (255, 255, 255, 255), (50, 750, 600, 100))

    def update_player_HP(self, value=0):
        """ Shows updated HP values for player's pokemon """
        max_hp = self.trainer_pokemon.hp
        hp_text = f'HP: {self.trainer_pokemon.hp - value}/{max_hp}'
        pygame.draw.rect(self.battle_surface, (255, 255, 255, 255), (20, 290, 200, 100))
        drawText(self.battle_surface, hp_text, (0, 0, 0), (20, 290, 200, 100), self.font)

    def update_opponent_HP(self, value=0):
        """ Shows updated HP values for opponent's pokemon """
        max_hp = self.rival_pokemon.hp
        hp_text = f'HP: {self.rival_pokemon.hp - value}/{max_hp}'
        pygame.draw.rect(self.battle_surface, (255, 255, 255, 255), (700, 450, 200, 100))
        drawText(self.battle_surface, hp_text, (0, 0, 0), (700, 450, 200, 100), self.font)


    def draw(self):
        self.window.fill((255, 255, 255))
        pygame.Surface.fill(self.battle_surface, (255, 255, 255))

        # Create a dialogue box
        dialgoue_box = pygame.image.load('sprites\dialogue_box.png')
        dialgoue_box = pygame.transform.scale(dialgoue_box, (700, 200))
        self.battle_surface.blit(dialgoue_box, (10, 700))

        # Show player's pokemon back sprite
        trainer_pokemon_sprite = self.trainer_pokemon.back
        trainer_pokemon_sprite = pygame.transform.scale(trainer_pokemon_sprite, (420, 420))
        self.battle_surface.blit(trainer_pokemon_sprite, (10, 330))

        # Show player's pokemon's nickname
        drawText(self.battle_surface, self.trainer_pokemon.nickname, (0, 0, 0), (20, 240, 300, 50), self.font)

        # Show opponent's pokemon front sprite
        rival_pokemon_sprite = self.rival_pokemon.front
        rival_pokemon_sprite = pygame.transform.scale(rival_pokemon_sprite, (320, 320))
        self.battle_surface.blit(rival_pokemon_sprite, (600, 100))

        # Show opponent's pokemon's nickname
        drawText(self.battle_surface, self.rival_pokemon.nickname, (0, 0, 0), (700, 400, 300, 50), self.font)        

        self.window.blit(self.battle_surface, (0, 0))
