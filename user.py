class User:
    # User class
    def __init__(self, firstname, selected_genres=[], selected_platforms=[]):
        self.firstname = firstname
        self.selected_genres = selected_genres
        self.selected_platforms = selected_platforms

    def add_genre(self, genre):
        if genre not in self.selected_genres:
            self.selected_genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.selected_genres:
            self.selected_genres.remove(genre)

    def add_console(self, console):
        if console not in self.selected_platforms:
            self.selected_platforms.append(console)

    def remove_console(self, console):
        if console in self.selected_platforms:
            self.selected_platforms.remove(console)
