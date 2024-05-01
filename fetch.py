import json
import requests
from game import Game

with open('config.json') as f:
    # Load config file
    config = json.load(f)

# Save API key in variable for use
api_key = config['api_key']

def fetch_games(genres, platforms):
    # Call API with key
    url = f"https://api.mobygames.com/v1/games?api_key={api_key}"
    params = {
        # Params for genres and platforms
        "genres": ",".join(genres),
        "platforms": ",".join(platforms)
    }

    try:
        # Try to call the API with proper parameters
        response = requests.get(url, params=params)
        response.raise_for_status()
        # Save response data
        data = response.json()
        games_data = data.get("games", [])

        # Create a list to store Game objects
        games = []

        # Iterate over game data and create Game objects
        for game_data in games_data:
            # Extract information from game data into variables
            title = game_data.get('title', '')
            genres = [genre['genre_name'] for genre in game_data.get('genres', [])]
            platforms = [platform['platform_name'] for platform in game_data.get('platforms', [])]
            rating = game_data.get('moby_score', '')
            description = game_data.get('description', '')

            # Create Game object and append it to the games list
            game = Game(title, genres, platforms, rating, description)
            games.append(game)

        return games
    except requests.RequestException as e:
        print("Error connecting to API ", e)
        return [], [], []
    