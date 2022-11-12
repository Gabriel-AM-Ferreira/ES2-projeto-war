from gameloop import *

class Menu:
    def __init__(self):
        n = int(input("Digite o numero de jogadores\n"))
        game = GameLoop(n)
        game.start()
        