from bs4 import BeautifulSoup

@staticmethod
def clean_description(description):
    # Clean description so HTML tags do not show
    return BeautifulSoup(description, "html.parser").get_text() if description else ""

@staticmethod
def sort_games_by_matching(games, user):
    # Insertion Sort
    for i in range(len(games)):
        key_game = games[i]
        j = i - 1
        while j >= 0 and is_better_match(key_game, games[j], user):
            # Check if game is a better match -> if it is, rearrange
            games[j + 1] = games[j]
            j -= 1
        games[j + 1] = key_game
    return games

@staticmethod
def is_better_match(game1, game2, user):
    # Check if game1 matches the console type
    if game1.platform in user.selected_platforms:
        # If game2 doesn't match the console type, prioritize game1
        if game2.platform not in user.selected_platforms:
            return True

    # Compare platforms first
    platforms_match1 = count_matching_platforms(game1.platform, user.selected_platforms)
    platforms_match2 = count_matching_platforms(game2.platform, user.selected_platforms)

    if platforms_match1 != platforms_match2:
        # If platforms match differs, return True if game1 has more matching platforms
        return platforms_match1 > platforms_match2

    # If platforms match is equal, compare genres
    genres_match1 = count_matching_genres(game1.genre, user.selected_genres)
    genres_match2 = count_matching_genres(game2.genre, user.selected_genres)

    # Return True if game1 has more matching genres
    if genres_match1 != genres_match2:
        return genres_match1 > genres_match2
    
    return False

@staticmethod
def count_matching_platforms(platforms, selected_platforms):
    # Count amount of matching platforms
    return sum(1 for platform in platforms if platform in selected_platforms)

@staticmethod
def count_matching_genres(genres, selected_genres):
    # Count amount of matching genres
    return sum(1 for genre in genres if genre in selected_genres)
