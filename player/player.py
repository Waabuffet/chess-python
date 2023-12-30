class Player:
    def __init__(self, color):
        self.color = color
        self.moves = 0
        self.timeSpent = 0

# we can also implement the time spent by each player to make things more interesting
# or we can allow each player a limited time if we want to rush the game