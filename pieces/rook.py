from pieces.piece import Piece

class Rook(Piece):
    def __init__(self, x, y, player, board):
        super().__init__(x, y, player, board)
        self.type = 'rook'

    def showPossibleRoutes(self, checkingCheck):
        # rook can move in straight lines, four directions until a piece blocks its way
        # this code has been optimized as well same as bishop
        for k in range(0, 4):
            a = 0
            b = 0
            c = 0
            if k == 0:
                a = self.x
                b = -1
                c = -1
            elif k == 1:
                a = self.x
                b = len(self.board.squares)
                c = 1
            elif k == 2:
                a = self.y
                b = -1
                c = -1
            elif k == 3:
                a = self.y
                b = len(self.board.squares)
                c = 1

            for i in range(a, b, c):
                if k == 0 or k == 1:
                    j = self.y
                    if i == self.x:
                        continue
                    cell = self.board.squares[i][j]
                    if cell == None:
                        if not checkingCheck:
                            self.board.markSquare(i, j)
                    elif isinstance(cell, Piece):
                        if cell.player.color != self.player.color:
                            if not checkingCheck:
                                cell.targeted = True
                            if cell.isKing():
                                if checkingCheck:
                                    return cell.player.color
                                else:
                                    self.board.kingUnderAttack = cell.player.color
                        break
                else:
                    j = self.x
                    if i == self.y:
                        continue
                    cell = self.board.squares[j][i]
                    if cell == None:
                        if not checkingCheck:
                            self.board.markSquare(j, i)
                    elif isinstance(cell, Piece):
                        if cell.player.color != self.player.color:
                            if not checkingCheck:
                                cell.targeted = True
                            if cell.isKing():
                                if checkingCheck:
                                    return cell.player.color
                                else:
                                    self.board.kingUnderAttack = cell.player.color
                        break

