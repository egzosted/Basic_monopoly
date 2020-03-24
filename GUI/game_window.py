import tkinter as tk
import game


class GameWindow:
    def __init__(self, players_color):
        self.players_color = players_color
        self.window = tk.Tk()
        self.window.geometry("1024x768")
        self.symbols = True
        self.this_game = game.Game(self.window, players_color, self)

        # creation labels for players and name of game
        self.l_monopoly = tk.Label(self.window, text="Monopoly", font=("Courier", 30))
        screen_width, screen_height = self.get_width_height()
        self.l_monopoly.place(x=0.4 * screen_width, y=0.3 * screen_height)
        self.l_current_player = tk.Label(
            self.window, text=f"Next: {self.this_game.players[self.this_game.current_player_index].name}", font=("Courier", 15))
        self.l_current_player.place(x=0.6 * screen_width, y=0.4 * screen_height)
        self.b_next_round = tk.Button(
            self.window, text="Next round", bg="MediumPurple4", fg="white", command=self.this_game.perform_round)
        self.b_next_round.place(x=0.6 * screen_width, y=0.6 * screen_height)
        self.l_players = []
        for index, i in enumerate(self.this_game.players):
            self.l_players.append(
                tk.Label(text=f"Player no {index + 1}: {i.name} {i.cash}", font=("Courier", 15), fg=i.name))
            self.l_players[index].place(x=0.5 * screen_width, y=(0.4 + index / 10) * screen_height)

        # buttons for situation when field doesnt have owner
        self.b_skip = tk.Button(self.window, text="Skip", bg="black",
                                fg="white", font=("Courier", 20))
        self.b_buy = tk.Button(self.window, text="Buy", bg="black",
                               fg="white", font=("Courier", 20))

        # button for situation where player on field is owner
        self.b_sell = tk.Button(self.window, text="Sell", bg="black",
                                fg="white", font=("Courier", 20))

        # button for paying rent
        self.b_pay = tk.Button(self.window, text="Pay", bg="black",
                               fg="white", font=("Courier", 20))

        # circles that represent players on map
        self.symbols = [None] * len(self.l_players)
        self.canvas = self.this_game.board.canvas
        self.on_resize()
        self.window.mainloop()

    def on_resize(self):
        screen_width, screen_height = self.get_width_height()
        self.l_monopoly.place(x=0.3 * screen_width, y=0.3 * screen_height)
        for index, i in enumerate(self.l_players):
            i.place(x=0.3 * screen_width, y=(0.4 + index / 10) * screen_height)
        self.l_current_player.place(x=0.6 * screen_width, y=0.4 * screen_height)
        self.b_next_round.place(x=0.6 * screen_width, y=0.6 * screen_height)
        self.draw_players()

    def get_width_height(self):
        self.window.update()
        return self.window.winfo_width(), self.window.winfo_height()

    def hide_menu(self):
        # self.l_monopoly.lower()
        self.l_current_player.lower()
        self.b_next_round.lower()
        # for i in self.l_players:
        # i.lower()

    def show_menu(self):
        self.this_game.current_player_index = (
            self.this_game.current_player_index + 1) % len(self.l_players)
        self.this_game.current_player = self.this_game.players[self.this_game.current_player_index]
        # self.l_monopoly.lift()
        self.l_current_player.lift()
        self.b_next_round.lift()
        for index, i in enumerate(self.l_players):
            j = self.this_game.players[index]
            i.config(text=f"Player no {index + 1}: {j.name} {j.cash}")
            # i.lift()
        self.l_current_player.config(
            text=f"Next: {self.this_game.players[self.this_game.current_player_index].name}")

    def show_offer(self, city, player):
        screen_width, screen_height = self.get_width_height()
        self.b_skip.place(x=0.5 * screen_width, y=0.5 * screen_height)
        self.b_buy.place(x=0.5 * screen_width, y=0.6 * screen_height)
        self.b_skip.lift()
        self.b_buy.lift()
        self.b_skip.config(command=self.buy_action)
        self.b_buy.config(command=lambda: [city.first_owner(player), self.buy_action()])

    def show_sell(self, city, player):
        screen_width, screen_height = self.get_width_height()
        self.b_skip.place(x=0.5 * screen_width, y=0.5 * screen_height)
        self.b_sell.place(x=0.5 * screen_width, y=0.6 * screen_height)
        self.b_skip.lift()
        self.b_sell.lift()
        self.b_skip.config(command=self.sell_action)
        self.b_sell.config(command=lambda: [city.sell_to_bank(player), self.sell_action()])

    def pay_rent(self, city, player):
        screen_width, screen_height = self.get_width_height()
        self.b_pay.place(x=0.5 * screen_width, y=0.5 * screen_height)
        self.b_pay.lift()
        owner = self.this_game.find_owner(player.position)
        self.b_pay.config(command=lambda: [city.charge_rent(player, owner), self.pay_action()])

    def buy_action(self):
        self.b_skip.lower()
        self.b_buy.lower()
        self.show_menu()

    def sell_action(self):
        self.b_skip.lower()
        self.b_sell.lower()
        self.show_menu()

    def pay_action(self):
        self.b_pay.lower()
        self.show_menu()

    def draw_players(self):
        # first we delete old symbols
        for i in self.symbols:
            self.canvas.delete(i)

        # then we draw new
        screen_width, screen_height = self.get_width_height()
        self.multipliers = [0.2, 0.4, 0.6, 0.8]  # array with relative positions inside of field
        for index, i in enumerate(self.this_game.players):
            position = i.position
            x = self.this_game.board.fields[position].x
            y = self.this_game.board.fields[position].y
            extra_width = self.multipliers[index] * 0.2 * screen_width
            extra_height = 0.1 * screen_height
            radius = 0.02 * screen_height
            att1 = x / 5 * screen_width + extra_width - radius
            att2 = y / 5 * screen_height + extra_height - radius
            att3 = x / 5 * screen_width + extra_width + radius
            att4 = y / 5 * screen_height + extra_height + radius
            self.symbols[index] = self.canvas.create_oval(att1, att2, att3, att4, fill=i.name)
