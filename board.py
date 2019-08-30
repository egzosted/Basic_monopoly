import fieldBonus, fieldCity, resizingCanvas as rC
import tkinter as tk


class Board:
    def __init__(self, window, gw):
        self.size = 16  # 12 cities and 4 special fields
        self.game_window = gw
        self.window = window
        self.window.update()
        screen_width = self.window.winfo_width()
        screen_height = self.window.winfo_height()
        self.fields = []
        self.canvas = rC.ResizingCanvas(self.window, self.fields, self.game_window, width=screen_width, height=screen_height)
        self.canvas.pack()

        self.fields.append(fieldBonus.FieldBonus(self, 0, "Start", 200, window, 0, 4, self.canvas, "snow", gw, True))
        self.fields.append(fieldCity.FieldCity(self, 1, "Madrid", 100, 50, window, 0, 3, self.canvas, "khaki2", gw))
        self.fields.append(fieldCity.FieldCity(self, 2, "Rome", 200, 100, window, 0, 2, self.canvas, "khaki3", gw))
        self.fields.append(fieldCity.FieldCity(self, 3, "Berlin", 300, 150, window, 0, 1, self.canvas, "khaki4", gw))
        self.fields.append(fieldBonus.FieldBonus(self, 4, "Zoo", 200, window, 0, 0, self.canvas, "pale green", gw, False))
        self.fields.append(fieldCity.FieldCity(self, 5, "Bogota", 400, 200, window, 1, 0, self.canvas, "spring green", gw))
        self.fields.append(fieldCity.FieldCity(self, 6, "Sao Paulo", 500, 250, window, 2, 0, self.canvas, "lime green", gw))
        self.fields.append(fieldCity.FieldCity(self, 7, "Lima", 600, 300, window, 3, 0, self.canvas, "forest green", gw))
        self.fields.append(fieldBonus.FieldBonus(self, 8, "Stock", 200, window, 4, 0, self.canvas, "gray73", gw, True))
        self.fields.append(fieldCity.FieldCity(self, 9, "Toronto", 700, 350, window, 4, 1, self.canvas, "DarkOrchid2", gw))
        self.fields.append(fieldCity.FieldCity(self, 10, "New York", 800, 400, window, 4, 2, self.canvas, "DarkOrchid3", gw))
        self.fields.append(fieldCity.FieldCity(self, 11, "Los Angeles", 900, 450, window, 4, 3, self.canvas, "DarkOrchid4", gw))
        self.fields.append(fieldBonus.FieldBonus(self, 12, "Prison", 200, window, 4, 4, self.canvas, "gray21", gw, False))
        self.fields.append(fieldCity.FieldCity(self, 13, "Beijing", 1000, 500, window, 3, 4, self.canvas, "LightPink1", gw))
        self.fields.append(fieldCity.FieldCity(self, 14, "Seoul", 1100, 550, window, 2, 4, self.canvas, "LightPink2", gw))
        self.fields.append(fieldCity.FieldCity(self, 15, "Tokyo", 1200, 600, window, 1, 4, self.canvas, "LightPink3", gw))
