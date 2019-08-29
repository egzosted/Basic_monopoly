import tkinter as tk


class Color:
    def __init__(self, num_players):
        self.window = tk.Tk()
        self.num_players = int(num_players)
        self.options = ['yellow', 'red', 'green', 'blue']   # player will be represented by 1 of 4 colors
        self.o_menu = []    # list of drop down menus
        self.l_players = []  # list of labels for players
        self.variable = []  # list of strings that represent specific option
        self.players_color = []  # list of colors that players chose
        self.b_confirm = tk.Button(self.window, text="Confirm", command=self.get_colors)
        for i in range(self.num_players):
            self.l_player = tk.Label(text=f"Choose color of {i+1}. player", font=('Courier', 25))
            self.l_players.append(self.l_player)
            self.variable.append(tk.StringVar(self.window))
            self.variable[i].set(self.options[0])
            self.o_menu.append(tk.OptionMenu(self.window, self.variable[i], *self.options))
            self.l_players[i].grid(row=i, column=0)
            self.o_menu[i].grid(row=i, column=1)
        self.b_confirm.grid(row=int(num_players), column=0, columnspan=2)
        self.window.mainloop()

    def get_colors(self):
        for i in range(self.num_players):
            self.players_color.append(self.variable[i].get())
        self.window.destroy()
