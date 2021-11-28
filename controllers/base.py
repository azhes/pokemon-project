from abc import ABC, abstractmethod

import pygame
import pygame.locals

class PygameController(ABC):
    """ This class defines a private method.
    
    The controllers inherit from this class, which allows them to run
    a Pygame loop by just calling predefined methods.
    
    """

    FPS = 60

    def __init__(self, view):
        """ The controller receives a view when instantiated. """
        self.view = view

    def run(self):
        """
        Main method: runs a Pygame loop and passes the event to self.process
         to return anything else than True to stop the loop.
         
        The optional argument 'stop_after' is the maximum amount of time to
        run the Pygame event loop (in seconds). """

        running = True
        start = pygame.time.get_ticks()
        clock = pygame.time.Clock()
        while running is True:
            clock.tick(self.FPS)
            self.view.draw()
            self.view.update()
            for event in pygame.event.get():
                running = self.process(event)
                if running is False:
                    break
            now = pygame.time.get_ticks()

    def process(self, event):
        """ Abstract method: should be implemented by child classes """
        # Invoked close from the OS
        if event.type == pygame.locals.QUIT:
            pygame.quit()
        # Pressed a key - is it Escape?
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                return False

        return True
