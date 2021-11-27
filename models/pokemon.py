from abc import abstractmethod, ABC
from move import Move
import json

class Pokemon(ABC):
    """ Abstract class that represents a pokemon """
    def __init__(self, nickname, hp, attack, defense, spattack, spdefense, speed, type1, type2=None):
        """ All pokemon have HP, Attack, Defense, Special Attack,
        Special Defense, Speed """
        self._nickname = nickname
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._spattack = spattack
        self._spdefense = spdefense
        self._speed = speed
        self.type1 = type1
        self.type2 = type2
        self.moves_list = []

    @property
    def nickname(self):
        """ Getter for nickname """
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        """ Setter for nickname """
        self._nickname = value

    @property
    def hp(self):
        """ Getter for HP """
        return self._hp

    @hp.setter
    def hp(self, value):
        """ Setter for HP """
        self._hp = value

    @property
    def attack(self):
        """ Getter for Attack """
        return self._attack

    @property
    def defense(self):
        """ Getter for Defense """
        return self._defense

    @property
    def spattack(self):
        """ Getter for Special Attack """
        return self._spattack

    @property
    def spdefense(self):
        """ Getter for Special Defense """
        return self._spdefense

    @property
    def speed(self):
        """ Getter for Speed """
        return self._speed

    def add_move(self, move_name):
        """ Adds a move to the pokemon's move list.
        Reads the moves.json file and creates move instances. """
        with open('moves.json') as f:
            data = json.load(f)
        for move in data:
            if move_name == move['name']:
                createdMove = Move(move['name'], move['pp'], move['power'], move['accuracy'], move['type'])
                self.moves_list.append(createdMove)

    def view_moves(self):
        """ Views the moves for that pokemon """
        for move in self.moves_list:
            print(move.name)

    def take_damage(self, value):
        """ Method that is called when the pokemon takes damage """
        self.hp = self.hp - value

    def heal(self, value):
        """ Method that is called when the pokemon heals damage """
        self.hp = self.hp + value