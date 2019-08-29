import random


class Player:
    def __init__(self, name, cash):
        self.__name = name
        self.cash = cash
        self.__position = 0

    def move(self, board_size):
        shift = random.randint(1, 6)    # player can move around maximally 6 fields
        self.__position += shift
        self.__position %= board_size

    def pay(self, cost):
        self.cash -= cost




# atrybuty:
# kasa
# nazwa
# pozycja

# metody:
# ruch (odpala metode obslugi dla danego pola)
# wystawienie oferty sprzedazy nieruchomosci
# przyjecie oferty kupna
# zaplacenie/otrzymanie bonusu


# ziomus to player