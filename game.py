class Game:
    # Game class
    def __init__(self, title, genre, platform, rating, description):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.rating = rating
        self.description = description

    # Getters and Setters
    def get_title(self):
        return self.title
    
    def get_genre(self):
        return self.genre
    
    def get_platform(self):
        return self.platform
    
    def get_rating(self):
        return self.rating
    
    def get_description(self):
        return self.description
    
    def set_title(self, title):
        self.title = title

    def set_genre(self, genre):
        self.genre = genre
    
    def set_platform(self, platform):
        self.platform = platform

    def set_rating(self, rating):
        self.rating = rating

    def set_description(self, description):
        self.description = description