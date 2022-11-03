from inputPlayer import ask_quantity, ask_yes_or_no

def move_troops(player):
    while True:
        print("Movendo tropas")
        if (from_territory := player.ask_from_territory()) is None:
            return

        to_territory = player.ask_to_territory(from_territory)
        quantity = player.choose_moving_troops(from_territory)
        from_territory.remove_troops(quantity)
        to_territory.add_troops(quantity)