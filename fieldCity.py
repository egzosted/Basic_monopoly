import field


class FieldCity(field.Field):
    def __init__(self, board, position, name, value, rent_value, window, x, y, canvas, color):
        super().__init__(board, position, name, value, window, x, y, canvas, color)
        self.rent_value = rent_value
        self.owner = None

    def handle_player(self, playerID):
        print("Hello")
        # if board.owners[self.name] == None :
        #     showOffer()
        # elif board.owners[self.name] == playerID :
        #     welcomeHost()
        # else :
        #     chargeRent()

    def showOffer(self):
        #runs when player is on empty field
        pass

    def welcomeHost(self):
        #runs when host come to his field
        pass

    def chargeRent(self):
        #runs when non-host come to field
        pass
