from player.player import Player

class AI(Player):
    def __init__(self, color, difficulty):
        super().__init__(color)
        self.difficulty = difficulty

    def makeMove(self):
        pass