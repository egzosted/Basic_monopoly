import field


class FieldBonus(field.Field):
    def __init__(self, board, position, name, value, window, x, y, canvas, color):
        super().__init__(board, position, name, value, window, x, y, canvas, color)

    def handle_player(self, playerID):
        print("Hello")
