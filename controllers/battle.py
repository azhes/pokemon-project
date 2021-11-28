import pygame
import pygame.locals
import random
from views import BattleView
from .base import PygameController

class BattleController(PygameController):
    """ Controls a pokemon battle. 
    Constructor takes"""

    def __init__(self, view, window):
        super().__init__(view)
        self.window = window
        self.view = view

    def type_effectiveness(self, mv_type, def_type):
        """ Method for determining type effectiveness """
        effectiveness = {
            'fire': {
                'weakness': ['water'],
                'strength': ['grass', 'fire']
            },
            'water': {
                'weakness': ['grass', 'electric'],
                'strength': ['fire', 'water']
            },
            'grass': {
                'weakness': ['fire'],
                'strength': ['grass', 'electric', 'water']
            },
            'electric': {
                'weakness': [],
                'strength': ['water']
            }
        }

        if mv_type in effectiveness[def_type]['weakness']:
            multiplier = 2
        elif mv_type in effectiveness[def_type]['strength']:
            multiplier = 0.5
        else:
            multiplier = 1

        return multiplier

    def calculate_damage(self, attack, defense, power, atk_type, def_type, mv_type):
        """ Calculates damage """

        # 10% chance of a critical hit (double damage)
        critical_chance = random.randint(0, 9)
        if critical_chance == 9:
            critical = 2
        else: 
            critical = 1

        # determine type effectiveness
        effectiveness = self.type_effectiveness(mv_type, def_type)
        
        # STAB (Same Type Attack Bonus) If the pokemon's type is the same as the
        # type of the move it's using, then it deals 1.5x damage.
        if atk_type == mv_type:
            stab = 1.5
        else:
            stab = 1
        
        # calculate damage (adapted from https://bulbapedia.bulbagarden.net/wiki/Damage)
        damage = int((((((10 / 5) + 2) * power * (attack/defense))/50)+2) * stab * effectiveness * critical)

        return damage

    def process(self, event):
        running = super().process(event)

        if running is False:
            return False

        

        return True