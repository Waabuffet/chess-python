from pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, x, y, player, board):
        super().__init__(x, y, player, board)
        self.type = 'bishop'

    def showPossibleRoutes(self, checkingCheck):
        self.board.hideMarks()
        obstacle = False

        #replaced commented code (8 loops into 3 loops)
        # bishop can only move diagonally, so to check if the cell is a legal movement
        # we need to check if the abs(new_cell_x - bishop_cell_x) == abs(new_cell_y - bishop_cell_y)
        # keep in mind if cell has a piece its rroute is cut off
        # if cell has piece of opposing color, it will be targeted
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

        # for i in range(self.x, -1, -1):
        #     for j in range(self.y, -1, -1):
        #         if(i == self.x and j == self.y):
        #             continue

        #         x = abs(i - self.x)
        #         y = abs(j - self.y)
        #         if(x == y and self.board.squares[i][j] == None):
        #             self.board.markSquare(i, j)
        #         elif(x == y and self.board.squares[i][j] != None):
        #             obstacle = True
        #             break
        #     if(obstacle):
        #         break

        # obstacle = False
        # for i in range(self.x, -1, -1):
        #     for j in range(self.y, 8):
        #         if(i == self.x and j == self.y):
        #             continue

        #         x = abs(i - self.x)
        #         y = abs(j - self.y)
        #         if(x == y and self.board.squares[i][j] == None):
        #             self.board.markSquare(i, j)
        #         elif(x == y and self.board.squares[i][j] != None):
        #             obstacle = True
        #             break
        #     if(obstacle):
        #         break
        
        # obstacle = False
        # for i in range(self.x, 8):
        #     for j in range(self.y, -1, -1):
        #         if(i == self.x and j == self.y):
        #             continue

        #         x = abs(i - self.x)
        #         y = abs(j - self.y)
        #         if(x == y and self.board.squares[i][j] == None):
        #             self.board.markSquare(i, j)
        #         elif(x == y and self.board.squares[i][j] != None):
        #             obstacle = True
        #             break
        #     if(obstacle):
        #         break

        # obstacle = False
        # for i in range(self.x, 8):
        #     for j in range(self.y, 8):
        #         if(i == self.x and j == self.y):
        #             continue

        #         x = abs(i - self.x)
        #         y = abs(j - self.y)
        #         if(x == y and self.board.squares[i][j] == None):
        #             self.board.markSquare(i, j)
        #         elif(x == y and self.board.squares[i][j] != None):
        #             obstacle = True
        #             break
        #     if(obstacle):
        #         break