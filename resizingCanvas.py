import tkinter as tk


class ResizingCanvas(tk.Canvas):
    def __init__(self, parent, fields, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.window = parent
        self.fields = fields
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.window.update()
        screen_width = self.window.winfo_width()
        screen_height = self.window.winfo_height()
        self.config(width=screen_width, height=screen_height)
        for i in self.fields:
            self.delete(i.rectangle)
            print(screen_width, screen_height)
            i.rectangle = self.create_rectangle((i.x / 5) * screen_width, (i.y / 5) * screen_height, ((i.x + 1) / 5) * screen_width, ((i.y + 1) / 5) * screen_height, fill='DarkOrchid1')