from app import App
from steam_client.models import SteamUser

if __name__ == '__main__':
    app = App()
    steam_id = input("Enter your Steam ID: ")
    user = SteamUser(steam_id)

    friends_list = app.client.get_user_friends(user)
    user.game_list = app.client.get_user_games(user)

    for friend in friends_list:
        friend.game_list = app.client.get_user_games(friend)

    top_games = app.get_most_popular_games(user, friends_list)

    suggestions = app.create_game_suggestions(top_games)

    app.display_game_suggestions(user, suggestions)

