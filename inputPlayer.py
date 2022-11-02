from getObject import get_object_by_name

def ask_player_name():
    while True:
        name = input("Qual o nome do jogador?\n")
        if name != "":
            break
        print("Nome invalido")
    return name

def ask_color(colors):
    while True:
        color = input(f"Qual cor deseja?\n{colors}\n")
        if color in colors:
            return color
        print("Cor invalida")

def ask_territory(territories, question):
    while True:
        territory_name = input(f"{question}\n{[territory.name for territory in territories]}\n")
        terr = get_object_by_name(territory_name, territories)
        if terr is not None:
            break
        print("Territorio invalido")
    return terr

def ask_quantity(troops, question):
    while True:
        quantity = int(input(f"{question}"))
        if quantity <= troops and quantity > 0:
            break
        print("Quantidade invalida de tropas")
    return quantity

def ask_quantity_combat(troops, question):
    while True:
        quantity = int(input(f"{question}"))
        if quantity <= troops and quantity > 0 and quantity < 4:
            break
        print("Quantidade invalida de tropas")
    return quantity

def ask_card(cards):
    while True:
        card_name = input(f"Qual carta deseja trocar?\n{[card.territory for card in cards]}\n")
        card = get_object_by_name(card_name, cards)
        if card is not None:
            return card
        print("Carta invalida")