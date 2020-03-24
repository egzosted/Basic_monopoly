import tkinter as tk


class Start:
    def __init__(self):
        self.window = tk.Tk()
        self.l_introduction = tk.Label(
            self.window, text="Welcome to Monopoly!", font=('Courier', 35))
        self.l_enter = tk.Label(self.window, text="Enter number of players: ", font=('Courier', 24))
        self.e_players = tk.Entry(self.window)
        self.b_confirm = tk.Button(self.window, text="Confirm", command=self.get_num_players)
        self.l_introduction.grid(row=0, column=0, columnspan=2)
        self.l_enter.grid(row=1, column=0)
        self.e_players.grid(row=1, column=1)
        self.b_confirm.grid(row=2, column=0, columnspan=2)
        self.num_players = int()
        self.window.mainloop()

    def get_num_players(self):
        self.num_players = self.e_players.get()
        self.window.destroy()
