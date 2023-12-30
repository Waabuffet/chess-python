from pieces.piece import Piece

class Knight(Piece):
    def __init__(self, x, y, player, board):
        super().__init__(x, y, player, board)
        self.type = 'knight'

    def showPossibleRoutes(self, checkingCheck):
        poss = [-2, -1, 1, 2]
        # when we think of the knight in chess, we picture its movement as L shaped, but to translate that into code
        # it's actually always a combination of 2 elements of the above list as long as they are not the same element (ex: -2 and -2 or -2 and 2)
        # and they are relative to the knight's coordinates
        for i in range(0, len(poss)):
            for j in range(0, len(poss)):
                if i == j or poss[i] + poss[j] == 0:
                    continue #skip illegal movements

                x = self.x + poss[i]
                y = self.y + poss[j]

                if x > -1 and x < len(self.board.squares) and y > -1 and y < len(self.board.squares):
                    cell = self.board.squares[x][y]
                    if cell == None:
                        if not checkingCheck:
                            self.board.markSquare(x, y)
                    elif isinstance(cell, Piece):
                        if cell.player.color != self.player.color:
                            if not checkingCheck:
                                cell.targeted = True
                            if cell.isKing():
                                if checkingCheck:
                                    return cell.player.color
                                else:
                                    self.board.kingUnderAttack = cell.player.color

                

# legal combination for knight movement:
# -2 -1
# -2 +1
# -1 -2
# -1 +2
# +1 -2
# +1 +2
# +2 -1
# +2 +1

# illegal combinations:
# -2 -2
# -2 2
# -1 -1
# -1 1
# 1 1
# 2 2