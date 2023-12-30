class Piece:
    def __init__(self, x, y, player, board):
        self.x = x
        self.y = y
        self.player = player
        self.type = None
        self.board = board
        self.moves = 0
        self.targeted = False
        self.image = None
        
    def setImage(self, image):
        self.image = image

    def __str__(self): #used to print the name of the piece for debugging
        if self.targeted:
            return self.type + ' T(' + self.player.color + ')'
        else:
            return self.type + ' (' + self.player.color + ')'
    def __repr__(self):
        return self.__str__()
    def showPossibleRoutes(self, checkingCheck):
        pass
    def show(self):
        pass
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def isKing(self): #need it to check if king is checked or checkmate
        return False
    def isPawn(self): #need it to check if pawn reached the end to turn it to Queen
        return False