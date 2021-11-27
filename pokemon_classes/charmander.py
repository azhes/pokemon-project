from pokemon import Pokemon

class Charmander(Pokemon):
    """ Represents a Charmander. Inherits from Pokemon. """
    def __init__(self, nickname, hp, attack, defense, spattack, spdefense, speed, type1, type2=None, name='Charmander'):
        super().__init__(nickname, hp, attack, defense, spattack, spdefense, speed, type1, type2=None)
        if name == nickname:
            self.nickname = name
        else:
            self.nickname = nickname