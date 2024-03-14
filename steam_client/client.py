import requests
from steam_client.models import SteamUser, SteamGame


class SteamClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_user_friends(self, user):
        friends_list = []
        url = f"http://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={self.api_key}&steamid={user.user_id}"
        response = requests.get(url)

        friends_data = response.json()["friendslist"]["friends"]
        for steam_user_data in friends_data:
            steam_user = SteamUser(steam_user_data["steamid"])
            friends_list.append(steam_user)

        return friends_list

    def get_user_games(self, steam_user):
        games_list = []
        url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={self.api_key}&steamid={steam_user.user_id}&include_appinfo=true&include_played_free_games=true"

        response = requests.get(url)
        games_data = response.json()["response"].get("games", [])
        for game_data in games_data:
            game = SteamGame(game_id=game_data["appid"], name=game_data["name"])
            games_list.append(game)

        return games_list

    def check_coop(self, game_id):
        url = f"https://store.steampowered.com/api/appdetails?l=en&filters=categories&appids={game_id}"
        response = requests.get(url)

        game_data = response.json().get(str(game_id))

        for category in game_data["data"]["categories"]:
            if category["id"] == 9:
                return True

        return False
