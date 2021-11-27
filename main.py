from pokemon import Pokemon
from move import Move
from pokemon_classes import Charmander
from trainer import Trainer
import pygame
import pygame_textinput
import pygame.locals

def main():
    """ Main function to run the game """

    # Initialize pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((1000, 1000))        

    # Player inputs their name
    backgroundSurface = pygame.Surface((50, 50))
    color = pygame.Color(255, 20, 10)
    arial = pygame.font.SysFont('arial', 24)



    # # New player
    # player = Trainer()



if __name__ == "__main__":
    main()
    char = Charmander("char", 39, 52, 43, 60, 50, 65, 'fire')


