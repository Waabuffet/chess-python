from pieces.piece import Piece
from pieces.rook import Rook

class King(Piece):
    def __init__(self, x, y, player, board):
        super().__init__(x, y, player, board)
        self.type = 'king'
        self.castling_up = None
        self.castling_down = None

    def showPossibleRoutes(self, checkingCheck):
        #king can move one cell in any direction as long as it has no piece of same color (or of course is outside the edge of the board)
        # if cell has piece of opposing color, it is targeted
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if(i >= 0 and i < len(self.board.squares) and j >= 0 and j < len(self.board.squares)):
                    if(i == self.x and j == self.y):
                        continue
                    cell = self.board.squares[i][j]
                    if(cell == None):
                        if not checkingCheck:
                            self.board.markSquare(i, j)
                    elif isinstance(cell, Piece):
                        if cell.player.color != self.player.color:
                            cell.targeted = True
                            if cell.isKing():
                                if checkingCheck:
                                    return cell.player.color
                                else:
                                    self.board.kingUnderAttack = cell.player.color
    
        #this part will check if castling is allowed (switching king adn rook)
        if self.moves == 0:
            # for i in range(0, 8, 7): #will iterate twice, i = 0, i = 7
                rook_up = self.board.squares[self.x][0]
                rook_down = self.board.squares[self.x][7]
                if isinstance(rook_up, Rook):
                    if rook_up.moves == 0:
                        can_move = True
                        for j in range(rook_up.y + 1, self.y):
                            if isinstance(self.board.squares[self.x][j], Piece):
                                can_move = False
                                break
                        if can_move:
                            self.castling_up = (self.x, 2)
                            self.board.markSquare(self.x, 2)
                
                if isinstance(rook_down, Rook):
                    if rook_down.moves == 0:
                        can_move = True
                        for j in range(self.y + 1, rook_down.y):
                            if isinstance(self.board.squares[self.x][j], Piece):
                                can_move = False
                                break
                        if can_move:
                            self.castling_down = (self.x, 6)
                            self.board.markSquare(self.x, 6)

    def isKing(self):
        return True