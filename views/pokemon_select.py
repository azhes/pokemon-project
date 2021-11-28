import pygame
from .base import PygameView
from models import drawText

class PokemonSelectView(PygameView):
    """ Shows the player a list of available pokemon.
    The player selects up to 3 pokemon for their team.
    draw() method displays sprites of the available pokemon and a
    selection box next to each. """

    def __init__(self, window, font):
        super().__init__(window)
        self.window = window
        self.font = font

    def draw(self):
        pokemon_surface = pygame.Surface((1000, 1000))
        pygame.Surface.fill(pokemon_surface, (255, 255, 255))

        drawText(pokemon_surface, f'Choose your pokemon:', (0, 0, 0), (300, 50, 400, 200), self.font)

        char_sprite = pygame.image.load('sprites\char_front.png')
        char_sprite = pygame.transform.scale(char_sprite, (120, 120))
        pokemon_surface.blit(char_sprite, (325, 200))
        char_select = pygame.draw.rect(pokemon_surface, (200, 50, 20), (30, 200, 300, 100))
        char_text = f'Charmander'
        drawText(pokemon_surface, char_text, (0, 0, 0), (65, 230, 200, 100), self.font)

        bulb_sprite = pygame.image.load('sprites\\bulb_front.png')
        bulb_sprite = pygame.transform.scale(bulb_sprite, (120, 120))
        pokemon_surface.blit(bulb_sprite, (550, 200))
        bulb_select = pygame.draw.rect(pokemon_surface, (20, 200, 50), (650, 200, 300, 100))
        bulb_text = f'Bulbasaur'
        drawText(pokemon_surface, bulb_text, (0, 0, 0), (700, 230, 200, 100), self.font)

        squirt_sprite = pygame.image.load('sprites\squirt_front.png')
        squirt_sprite = pygame.transform.scale(squirt_sprite, (120, 120))
        pokemon_surface.blit(squirt_sprite, (325, 400))
        squirt_select = pygame.draw.rect(pokemon_surface, (20, 50, 200), (30, 400, 300, 100))
        squirt_text = f'Squirtle'
        drawText(pokemon_surface, squirt_text, (0, 0, 0), (85, 430, 200, 100), self.font)

        pika_sprite = pygame.image.load('sprites\pika_front.png')
        pika_sprite = pygame.transform.scale(pika_sprite, (120, 120))
        pokemon_surface.blit(pika_sprite, (540, 400))
        pika_select = pygame.draw.rect(pokemon_surface, (232, 240, 0), (650, 400, 300, 100))
        pika_text = f'Pikachu'
        drawText(pokemon_surface, pika_text, (0, 0, 0), (720, 430, 200, 100), self.font)

        self.window.blit(pokemon_surface, (0, 0))

