
def distribute_troops(player):
    print(f"Distribuicao de tropas do {player.name}") 
    # pega o numero de territorios do jogador
    number_of_territories = len(player.territories)
    # calcula o numero de tropas a serem distribuidas
    troops_to_distribute = max([3, number_of_territories // 2])
    # adiciona as tropas distribuidas ao jogador
    player.add_normal_troops(troops_to_distribute)
    # adiciona tropas extras dos continentes
    player.add_extra_troops()

def cards_exchange(player, exchange_number, used_cards):
    cards_quantity = len(player.cards)
    if cards_quantity < 3:
        return used_cards, exchange_number
    elif cards_quantity >= 5:
        used_cards = used_cards + player.exchange_cards(exchange_number)
        exchange_number += 1
        return used_cards, exchange_number
    print(f"{player.name} deseja trocar cartas?")
    print("1 - Sim")
    print("2 - Nao")
    while True:
        option = input("Opcao: ")
        if option == "1":
            used_cards = used_cards + player.exchange_cards(exchange_number)
            exchange_number += 1
            break
        elif option == "2":
            break
        print("Opcao invalida!")
    return used_cards, exchange_number
