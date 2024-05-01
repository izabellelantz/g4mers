import tkinter as tk
import utils
import heapq
from matches import MatchesPage
from matched_game import MatchedGame
from fetch import fetch_games

class SwipePage:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        # Create matches proirity queue using heapq
        self.matches = []

        self.root.title("G4MERS")

        # Fetch game recommendations from API based on user preferences and then sort using insertion sort method in utils file
        self.games = fetch_games(self.user.selected_genres, self.user.selected_platforms)
        self.games = utils.sort_games_by_matching(self.games, self.user)

        # Create labels and buttons and add to screen
        self.create_info_label()
        self.create_game_display()
        self.create_nav_buttons()
        self.create_matches_button()

    def create_info_label(self):
        # Create info label storing information about user
        self.name_label = tk.Label(self.root, text=self.user.firstname)
        self.name_label.pack(pady=10)

    def create_game_display(self):
        # Set current game index to 0 when initially set up
        self.current_game_index = 0
        # Create label and set on page
        self.game_display = tk.Label(self.root, text="")
        self.game_display.pack(pady=10)
        # Call update method
        self.update_game_display()

    def create_nav_buttons(self):
        # Add buttons for like, dislike, and superlike
        dislike_button = tk.Button(self.root, text="❮ PASS", command=self.dislike)
        dislike_button.pack(side="left", padx=10)
        like_button = tk.Button(self.root, text="LIKE ❯", command=self.like)
        like_button.pack(side="right", padx=10)
        superlike_button = tk.Button(self.root, text="❤", command=self.super_like)
        superlike_button.pack(side="bottom", pady=10)

    def dislike(self):
        # If dislike -> add one to index and simply move past
        self.current_game_index += 1
        self.update_game_display()

    def like(self):
        # Create MatchedGame obejct from game object
        matched_game = MatchedGame.from_game(self.games[self.current_game_index])
        priority = 0  # Regular priority for liked games
        heapq.heappush(self.matches, (priority, matched_game)) # Add to priority queue
        self.current_game_index += 1 # Move on
        self.update_game_display()

    def super_like(self):
        # Create MatchedGame object from game object
        matched_game = MatchedGame.from_game(self.games[self.current_game_index], is_super_liked=True)
        priority = -1  # Higher priority for super-liked games
        heapq.heappush(self.matches, (priority, matched_game)) # Add to priority queue
        self.current_game_index += 1 # Move on
        self.update_game_display()

    def update_game_display(self):
        while self.current_game_index < len(self.games):
            # While there are games yet to go through
            # Clear the current game from screen
            self.clear_game_display()

            # Set new game
            game = self.games[self.current_game_index]
        
            # Format genres and platforms
            genres = ', '.join(game.genre)
            platforms = ', '.join(game.platform)
            # Clean up the description
            description = utils.clean_description(game.description)

            # Construct game info string
            game_info = f"Title: {game.title}\nGenres: {genres}\nPlatform: {platforms}\nRating: {game.rating}"

            try:
                # Load image
                cover_photo_path = "controller.png"
                cover_photo = tk.PhotoImage(file=cover_photo_path)
                cover_photo = cover_photo.subsample(8, 8)
                self.cover_photo_label = tk.Label(self.root, image=cover_photo)
                self.cover_photo_label.image = cover_photo  # Keep reference to prevent garbage collection
                self.cover_photo_label.pack(pady=10)
            except Exception as e:
                print("Error loading cover photo:", e)

            # Display game info and description
            self.game_display.config(text=game_info)
            self.description_label = tk.Label(self.root, text=description, justify=tk.LEFT, wraplength=700)
            self.description_label.pack(pady=10)

            return
        # If no more games match the criteria, update the display to show no more games
        self.game_display.config(text="No more games to display")



    def create_matches_button(self):
        # Matches Button
        self.matches_button = tk.Button(self.root, text="View Matches", command=self.show_matches_page)
        self.matches_button.pack(pady=10)

    def clear_screen(self):
        # Destroy all widgets except name
        for widget in self.root.winfo_children():
            if widget != self.name_label:
                widget.destroy()

    def clear_game_display(self):
        # Clear the game area only
        if hasattr(self, 'description_label'):
            self.description_label.destroy()
        if hasattr(self, 'cover_photo_label'):
            self.cover_photo_label.destroy()

    def show_matches_page(self):
        # clear the screen and open the matches page instead
        self.clear_screen()
        self.matches_page = MatchesPage(self.root, self.user, self.matches)