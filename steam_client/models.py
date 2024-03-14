class SteamGame:
    def __init__(self, game_id, name):
        self.game_id = game_id
        self.name = name

    def __str__(self):
        return f"Steam Game {self.game_id}"

    def __repr__(self):
        return f"Steam Game {self.game_id}"

    def __eq__(self, other):
        return self.name == other.name

class SteamUser:
    def __init__(self, user_id, game_list=None):
        self.user_id = user_id
        self.game_list = game_list or []

    def __str__(self):
        return f"Steam User {self.user_id}"

    def __repr__(self):
        return f"Steam User {self.user_id}"
