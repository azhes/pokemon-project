import pygame
import pygame.locals
import pygame.font
from views import GameView
from controllers import Game

def main():
    """ Main function to run the game """

    # Initialize pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((1000, 1000))

    # Create the game view and controller
    game = Game()

    # Run the game
    game.run(window)



if __name__ == "__main__":
    main()


