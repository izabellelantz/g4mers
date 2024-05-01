import unittest
from matched_game import MatchedGame
from game import Game
from user import User
import utils

class TestG4MERS(unittest.TestCase):

    def test_add_genre(self):
        # Test adding genre to user object
        user = User("Leah")
        user.add_genre("Adventure")
        self.assertIn("Adventure", user.selected_genres)

    def test_remove_genre(self):
        # Test removing genre from user
        user = User("Belle", selected_genres=["Simulation"])
        user.remove_genre("Simulation")
        self.assertNotIn("Simulation", user.selected_genres)

    def test_add_platform(self):
        # Test adding platform to user
        user = User("Belle")
        user.add_platform("Nintendo Switch")
        self.assertIn("Nintendo Switch", user.selected_platforms)

    def test_remove_platform(self):
        # Test removing platform from user
        user = User("Belle", selected_platforms=["Nintendo Switch"])
        user.remove_platform("Nintendo Switch")
        self.assertNotIn("Nintendo Switch", user.selected_platforms)

    def test_from_game(self):
        # Test converting Game object into MatchedGame object
        original_game = Game("Original", ["Genre"], ["Platform"], 4.0, "Description")
        matched_game = MatchedGame.from_game(original_game)
        self.assertEqual(matched_game.title, "Original")
        self.assertEqual(matched_game.genre, original_game.genre)
        self.assertEqual(matched_game.platform, original_game.platform)
        self.assertEqual(matched_game.rating, 4.0)
        self.assertEqual(matched_game.description, "Description")

    def test_sort_games_by_matching(self):
        # Test sorting games by matching
        user = User(firstname="Chris", selected_genres=["Action", "Adventure"], selected_platforms=["PC", "PlayStation"])
        games = [
            Game(title="Game 1", genre=["Action"], platform=["PC"], rating=4.0, description="D1"),
            Game(title="Game 2", genre=["Adventure"], platform=["PlayStation"], rating=5.6, description="D2"),
            Game(title="Game 3", genre=["RPG"], platform=["PC"], rating=3.2, description="D3"),
            Game(title="Game 4", genre=["Action", "Adventure"], platform=["PlayStation"], rating=9.8, description="D4")
        ]
        sorted_games = utils.sort_games_by_matching(games, user)
        expected_titles = ["Game 4", "Game 1", "Game 2", "Game 3"]
        self.assertEqual([game.title for game in sorted_games], expected_titles)

    def test_is_better_match(self):
        # Test comparing games
        user = User(firstname="Chris", selected_genres=["Action", "Adventure"], selected_platforms=["PC", "PlayStation"])
        game1 = Game(title="Game 1", genre=["Action"], platform=["PC"], rating=4.0, description="D1")
        game2 = Game(title="Game 2", genre=["Adventure"], platform=["PlayStation"], rating=5.6, description="D2")
        game3 = Game(title="Game 3", genre=["RPG"], platform=["PC"], rating=3.2, description="D3")
        game4 = Game(title="Game 4", genre=["Action", "Adventure"], platform=["PlayStation"], rating=9.8, description="D4")
        
        # Game 4 should be better match than Game 1
        self.assertTrue(utils.is_better_match(game4, game1, user))
        # Game 4 should be better match than Game 3
        self.assertTrue(utils.is_better_match(game4, game3, user))
        # Game 2 should not be better match than Game 1 (they are equal)
        self.assertFalse(utils.is_better_match(game2, game1, user))
        # Game 2 should be better match than Game 3
        self.assertTrue(utils.is_better_match(game2, game3, user))

    def test_count_matching_platforms(self):
        # Test counting matching platforms
        selected_platforms = ["PC", "PlayStation", "Xbox"]
        platforms = ["PC", "PlayStation", "Switch"]
        count = utils.count_matching_platforms(platforms, selected_platforms)
        self.assertEqual(count, 2)
        
        # Test when no platforms match
        platforms = ["Nintendo", "Sega"]
        count = utils.count_matching_platforms(platforms, selected_platforms)
        self.assertEqual(count, 0)

    def test_count_matching_genres(self):
        # Test counting matching genres
        selected_genres = ["Action", "Adventure", "RPG"]
        genres = ["Action", "Racing", "Puzzle", "RPG"]
        count = utils.count_matching_genres(genres, selected_genres)
        self.assertEqual(count, 2)
        
        # Test when no genres match
        genres = ["Simulation", "Strategy"]
        count = utils.count_matching_genres(genres, selected_genres)
        self.assertEqual(count, 0)


if __name__ == "__main__":
    unittest.main()