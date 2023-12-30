from pieces.piece import Piece

class Queen(Piece):
    def __init__(self, x, y, player, board):
        super().__init__(x, y, player, board)
        self.type = 'queen'

    def showPossibleRoutes(self, checkingCheck):
        # queen movement is a combination between rook movement and bishop movement
        # the optimisation of their codes also helped optimising the queen's
        #same as rook algorythm
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
        #same as bishop algorithm
        obstacle = False
        for k in range(0, 4):
            a = self.x
            b = 0
            c = 1
            d = self.y
            e = 0
            f = 1
            if k == 0:
                b = -1
                c = -1
                e = -1
                f = -1
            elif k == 1:
                b = -1
                c = -1
                e = len(self.board.squares)
                f = 1
            elif k == 2:
                b = len(self.board.squares)
                c = 1
                e = -1
                f = -1
            elif k == 3:
                b = len(self.board.squares)
                c = 1
                e = len(self.board.squares)
                f = 1
            obstacle = False
            for i in range(a, b, c):
                for j in range(d, e, f):
                    if(i == self.x and j == self.y):
                        continue

                    x = abs(i - self.x)
                    y = abs(j - self.y)
                    cell = self.board.squares[i][j]
                    if(x == y and cell == None):
                        if not checkingCheck:
                            self.board.markSquare(i, j)
                    elif(x == y and isinstance(cell, Piece)):
                        obstacle = True
                        if cell.player.color != self.player.color:
                            if not checkingCheck:
                                cell.targeted = True
                            if cell.isKing():
                                if checkingCheck:
                                    return cell.player.color
                                else:
                                    self.board.kingUnderAttack = cell.player.color
                        break
                if(obstacle):
                    break