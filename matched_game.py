from game import Game

class MatchedGame(Game):
    # Matched Game class
    def __init__(self, title, genres, platforms, rating, description, is_super_liked=False):
        super().__init__(title, genres, platforms, rating, description)
        self.is_super_liked = is_super_liked

    @classmethod
    def from_game(cls, game, is_super_liked=False):
        # Create MatchedGame object from Game object
        return cls(game.title, game.genre, game.platform, game.rating, game.description, is_super_liked)
    
    def __lt__(self, other):
        # Super-liked games should be prioritized over regular liked games
        if self.is_super_liked and not other.is_super_liked:
            return True
        elif not self.is_super_liked and other.is_super_liked:
            return False
        # If both are either super-liked or regular liked, prioritize based on title
        return self.title < other.title
    
    # Getters and setters
    def get_is_super_liked(self):
        return self.is_super_liked
    
    def set_is_super_liked(self, is_super_liked):
        self.is_super_liked = is_super_liked