import board, player
import tkinter as tk
from GUI import game_window as gw


class Game:
    def __init__(self, window, players_color):
        self.board = board.Board(window)
        self.players = []
        for i in players_color:
            self.players.append(player.Player(i, 3000))
        self.current_player = self.players[0].name





# Metoda przeprowadzenia tury

# slownik nieruchomosci i ich wlasciciela
