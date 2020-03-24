import field


class FieldBonus(field.Field):
    def __init__(self, board, position, name, value, window, x, y, canvas, color, gw, positive):
        super().__init__(board, position, name, value, window, x, y, canvas, color, gw)
        self.positive = positive    # boolean value that say if player gets money or has to pay
        self.rent_value = 200

    def handle_player(self, player):
        if self.positive:
            self.check_bankruptcy(player)
            player.collect(self.value)
        else:
            player.pay(self.value)
        self.game_window.show_menu()
