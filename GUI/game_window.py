import board, game
import tkinter as tk


class GameWindow:
    def __init__(self, players_color):
        self.players_color = players_color
        self.window = tk.Tk()
        self.window.geometry("1024x768")
        self.this_game = game.Game(self.window, players_color, self)

        # creation labels for players and name of game
        self.l_monopoly = tk.Label(self.window, text="Monopoly", font=("Courier", 30))
        screen_width, screen_height = self.get_width_height()
        self.l_monopoly.place(x=0.4 * screen_width, y=0.3 * screen_height)
        self.l_current_player = tk.Label(self.window, text=f"Next: {self.this_game.players[self.this_game.current_player_index].name}", font=("Courier", 15))
        self.l_current_player.place(x=0.6 * screen_width, y=0.4 * screen_height)
        self.b_next_round = tk.Button(self.window, text="Next round", bg="MediumPurple4", fg="white", command=self.this_game.perform_round)
        self.b_next_round.place(x=0.6 * screen_width, y=0.6 * screen_height)
        self.l_players = []
        for index, i in enumerate(self.this_game.players):
            self.l_players.append(tk.Label(text=f"Player no {index + 1}: {i.name} {i.cash} {i.position}", font=("Courier", 15), fg=i.name))
            self.l_players[index].place(x=0.5*screen_width, y=(0.4 + index / 10) * screen_height)
        self.window.bind("<Configure>", self.on_resize)

        # buttons for situation when field doesnt have owner
        self.b_skip = tk.Button(self.window, text="Skip", bg="black", fg="white", font=("Courier", 20), command=self.buy_action)
        self.b_buy = tk.Button(self.window, text="Buy", bg="black", fg="white", font=("Courier", 20))
        self.window.mainloop()

    def on_resize(self, event):
        screen_width, screen_height = self.get_width_height()
        self.l_monopoly.place(x=0.3 * screen_width, y=0.3 * screen_height)
        for index, i in enumerate(self.l_players):
            i.place(x=0.3 * screen_width, y=(0.4 + index / 10) * screen_height)
        self.l_current_player.place(x=0.6 * screen_width, y=0.4 * screen_height)
        self.b_next_round.place(x=0.6 * screen_width, y=0.6 * screen_height)

    def get_width_height(self):
        self.window.update()
        return self.window.winfo_width(), self.window.winfo_height()

    def hide_menu(self):
        self.l_monopoly.lower()
        self.l_current_player.lower()
        self.b_next_round.lower()
        for index, i in enumerate(self.l_players):
            j = self.this_game.players[index]
            i.config(text=f"Player no {index + 1}: {j.name} {j.cash} {j.position}")
            i.lift()
        for i in self.l_players:
            i.lower()

    def show_menu(self):
        self.this_game.current_player_index = (self.this_game.current_player_index + 1) % len(self.l_players)
        self.this_game.current_player = self.this_game.players[self.this_game.current_player_index]
        self.l_monopoly.lift()
        self.l_current_player.lift()
        self.b_next_round.lift()
        for index, i in enumerate(self.l_players):
            j = self.this_game.players[index]
            i.config(text=f"Player no {index + 1}: {j.name} {j.cash} {j.position}")
            i.lift()
        self.l_current_player.config(text=f"Next: {self.this_game.players[self.this_game.current_player_index].name}")

    def show_offer(self, city, player):
        screen_width, screen_height = self.get_width_height()
        self.b_skip.place(x=0.5 * screen_width, y=0.5 * screen_height)
        self.b_buy.place(x=0.5 * screen_width, y=0.6 * screen_height)
        self.b_skip.lift()
        self.b_buy.lift()
        self.b_buy.config(command=lambda: [city.first_owner(player), self.buy_action()])

    def buy_action(self):
        self.b_skip.lower()
        self.b_buy.lower()
        self.show_menu()




