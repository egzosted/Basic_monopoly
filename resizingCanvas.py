import tkinter as tk


class ResizingCanvas(tk.Canvas):
    def __init__(self, parent, fields, gw, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.gw = gw
        self.window = parent
        self.fields = fields
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        if self.gw.symbols is not True:
            self.gw.on_resize()
        self.window.update()
        screen_width = self.window.winfo_width()
        screen_height = self.window.winfo_height()
        self.config(width=screen_width, height=screen_height)
        for i in self.fields:
            self.delete(i.rectangle)
            self.delete(i.text)
            i.rectangle = self.create_rectangle((i.x / 5) * screen_width, (i.y / 5) * screen_height, ((i.x + 1) / 5) * screen_width, ((i.y + 1) / 5) * screen_height, fill=i.color)
            if i.owner is not None:
                self.delete(i.owner_rectangle)
                i.owner_rectangle = self.create_rectangle((i.x / 5) * screen_width, (i.y / 5) * screen_height,
                                                           ((i.x + 1) / 5) * screen_width,
                                                           ((i.y + 0.2) / 5) * screen_height,
                                                           fill=i.owner.name)
            i.text = self.create_text((i.x / 5) * screen_width + 0.1 * screen_width, (i.y / 5) * screen_height + 0.15 * screen_height, text=i.name, font=("Monospace", 20))
