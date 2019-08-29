import board, game
import tkinter as tk


class GameWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1024x768")
        self.game = game.Game(self.window)
        self.window.mainloop()
