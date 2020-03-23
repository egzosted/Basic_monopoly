import board
import player


class Game:
    def __init__(self, window, players_color, gw):
        self.game_window = gw
        self.board = board.Board(window, self.game_window)
        self.players = []
        for i in players_color:
            self.players.append(player.Player(i, 3000))
        self.current_player_index = 0
        self.current_player = self.players[0]

    def perform_round(self):
        self.game_window.hide_menu()
        self.current_player.move(self.board.size)   # player has to get new position
        self.game_window.draw_players()
        self.board.fields[self.current_player.position].handle_player(
            self.current_player)     # then field will perform an action

    def find_owner(self, position):
        owner_name = self.board.fields[position].owner
        for i in self.players:
            if i.name == owner_name:
                return i


# Metoda przeprowadzenia tury

# slownik nieruchomosci i ich wlasciciela
