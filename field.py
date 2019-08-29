from abc import ABC, abstractmethod
import tkinter as tk
import resizingCanvas as rc


class Field(ABC):
    def __init__(self, board, position, name, value, window, x, y, canvas):
        self.board = board
        self.position = position
        self.name = name
        self.value = value
        self.x = x
        self.y = y
        screen_width = window.winfo_width()
        screen_height = window.winfo_height()
        # self.canvas = rc.ResizingCanvas(self.window, height=screen_height / 5, width=screen_width / 5)
        self.rectangle = canvas.create_rectangle((x / 5) * screen_width, (y / 5) * screen_height, ((x + 1) / 5) * screen_width, ((y + 1) / 5) * screen_height, fill='green')

    @abstractmethod
    def handle_player(self, player):
        pass
