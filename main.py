from GUI import color, start, game_window as gw

# first we launch window where user chooses number of players
introduction = start.Start()
num_players = introduction.num_players  # after window is closed  we can read value

# then we can launch window where users choose their identifiers (colors)
color = color.Color(num_players)
players_color = color.players_color


game = gw.GameWindow(players_color)
