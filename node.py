from enum import Enum

class Rarity(Enum):
    BLANK = 0,
    COMMON = 1,
    MAGIC = 2,
    RARE = 3,
    LEGENDARY = 4,
    GLYPH = 5

class ParagonNode(object):
    def __init__(self, parameters=None, rarity:Rarity=None):
        self.blank = True if (parameters is None and rarity is None) else False
        self.parameters = parameters
        self.explored = False
        self.marked = False
        self.parent = None  # Use for breadth-first search
        self.rarity:Rarity = Rarity.BLANK if rarity is None else rarity

    def setNode(self, parameters):
        if parameters is not None:
            self.blank = False
        self.parameters = parameters

    def __str__(self):
        if self.marked:
            return 'X'
        if self.rarity == Rarity.GLYPH:
            return 'g'
        elif self.rarity == Rarity.LEGENDARY:
            return 'l'
        elif self.rarity == Rarity.RARE:
            return 'r'
        elif self.rarity == Rarity.MAGIC:
            return 'm'
        elif self.rarity == Rarity.COMMON:
            return 'c'
        elif self.rarity == Rarity.BLANK:
            return 'b'
        if self.blank:
            return " "
        return "_"
