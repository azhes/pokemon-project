class Move():
    """ Represents a Move. """
    def __init__(self, name, pp, power, accuracy, type):
        """ All moves have power points (pp), power, accuracy, and a type """
        self.name = name
        self._pp = pp
        self.power = power
        self.accuracy = accuracy
        self.type = type

    @property
    def pp(self):
        """ Getter for pp """
        return self._pp

    @pp.setter
    def pp(self, value):
        """ Setter for pp """
        self._pp -= value