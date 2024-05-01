import tkinter as tk

class MatchesPage:
    def __init__(self, root, user, liked_games):
        self.root = root
        self.user = user
        self.liked_games = liked_games

        self.root.title("Matches")

        # Display the user's first name
        self.name_label = tk.Label(self.root, text=f"Welcome {self.user.firstname}")
        self.name_label.pack(pady=10)

        # Define background colors for matches
        self.regular_liked_color = "lightgreen"
        self.super_liked_color = "lightpink"

        # Display liked games
        self.display_liked_games()

    def display_liked_games(self):
        if self.liked_games:
            for match in self.liked_games:
                game = match[1]  # Access the MatchedGame object from the tuple

                # Choose background color based on whether the game is super-liked or not
                bg_color = self.super_liked_color if game.is_super_liked else self.regular_liked_color

                # Construct game info string
                game_info = f"Title: {game.title}\nGenres: {game.genre}\nPlatform: {game.platform}\nRating: {game.rating}"

                # Create a frame to hold the game information
                game_frame = tk.Frame(self.root, bg=bg_color)
                game_frame.pack(pady=5, fill=tk.X)

                # Display game information
                game_info_label = tk.Label(game_frame, text=game_info, justify=tk.LEFT)
                game_info_label.grid(row=0, column=1, padx=10, pady=5)

        else:
            # Show no matches if that is the case
            no_matches_label = tk.Label(self.root, text="You haven't liked any games yet.", padx=10, pady=5)
            no_matches_label.pack(pady=5)