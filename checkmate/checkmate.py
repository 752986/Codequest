import sys

class Piece:`q`
    color: bool # black is false, white is true

class Pawn:
    pass

class Rook:
    pass

class Bishop:
    pass

class Knight:
    pass

class Queen:
    pass

class King:
    pass


SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for case_num in range(cases):
    board: list[list[Piece]]
    for i in range(8):
        line = sys.stdin.readline().rstrip()
        for char in line:
            piece: Piece

            if char == 'p':
                

            
