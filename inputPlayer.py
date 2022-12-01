from getObject import get_object_by_name
from menu import *
from Button import *

def ask_player_name():
    while True:
        name = input("Qual o nome do jogador?\n")
        if name != "":
            break
        print("Nome invalido")
    return name

def ask_color(colors, screen):

    prompt= Button(screen, (1096,0),"    Clique na sua cor !    ")
    vermelho = Button(screen, (1096,prompt.h),"aaaaaaaaaa")
    Button.colore(vermelho, (255,0,0))
    azul = Button(screen, (1096+vermelho.w, prompt.h), "aaaaaaaaaa")
    Button.colore(azul, "blue")
    verde = Button(screen, (1096, prompt.h+vermelho.h), "aaaaaaaaaa")
    Button.colore(verde, "green")
    amarelo = Button(screen, (1096+vermelho.w, prompt.h+vermelho.h), "aaaaaaaaaa")
    Button.colore(amarelo, "yellow")
    preto = Button(screen, (1096, prompt.h+2*amarelo.h), "aaaaaaaaaa")
    Button.colore(preto, (50,50,50))
    branco = Button(screen, (1096+vermelho.w, prompt.h+2*amarelo.h), "aaaaaaaaaa")
    Button.colore(branco, "white")

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if Button.clicado(vermelho, event):
                color = "VERMELHO"
                return color
            if Button.clicado(azul, event):
                color = "AZUL"
                return color
            if Button.clicado(verde, event):
                color = "VERDE"
                return color
            if Button.clicado(amarelo, event):
                color = "AMARELO"
                return color
            if Button.clicado(preto, event):
                color = "PRETO"
                return color
            if Button.clicado(branco, event):
                color = "BRANCO"
                return color

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

def ask_yes_or_no(question):
    while True:
        answer = input(f"{question} (s/n)\n")
        if answer == "s":
            return True
        elif answer == "n":
            return False
        print("Resposta invalida")