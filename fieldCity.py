import field
MAP_SIZE = 16


class FieldCity(field.Field):
    def __init__(self, board, position, name, value, rent_value, window, x, y, canvas, color, gw):
        super().__init__(board, position, name, value, window, x, y, canvas, color, gw)
        self.rent_value = rent_value
        self.owner = None

    def handle_player(self, player):
        if self.owner is None:
            self.game_window.show_offer(self, player)
        elif self.owner == player.name:
            self.game_window.show_sell(self, player)
        else:
            self.game_window.pay_rent(self, player)

    def first_owner(self, player):
        if player.cash >= self.value:
            self.owner = player.name
            player.pay(self.value)
            self.game_window.window.update()
            screen_width = self.game_window.window.winfo_width()
            screen_height = self.game_window.window.winfo_height()
            self.owner_rectangle = self.canvas.create_rectangle((self.x / 5) * screen_width, (self.y / 5) * screen_height,
                                                                ((self.x + 1) / 5) * screen_width,
                                                                ((self.y + 0.2) / 5) * screen_height,
                                                                fill=self.owner)

    def sell_to_bank(self, player):
        self.owner = None
        player.collect(self.rent_value)
        self.canvas.delete(self.owner_rectangle)
        self.owner_rectangle = None

    def charge_rent(self, player, owner):
        if self.check_bankruptcy(player):
            owner.collect(self.rent_value)
            return
        player.pay(self.rent_value)
        owner.collect(self.rent_value)
