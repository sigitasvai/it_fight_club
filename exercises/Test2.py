import random


class Player:
    def __init__(self, nickname, is_ready):
        self.nickname = nickname
        self.is_ready = is_ready


class LocalPlayer(Player):
    def __init__(self, nickname, is_ready):
        super().__init__(nickname, is_ready)
        self.joystick_number = 0

    def set_joystick_number(self, number):
        self.joystick_number = number


class OnlinePlayer(Player):
    def __init__(self, nickname, is_ready, latency_ms):
        super().__init__(nickname, is_ready)
        self.latency_ms = latency_ms

    def get_connection_rating(self):
        if self.latency_ms < 50:
            return "Good"
        elif 50 < self.latency_ms < 80:
            return "Fair"
        elif self.latency_ms >= 80:
            return "Bad"


class Game:
    def __init__(self):
        self.players = []
        self.joystick_number = 1

    def addPlayer(self, player):
        if isinstance(player, LocalPlayer):
            LocalPlayer.set_joystick_number(player, self.joystick_number)
            self.joystick_number += 1

        self.players.append(player)


my_game = Game()

my_game.addPlayer(OnlinePlayer("zaraza390", is_ready=True, latency_ms=55))
my_game.addPlayer(LocalPlayer("xman939", is_ready=True))
my_game.addPlayer(LocalPlayer("boosteriz", is_ready=False))

for player in my_game.players:
    if player.is_ready:
        print(f"{player.nickname} is ready!")
        if isinstance(player, OnlinePlayer):
            print(f"Connection: {player.get_connection_rating()}")
        elif isinstance(player, LocalPlayer):
            print(f"Controls: {player.joystick_number}")
