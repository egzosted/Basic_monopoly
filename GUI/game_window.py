import board, game
import tkinter as tk


class GameWindow:
    def __init__(self, players_color):
        self.players_color = players_color
        self.window = tk.Tk()
        self.window.geometry("1024x768")
        self.game = game.Game(self.window, players_color)

        # creation labels for players and name of game
        self.l_monopoly = tk.Label(self.window, text="Monopoly", font=("Courier", 30))
        screen_width, screen_height = self.get_width_height()
        self.l_monopoly.place(x=0.4 * screen_width, y=0.3 * screen_height)
        self.l_current_player = tk.Label(self.window, text=f"Next: {self.game.current_player}", font=("Courier", 15))
        self.l_current_player.place(x=0.6 * screen_width, y=0.4 * screen_height)
        self.b_next_round = tk.Button(self.window, text="Next round", bg="MediumPurple4", fg="white")
        self.b_next_round.place(x=0.6 * screen_width, y=0.6 * screen_height)
        self.l_players = []
        for index, i in enumerate(self.game.players):
            self.l_players.append(tk.Label(text=f"Player no {index + 1}: {i.name} {i.cash}", font=("Courier", 15), fg=i.name))
            self.l_players[index].place(x=0.5*screen_width, y=(0.4 + index / 10) * screen_height)
        self.window.bind("<Configure>", self.on_resize)
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
