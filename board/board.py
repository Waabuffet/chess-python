from pieces.piece import Piece
from pieces.queen import Queen
import math

class Board:
    def __init__(self, player1, player2, boardLength, size, font):
        self.squares = []
        self.squaresNum = 8
        self.markedSymbol = 'X'
        self.markedRadius = 10
        self.selectedPiece = None
        self.player1 = player1
        self.player2 = player2
        self.playerTurn = self.player1
        self.kingUnderAttack = None
        self.king = None
        self.pieceMoving = None
        self.animation_speed = 3
        self.moving_piece_pos = None
        self.size = size

        self.change_text = False

        self.TEXT_FONT = font
        self.text_message = 'Game started'
        
        #initialize emtpy cells
        for i in range(0, boardLength):
            sub = []
            for j in range(0, boardLength):
                sub.append(None)
            self.squares.append(sub)
    
    #function that shows the board, cells, pieces and possible moving routes
    def show(self, pygame, screen):
        cnt = 0
        white, black, red, blue = (255,255,255), (218,202,98), (255,0,0), (0,0,255)

        if self.change_text:
            screen.fill(white)
            self.change_text = False
        
        for i in range(0, len(self.squares)):
            for j in range(0, len(self.squares[i])):
                #print board cells
                if cnt%2 == 0:
                    pygame.draw.rect(screen, white, [self.size * i, self.size * j, self.size, self.size])
                else:
                    pygame.draw.rect(screen, black, [self.size * i, self.size * j, self.size, self.size])
                
                if self.squares[i][j] != None:
                    cell = self.squares[i][j]
                    if isinstance(cell, Piece): #print pieces images
                        if cell.targeted: #print red cell
                            pygame.draw.rect(screen, red, [self.size * i, self.size * j, self.size, self.size])
                        if cell.isKing() and self.kingUnderAttack != None: #print blue cell
                            if cell.player.color == self.kingUnderAttack:
                                pygame.draw.rect(screen, blue, [self.size * i, self.size * j, self.size, self.size])
                        pieceImage = pygame.image.load(self.squares[i][j].image)
                        pieceImage = pygame.transform.scale(pieceImage, (self.size // 2, self.size // 2))
                        
                        if self.pieceMoving != cell: #attempt for animation
                            screen.blit(pieceImage, [self.size * i + self.size // 4, self.size * j + self.size // 4])
                        else: #animate piece movement
                            x_dest = cell.getX() * self.size + self.size // 4
                            y_dest = cell.getY() * self.size + self.size // 4
                            if x_dest != self.moving_piece_pos[0] and y_dest != self.moving_piece_pos[1]:
                                new_x = self.moving_piece_pos[0] + (math.copysign(1, x_dest - self.moving_piece_pos[0]) * self.animation_speed)
                                new_y = self.moving_piece_pos[1] + (math.copysign(1, y_dest - self.moving_piece_pos[1]) * self.animation_speed)
                                self.moving_piece_pos = (new_x, new_y)
                                screen.blit(pieceImage, [new_x, new_y])
                                if abs(x_dest - self.moving_piece_pos[0]) < self.animation_speed and abs(y_dest - self.moving_piece_pos[1]) < self.animation_speed:
                                    self.pieceMoving = None
                                    self.moving_piece_pos = None
                            else:
                                self.pieceMoving = None
                                self.moving_piece_pos = None

                    elif cell == self.markedSymbol: #showing cell possible movement routes
                        pygame.draw.circle(screen, red, [self.size * i + self.size // 2, self.size * j + self.size // 2], self.markedRadius)
                cnt += 1
            cnt -= 1 #this is used to make each cell a different color on different rows

        #text area
        board_length = self.size * len(self.squares)
        text_x = board_length // 2 - 50
        text_y = board_length + 10
        textsurface = self.TEXT_FONT.render(self.text_message, False, (0, 0, 0))
        screen.blit(textsurface,(text_x,text_y))

    #show message when turn changes, when check and when checkmate
    def setMessage(self, message):
        self.text_message = message
        self.change_text = True
    
    #did not work properly
    def animatePieceMovement(self, piece, oldX, oldY):
        self.pieceMoving = piece
        x_coord = oldX * self.size + self.size // 4
        y_coord = oldY * self.size + self.size // 4
        self.moving_piece_pos = (x_coord, y_coord)

    #on new game when adding pieces to the board
    def addPiece(self, piece, x, y):
        self.squares[x][y] = piece
        if piece.isKing():
            self.king = piece
    
    #show possible moving routes for a specific piece
    def markSquare(self, x, y):
        if(self.squares[x][y] == None):
            self.squares[x][y] = self.markedSymbol

    #switch player turns
    def switchTurns(self):
        if self.playerTurn == self.player1:
            self.playerTurn = self.player2
        else:
            self.playerTurn = self.player1
        self.setMessage(self.playerTurn.color + ' turn')
    
    #move piece on the board, this method checks if king is under check and prevents player from moving if so
    #also it check if game has ended (checkmate)
    def movePiece(self, piece, x, y):
        oldX = piece.getX()
        oldY = piece.getY() 
        piece.setX(x)
        piece.setY(y)
        piece.moves += 1
        self.squares[x][y] = piece
        self.squares[oldX][oldY] = None

        #check if pawn reached the end so turn it into queen before checking check
        if piece.isPawn():
            if (piece.player.color == 'white' and piece.x == 0) or (piece.player.color == 'black' and piece.x == 7):
                self.squares[piece.x][piece.y] = Queen(piece.x, piece.y, piece.player, self)
                color = piece.player.color[0].upper()
                self.squares[piece.x][piece.y].setImage('./assets/Queen ' + color + '.png')               

        #cehck if king is checked
        theKingChecked = self.kingChecked(piece.player.color)
        can_move = False
        if theKingChecked != None:
            if theKingChecked == piece.player.color: #if king of player color is checked, its an illegal move and piece is put back where it was
                piece.setX(oldX)
                piece.setY(oldY)
                piece.moves -= 1
                self.squares[x][y] = None
                self.squares[oldX][oldY] = piece
                self.kingUnderAttack = theKingChecked
                self.setMessage('illegal move')
            else:
                self.kingUnderAttack = theKingChecked
                can_move = True
        else:
            self.kingUnderAttack = None
            can_move = True
            
            #casttling (switching king and rook)
            if piece.isKing(): #castling only allowed if not checked
                if piece.castling_up != None:
                    if piece.castling_up[0] == x and piece.castling_up[1] == y:
                        self.movePiece(self.squares[piece.x][0], piece.x, 3)
                        piece.castling_up = None
                        self.switchTurns()
                if piece.castling_down != None:
                    if piece.castling_down[0] == x and piece.castling_down[1] == y:
                        self.movePiece(self.squares[piece.x][7], piece.x, 5)
                        piece.castling_down = None
                        self.switchTurns()
        
        if can_move:
            self.switchTurns()
            self.animatePieceMovement(piece, oldX, oldY)
        
        #cleaning up after castling, even if it didnt happen
        if piece.isKing():
            if piece.castling_up != None:
                piece.castling_up = None
            if piece.castling_down != None:
                piece.castling_down = None
        check_mate = self.checkMate(self.playerTurn.color)
        if check_mate:
            self.setMessage('Check Mate')

    #removes possible moving routes from the board
    def hideMarks(self):
        for i in range(0, len(self.squares)):
            for j in range(0, len(self.squares[i])):
                cell = self.squares[i][j]
                if(cell == self.markedSymbol):
                    self.squares[i][j] = None
                elif isinstance(cell, Piece):
                    cell.targeted = False
    
    #check if mouse clicked on a piece and show possible movement routes
    def checkClick(self, pos, size):
        if self.pieceMoving == None: #prevent action when animation still going
            clickX = pos[0]
            clickY = pos[1]
            newX = None
            newY = None
            cell = None
            found = False
            for i in range(0, len(self.squares)):
                for j in range(0, len(self.squares[i])):
                    if clickX > size * i and clickX < size * i + size and clickY > size * j and clickY < size * j + size:
                        cell = self.squares[i][j]
                        newX = i
                        newY = j
                        found = True
                        break
                if found:
                    break
                
            if cell != None:
                if isinstance(cell, Piece): #if the selected cell has a piece
                    if cell.player.color == self.playerTurn.color:
                        self.hideMarks()
                        if cell != self.selectedPiece:
                            cell.showPossibleRoutes(False)
                            self.selectedPiece = cell
                        else:
                            self.selectedPiece = None
                    elif cell.targeted:
                        self.movePiece(self.selectedPiece, newX, newY)
                        self.hideMarks()
                elif cell == self.markedSymbol:
                    if self.selectedPiece != None:
                        self.movePiece(self.selectedPiece, newX, newY)
                        self.hideMarks()
            else: #if not a piece, remove selection and hide cell movement routes
                self.selectedPiece = None
                self.hideMarks()
            
    #method that checks if king is under check
    def kingChecked(self, playerColor):
        foundOppositeColor = None
        for i in range(0, len(self.squares)):
            for j in range(0, len(self.squares[i])):
                if isinstance(self.squares[i][j], Piece):
                    theKingChecked = self.squares[i][j].showPossibleRoutes(True)
                    if theKingChecked != None:
                        if theKingChecked != playerColor:
                            foundOppositeColor = theKingChecked
                        else:
                            return theKingChecked
        if foundOppositeColor != None:
            return foundOppositeColor
        return None

    #method that checks if checkmate
    def checkMate(self, playerColor):
        for i in range(0, len(self.squares)):
            for j in range(0, len(self.squares[i])):
                cell = self.squares[i][j]
                if isinstance(cell, Piece):
                    if cell.player.color == playerColor:
                        cell_possible_routes = []
                        cell.showPossibleRoutes(False)
                        newPos = None
                        for x in range(0, len(self.squares)):
                            for y in range(0, len(self.squares[x])):
                                inner_cell = self.squares[x][y]
                                if inner_cell == self.markedSymbol:
                                    pos = (x, y)
                                    cell_possible_routes.append(pos)
                        for k in range(0, len(cell_possible_routes)):
                            newPos = cell_possible_routes[k]
                            oldX = cell.getX()
                            oldY = cell.getY()
                            cell.setX(newPos[0])
                            cell.setY(newPos[1])
                            self.squares[newPos[0]][newPos[1]] = cell
                            self.squares[oldX][oldY] = None
                            #check if king is checked
                            theKingChecked = self.kingChecked(cell.player.color)

                            cell.setX(oldX)
                            cell.setY(oldY)
                            self.squares[oldX][oldY] = cell
                            self.squares[newPos[0]][newPos[1]] = None
                            if theKingChecked == None:
                                return False
        return True

        # ==== BRAINSTORMING ====
        # if self.kingUnderAttack == None:
        #     # check all player pieces
        #     #   foreach piece check all movements
        #     #       foreach movement check all opposite player pieces
        #     #           foreach other player pieces check all piece movements
        #     #               foreach other player piece movement check if it makes king checked
        #     pass
        # else:
        #     # check if king can move and go out of check zone
        #     # check all player pieces
        #     #   foreach piece check all possible movements
        #     #       foreach movement check all opposite player pieces
        #     #           foreach other player piece check all movements
        #     #               foreach other player piece movement check if king still checked
        #     # if all above false then checkmate
        #     pass
        
        # for i in range(0, len(self.squares)):
        #     for j in range(0, len(self.squares[i])):
        #         pass
       