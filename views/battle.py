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
        pygame.draw.rect(self.battle_surface, (255, 255, 255, 255), (40, 750, 600, 100))

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

    def show_moves(self):
        """ Shows the player's pokemon's moves """
        moves_text = ''
        for index, move in enumerate(self.trainer_pokemon.moves_list):
            moves_text += f'{index + 1} {move.name}     '

        self.clear_dialogue()
        self.write_dialogue(moves_text)

    def show_attack(self, pokemon_nickname, move_name, effectiveness):
        """ Shows the move being used by the pokemon.
        Shows if the move is super effective (2) or not very effective (0.5). """
        attack_text = f'{pokemon_nickname} used {move_name}!'
        if effectiveness == 2:
            attack_text += f'It\'s super effective!'
        elif effectiveness == 0.5:
            attack_text += f'It\'s not very effective.'

        self.clear_dialogue()
        self.write_dialogue(attack_text)

    def show_faint(self, pokemon_nickname):
        """ Shows if the pokemon has fainted. """
        faint_text = f'{pokemon_nickname} fainted'

        self.clear_dialogue()
        self.write_dialogue(faint_text)

    def show_result(self, result):
        """ Shows if the player won or lost. """
        self.clear_dialogue()
        if result == 1:
            self.write_dialogue(f'You won!')
        elif result == 0:
            self.write_dialogue(f'You lost.')
        
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

        # Show player's pokemon's nickname and HP
        drawText(self.battle_surface, self.trainer_pokemon.nickname, (0, 0, 0), (20, 240, 300, 50), self.font)
        self.update_player_HP()

        # Show opponent's pokemon front sprite
        rival_pokemon_sprite = self.rival_pokemon.front
        rival_pokemon_sprite = pygame.transform.scale(rival_pokemon_sprite, (320, 320))
        self.battle_surface.blit(rival_pokemon_sprite, (600, 100))

        # Show opponent's pokemon's nickname
        drawText(self.battle_surface, self.rival_pokemon.nickname, (0, 0, 0), (700, 400, 300, 50), self.font) 
        self.update_opponent_HP()

        self.window.blit(self.battle_surface, (0, 0))
