import tkinter as tk
from tkinter import messagebox
from user import User
from swipe import SwipePage

class StartPage:
    def __init__(self, root):
        self.root = root
        self.root.title("G4MERS Preferences")
        self.root.geometry("1200x700")

        # Create input fields
        self.create_input_fields()

        # Create save button
        self.create_save_button()

    def create_input_fields(self):
        # First Name
        first_name_label = tk.Label(self.root, text="First Name:")
        first_name_label.pack(padx=10, pady=5)
        self.firstname_entry = tk.Entry(self.root)
        self.firstname_entry.pack(padx=10, pady=5)

        # Preferred Genres w/ Options
        genre_label = tk.Label(self.root, text="Preferred Genres:")
        genre_label.pack(padx=10, pady=5)
        self.selected_genres = []
        for genre in ["Action", "Adventure", "RPG", "Strategy / Tactics", "Simulation", "Fighting", "Cards / Tiles", "Visual Novel", "Romance"]:
            genre_var = tk.BooleanVar()
            genre_var.set(False)
            genre_checkbutton = tk.Checkbutton(self.root, text=genre, variable=genre_var)
            genre_checkbutton.pack(padx=10, pady=2, anchor="w")
            self.selected_genres.append((genre, genre_var))

        # Preferred Consoles w/ options
        platform_label = tk.Label(self.root, text="Preferred Consoles:")
        platform_label.pack(padx=10, pady=5)
        self.selected_platforms = []
        for console in ["Xbox One", "Xbox Series", "PlayStation 4", "PlayStation 5", "Nintendo Switch", "Nintendo DS"]:
            console_var = tk.BooleanVar()
            console_var.set(False)
            console_checkbutton = tk.Checkbutton(self.root, text=console, variable=console_var)
            console_checkbutton.pack(padx=10, pady=2, anchor="w")
            self.selected_platforms.append((console, console_var))

    def create_save_button(self):
        # Save Button
        save_button = tk.Button(self.root, text="Save Preferences", command=self.save_preferences)
        save_button.pack(pady=10)

    def save_preferences(self):
        # Get values from input fields
        firstname = self.firstname_entry.get()
        selected_genres = [genre[0] for genre in self.selected_genres if genre[1].get()]
        selected_platforms = [platform[0] for platform in self.selected_platforms if platform[1].get()]

        if not firstname:
            messagebox.showerror("Error", "Please enter your first name.")
            return

        # Create user object with selected preferences
        user = User(firstname, selected_genres, selected_platforms)

        # Display a message box with the collected preferences
        messagebox.showinfo("Preferences Saved", f"First Name: {firstname}\nPreferred Genres: {selected_genres}\nPreferred Consoles: {selected_platforms}")

        # Clear the screen and move to the swipe page
        self.clear_screen()
        self.swipe_page = SwipePage(self.root, user)

    def clear_screen(self):
        # Clear entire window
        for widget in self.root.winfo_children():
            widget.destroy()
