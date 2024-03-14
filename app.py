import os
from collections import defaultdict

from steam_client.client import SteamClient


class App:
    def __init__(self):
        api_key = os.environ["STEAM_API_KEY"]
        self.client = SteamClient(api_key)

    def get_most_popular_games(self, user, friends_list):
        top_games = defaultdict(int)
        for game in user.game_list:
            for friend in friends_list:
                if game in friend.game_list:
                    top_games[game.game_id] += 1

        return top_games

    def create_game_suggestions(self, top_games):
        games_suggestions_ids = []
        sorted_games = sorted(top_games.items(), key=lambda item: item[1], reverse=True)
        for game in sorted_games:
            if self.client.check_coop(game[0]):
                games_suggestions_ids.append(game[0])
                if len(games_suggestions_ids) == 3:
                    break

        return games_suggestions_ids

    def display_game_suggestions(self, user, game_suggestions_ids):
        print("Your game suggestions are:")
        for game_id in game_suggestions_ids:
            for game in user.game_list:
                if game.game_id == game_id:
                    print(game.name)
