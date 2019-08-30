from abc import ABC, abstractmethod
import tkinter as tk
import resizingCanvas as rc


class Field(ABC):
    def __init__(self, board, position, name, value, window, x, y, canvas, color, gw):
        self.board = board
        self.position = position
        self.name = name
        self.value = value
        self.canvas = canvas
        self.color = color
        self.x = x
        self.y = y
        self.game_window = gw
        self.owner = None
        screen_width = window.winfo_width()
        screen_height = window.winfo_height()
        self.rectangle = canvas.create_rectangle((x / 5) * screen_width, (y / 5) * screen_height, ((x + 1) / 5) * screen_width, ((y + 1) / 5) * screen_height, fill='green')
        self.text = canvas.create_text((self.x / 5) * screen_width + 0.1 * screen_width,
                                (self.y / 5) * screen_height + 0.15 * screen_height, text=self.name, font=("Monospace", 20))
        if self.owner is not None:
            self.owner_rectangle = canvas.create_rectangle((x / 5) * screen_width, (y / 5) * screen_height,
                                                           ((x + 1) / 5) * screen_width,
                                                           ((y + 0.2) / 5) * screen_height,
                                                           fill=self.owner)


    @abstractmethod
    def handle_player(self, player):
        pass
