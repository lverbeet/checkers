from enum import Enum

# Enumeration objects
##PieceType:
class PieceType(Enum):
    SINGLE = 1
    DOUBLE = 2

##PieceColor:
class PieceColor(Enum):
    RED = 1
    WHITE = -1

##TileColor:
class TileColor(Enum):
    WHITE = 1
    BLACK = 2

##MoveType:
class MoveType(Enum):
    NONE = 0
    NORMAL = 1
    ATTACK = 2

# Classes
## Location: stores the x & y values that are the location coordinates within the GameBoard.Board[x][y]
## Is used by Piece & Tile class
class Location:
#
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x: int):
        self.__x = x

    def set_y(self, y: int):
        self.__y = y

##Piece:
class Piece:
# Constructor
    def __init__(self, color: PieceColor, location: Location):
        self.__color = color
        self.__location = location
        self.__type = PieceType.SINGLE
    # Get functions
    def get_color(self):
        return self.__color

    def get_location(self):
        return self.__location

    def get_type(self):
        return self.__type
    # Set functions
    ## Update new piece location to the object
    def set_new_location(self, new_location):
        self.__location = new_location
    ## Change
    def upgrade_piece(self):
        self.__type = PieceType.DOUBLE

##Tile:
class Tile:
    def __init__(self, color: TileColor, location: Location):
        self.__piece = None
        self.__color = color
        self.__location = location

    def get_color(self):
        return self.__color

    def get_location(self):
        return self.__location

    def get_piece(self) -> Piece:
        return self.__piece

    def get_has_piece(self) -> bool:
        if self.__piece is None:
            return False
        else:
            return True

    def remove_piece(self):
        self.__piece = None

    def place_piece(self, piece: Piece):
        self.__piece = piece

##Move:
class Move:
    def __init__(self, piece: Piece, move_type: MoveType, new_location: Location):
        self.__piece = piece
        self.__type = move_type
        self.__location = new_location

    def get_piece(self):
        return self.__piece

    def get_type(self):
        return self.__type

    def get_location(self):
        return self.__location

##Board:
class GameBoard:
    def __init__(self):
        self.__Board = []
        self.__length = 10
        self.__pieces = []

    def get_board(self):
        return self.__Board

    def get_pieces(self):
        return self.__pieces

    # fill_board():
    def fill_board(self):
        row = []
        for x in range(self.__length):
            for y in range(self.__length):
                color = None
                if (x + y) % 2 == 0:
                    color = TileColor.WHITE
                else:
                    color = TileColor.BLACK

                tile = Tile(color, Location(x, y))
                piece = None

                if x <= 3 and (x + y) % 2 != 0:
                    piece = Piece(PieceColor.RED, Location(x, y))

                if x >= 6 and (x + y) % 2 != 0:
                    piece = Piece(PieceColor.WHITE, Location(x, y))

                if piece is not None:
                    tile.place_piece(piece)
                    self.__pieces.append(piece)

                row.append(tile)

                if y == 9:
                    self.__Board.append(row)
                    row = []


