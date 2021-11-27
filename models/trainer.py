class Trainer:
    """ Represents a pokemon trainer, either the player, or the AI opponent """
    def __init__(self, name, pokemon_list):
        self.name = name
        self.pokemon_list = pokemon_list