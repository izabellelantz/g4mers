class User:
    # User class
    def __init__(self, firstname, selected_genres=[], selected_platforms=[]):
        self.firstname = firstname
        self.selected_genres = selected_genres
        self.selected_platforms = selected_platforms
    
    def get_firstname(self):
        return self.firstname
    
    def set_firstname(self, firstname):
        self.firstname = firstname
        
    # Add and remove genres from user
    def add_genre(self, genre):
        if genre not in self.selected_genres:
            self.selected_genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.selected_genres:
            self.selected_genres.remove(genre)

    def add_platform(self, platform):
        if platform not in self.selected_platforms:
            self.selected_platforms.append(platform)

    def remove_platform(self, platform):
        if platform in self.selected_platforms:
            self.selected_platforms.remove(platform)
