import fieldBonus
import fieldCity
import resizingCanvas as rC

MAP_SIZE = 16  # map with 16 objects like cities and extra places (zoo e.g)
POSITIVE_BONUS = True  # on extra field you gain cash
NEGATIVE_BONUS = False  # on extra field you lose cash
EXTRA_VALUE = 200  # cash of extra field


class Board:
    def __init__(self, window, gw, game):
        self.size = MAP_SIZE  # 12 cities and 4 special fields
        self.game_window = gw
        self.window = window
        self.this_game = game
        self.window.update()
        self.coordinates = [i for i in range(MAP_SIZE)]  # 1d coordinates of fields
        self.values = [(i + 1) * 100 for i in range(0, MAP_SIZE)]  # value of field to buy
        self.rent_values = [(i + 1) * 50 for i in range(0, MAP_SIZE)]  # value of rent and sell
        self.x = [i for i in range(5)]  # x coordinate in 2d
        self.y = [i for i in range(5)]  # y coordinate in 2d
        screen_width = self.window.winfo_width()
        screen_height = self.window.winfo_height()
        self.fields = []
        self.canvas = rC.ResizingCanvas(self.window, self.fields,
                                        self.game_window, width=screen_width, height=screen_height)
        self.canvas.pack()

        self.fields.append(fieldBonus.FieldBonus(self, self.coordinates[0], "Start", EXTRA_VALUE,
                                                 window, self.x[0], self.y[4], self.canvas, "snow", gw, POSITIVE_BONUS))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[1], "Madrid", self.values[0],
                                               self.rent_values[0], window, self.x[0], self.y[3], self.canvas, "khaki2", gw))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[2], "Rome", self.values[1],
                                               self.rent_values[1], window, self.x[0], self.y[2], self.canvas, "khaki3", gw))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[3], "Berlin", self.values[3],
                                               self.rent_values[3], window, self.x[0], self.y[1], self.canvas, "khaki4", gw))
        self.fields.append(fieldBonus.FieldBonus(self, self.coordinates[4], "Zoo", EXTRA_VALUE, window,
                                                 self.x[0], self.y[0], self.canvas, "pale green", gw, NEGATIVE_BONUS))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[5], "Bogota", self.values[5], self.rent_values[5],
                                               window, self.x[1], self.y[0], self.canvas, "spring green", gw))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[6], "Sao Paulo", self.values[6],
                                               self.rent_values[6], window, self.x[2], self.y[0], self.canvas, "lime green", gw))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[7], "Lima", self.values[7], self.rent_values[7],
                                               window, self.x[3], self.y[0], self.canvas, "forest green", gw))
        self.fields.append(fieldBonus.FieldBonus(self, self.coordinates[8], "Stock", EXTRA_VALUE,
                                                 window, self.x[4], self.y[0], self.canvas, "gray73", gw, POSITIVE_BONUS))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[9], "Toronto", self.values[9], self.rent_values[9],
                                               window, self.x[4], self.y[1], self.canvas, "DarkOrchid2", gw))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[10], "New York", self.values[10],
                                               self.rent_values[10], window, self.x[4], self.y[2], self.canvas, "DarkOrchid3", gw))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[11], "Los Angeles", self.values[11],
                                               self.rent_values[11], window, self.x[4], self.y[3], self.canvas, "DarkOrchid4", gw))
        self.fields.append(fieldBonus.FieldBonus(self, self.coordinates[12], "Prison", EXTRA_VALUE,
                                                 window, self.x[4], self.y[4], self.canvas, "gray21", gw, NEGATIVE_BONUS))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[13], "Beijing", self.values[13],
                                               self.rent_values[13], window, self.x[3], self.y[4], self.canvas, "LightPink1", gw))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[14], "Seoul", self.values[14], self.rent_values[14],
                                               window, self.x[2], self.y[4], self.canvas, "LightPink2", gw))
        self.fields.append(fieldCity.FieldCity(self, self.coordinates[15], "Tokyo", self.values[15], self.rent_values[15],
                                               window, self.x[1], self.y[4], self.canvas, "LightPink3", gw))
