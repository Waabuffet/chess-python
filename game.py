from pieces.king import King
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.rook import Rook
from board.board import Board
from player.player import Player
import pygame

#pygame setup
pygame.init()
SCREEN_WIDTH_HEIGHT = 600
MESSAGE_SCREEN_HEIGHT = 50
screen = pygame.display.set_mode((SCREEN_WIDTH_HEIGHT, SCREEN_WIDTH_HEIGHT + MESSAGE_SCREEN_HEIGHT))
pygame.display.set_caption('Chess Game')
white, black = (255,255,255), (0,0,0)
boardLength = 8
size = SCREEN_WIDTH_HEIGHT // boardLength
screen.fill(white)

#text setup
TEXT_SIZE = 15
pygame.font.init()
comicFont = pygame.font.SysFont('Comic Sans MS', TEXT_SIZE)


#game setup
player1 = None
player2 = None
board = None
 
def newGame():
    global player1
    global player2
    global board
    player1 = Player('white')
    player2 = Player('black')
    board = Board(player1, player2, boardLength, size, comicFont)

    #adding pieces on the board for both players
    board.addPiece(Rook(0, 0, player2, board), 0, 0)
    board.addPiece(Knight(0, 1, player2, board), 0, 1)
    board.addPiece(Bishop(0, 2, player2, board), 0, 2)
    board.addPiece(Queen(0, 3, player2, board), 0, 3)
    board.addPiece(King(0, 4, player2, board), 0, 4)
    board.addPiece(Bishop(0, 5, player2, board), 0, 5)
    board.addPiece(Knight(0, 6, player2, board), 0, 6)
    board.addPiece(Rook(0, 7, player2, board), 0, 7)

    board.addPiece(Rook(7, 0, player1, board), 7, 0)
    board.addPiece(Knight(7, 1, player1, board), 7, 1)
    board.addPiece(Bishop(7, 2, player1, board), 7, 2)
    board.addPiece(Queen(7, 3, player1, board), 7, 3)
    board.addPiece(King(7, 4, player1, board), 7, 4)
    board.addPiece(Bishop(7, 5, player1, board), 7, 5)
    board.addPiece(Knight(7, 6, player1, board), 7, 6)
    board.addPiece(Rook(7, 7, player1, board), 7, 7)

    for i in range(0, boardLength):
        board.addPiece(Pawn(1, i, player2, board), 1, i)
    
    for i in range(0, boardLength):
        board.addPiece(Pawn(6, i, player1, board), 6, i)

    #giving each piece its respective image
    for i in range(0, boardLength):
        for j in range(0, boardLength):
            if board.squares[i][j] != None:
                piece = board.squares[i][j]
                if piece.type == 'pawn' and piece.player.color == 'black':
                    piece.setImage('./assets/Pawn B.png')
                elif piece.type == 'pawn' and piece.player.color == 'white':
                    piece.setImage('./assets/Pawn W.png')
                elif piece.type == 'rook' and piece.player.color == 'black':
                    piece.setImage('./assets/Rook B.png')
                elif piece.type == 'rook' and piece.player.color == 'white':
                    piece.setImage('./assets/Rook W.png')
                elif piece.type == 'knight' and piece.player.color == 'black':
                    piece.setImage('./assets/Knight B.png')
                elif piece.type == 'knight' and piece.player.color == 'white':
                    piece.setImage('./assets/Knight W.png')
                elif piece.type == 'bishop' and piece.player.color == 'black':
                    piece.setImage('./assets/Bishop B.png')
                elif piece.type == 'bishop' and piece.player.color == 'white':
                    piece.setImage('./assets/Bishop W.png')
                elif piece.type == 'queen' and piece.player.color == 'black':
                    piece.setImage('./assets/Queen B.png')
                elif piece.type == 'queen' and piece.player.color == 'white':
                    piece.setImage('./assets/Queen W.png')
                elif piece.type == 'king' and piece.player.color == 'black':
                    piece.setImage('./assets/King B.png')
                elif piece.type == 'king' and piece.player.color == 'white':
                    piece.setImage('./assets/King W.png')
    

newGame()
board.setMessage('White turn')

pygame.draw.rect(screen, black, [size, size, boardLength*size, boardLength*size], 1)
pygame.display.update()

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            board.checkClick(pos, size)
    
    board.show(pygame, screen)
    pygame.display.flip()
