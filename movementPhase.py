
def move_troops(player):
    print("Movendo tropas")
    if (from_territory := player.ask_from_territory()) is None:
        print("Territorio de origem invalido")
        return

    to_territory = player.ask_to_territory(from_territory)
    quantity = player.choose_moving_troops(from_territory)
    from_territory.remove_troops(quantity)
    to_territory.add_troops(quantity)
