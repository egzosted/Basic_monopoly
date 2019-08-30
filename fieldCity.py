import field


class FieldCity(field.Field):
    def __init__(self, board, position, name, value, rent_value, window, x, y, canvas, color, gw):
        super().__init__(board, position, name, value, window, x, y, canvas, color, gw)
        self.rent_value = rent_value
        self.owner = None

    def handle_player(self, player):
        if self.owner is None:
            self.game_window.show_offer(self, player)
        # elif board.owners[self.name] == playerID :
        #     welcomeHost()
        # else :
        #     chargeRent()

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

    def welcomeHost(self):
        #runs when host come to his field
        pass

    def chargeRent(self):
        #runs when non-host come to field
        pass
