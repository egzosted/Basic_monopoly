import board, player
import tkinter as tk
from GUI import game_window as g_w


class Game:
    def __init__(self, window, players_color, gw):
        self.game_window = gw
        self.board = board.Board(window, gw)
        self.players = []
        for i in players_color:
            self.players.append(player.Player(i, 3000))
        self.current_player_index = 0
        self.current_player = self.players[0]

    def perform_round(self):
        self.game_window.hide_menu()
        self.current_player.move(self.board.size)   # player has to get new position
        self.board.fields[self.current_player.position].handle_player(self.current_player)     # then field will perform an action



# Metoda przeprowadzenia tury

# slownik nieruchomosci i ich wlasciciela
