
class Tile:
    """
    A class to represent a single tile in a puzzle.


    Attributes:
    id : integer
        a number representing the correct position of the puzzle

    position: integer
        a number representing the current position of a puzzle

    """
    def __init__(self,id,position):
        self.id=id
        self.position = position
    
    def get_position(self):
        return self.position

    def set_position(self,position):
        self.position = position