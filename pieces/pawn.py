from pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, x, y, player, board):
        super().__init__(x, y, player, board)
        self.type = 'pawn'

    def showPossibleRoutes(self, checkingCheck):
        #pawn movement is based on his color (white can only move left, black only right)
        #pawn can only attack diagonally, and only one step. this is the only case it can move diagonally
        # otherwise, it will move only 1 step forward
        # moreover, if pawn didn't move yet, it can move 2 steps forward once 
        if self.player.color == 'black':
            if self.x + 1 < len(self.board.squares) and self.board.squares[self.x + 1][self.y] == None:
                if not checkingCheck:
                    self.board.markSquare(self.x + 1, self.y)
                if self.moves == 0 and self.x + 2 < len(self.board.squares) and self.board.squares[self.x + 2][self.y] == None:
                    if not checkingCheck:
                        self.board.markSquare(self.x + 2, self.y)
                if self.y + 1 < len(self.board.squares):
                    cell = self.board.squares[self.x + 1][self.y + 1]
                    if cell != None:
                        if isinstance(cell, Piece):
                            if cell.player.color != self.player.color:
                                cell.targeted = True
                                if cell.isKing():
                                    if checkingCheck:
                                        return cell.player.color
                                    else:
                                        self.board.kingUnderAttack = cell.player.color
                if self.y - 1 > -1:
                    cell = self.board.squares[self.x + 1][self.y - 1]
                    if cell != None:
                        if isinstance(cell, Piece):
                            if cell.player.color != self.player.color:
                                cell.targeted = True
                                if cell.isKing():
                                    if checkingCheck:
                                        return cell.player.color
                                    else:
                                        self.board.kingUnderAttack = cell.player.color
        else:
            if self.x - 1 > -1 and self.board.squares[self.x - 1][self.y] == None:
                if not checkingCheck:
                    self.board.markSquare(self.x - 1, self.y)
                if self.moves == 0 and self.x - 2 > -1 and self.board.squares[self.x - 2][self.y] == None:
                    if not checkingCheck:
                        self.board.markSquare(self.x - 2, self.y)
                if self.y + 1 < len(self.board.squares):
                    cell = self.board.squares[self.x - 1][self.y + 1]
                    if cell != None:
                        if isinstance(cell, Piece):
                            if cell.player.color != self.player.color:
                                cell.targeted = True
                                if cell.isKing():
                                    if checkingCheck:
                                        return cell.player.color
                                    else:    
                                        self.board.kingUnderAttack = cell.player.color
                if self.y - 1 > -1:
                    cell = self.board.squares[self.x - 1][self.y - 1]
                    if cell != None:
                        if isinstance(cell, Piece):
                            if cell.player.color != self.player.color:
                                cell.targeted = True
                                if cell.isKing():
                                    if checkingCheck:
                                        return cell.player.color
                                    else:
                                        self.board.kingUnderAttack = cell.player.color
    
    def isPawn(self):
        return True