from dice import *
from inputPlayer import ask_quantity

def attack(player):
    # escolhe o territorio atacante
    if (attacking_territory := player.get_attacking_territory()) is None:
        return
    # escolhe o territorio alvo
    target_territory = player.get_defending_territory(attacking_territory)
    # escolhe o numero de tropas
    attacking_troops = player.choose_attacking_troops(attacking_territory)
    # escolhe o numero de tropas do alvo
    target_troops = target_territory.owner.choose_defending_troops(target_territory)
    # realiza o ataque
    combat(attacking_territory, target_territory, attacking_troops, target_troops)


def combat(attacking_territory, target_territory, attacking_troops, target_troops):
    # calcula os dados
    dice = Dice()
    attacking_dices = dice.roll_many(attacking_troops)
    target_dices = dice.roll_many(target_troops)
    # ordena os dados
    attacking_dices.sort(reverse=True)
    print(f"Dados do atacante: {attacking_dices}")
    target_dices.sort(reverse=True)
    print(f"Dados do defensor: {target_dices}")
    # compara os dados
    failed_attacks = 0
    for i in range(min([attacking_troops, target_troops])):
        if attacking_dices[i] > target_dices[i]:
            target_territory.remove_troops(1)
        else:
            attacking_territory.remove_troops(1)
            failed_attacks += 1

    # verifica se o territorio foi conquistado
    if target_territory.troops == 0:
        
        troops_to_move = attacking_territory.owner.move_pieces(attacking_troops - failed_attacks) 
        conquer_territory(attacking_territory, target_territory, troops_to_move)
    else:
        print("O ataque falhou!")

def conquer_territory(attacking_territory, target_territory, attacking_troops):
    # remove as tropas do territorio atacante
    attacking_territory.remove_troops(attacking_troops)
    # transfere as tropas para o territorio conquistado
    target_territory.add_troops(attacking_troops)
    # verifica se o jogador defensor perdeu o continente
    check_continent_loss(target_territory.owner, target_territory.continent)
    # transfere o territorio conquistado para o jogador atacante
    transfer_territory(attacking_territory.owner, target_territory)
    # verifica se o jogador atacante conquistou o continente
    check_continent_conquest(attacking_territory.owner, target_territory.continent)
    
    
def check_continent_loss(player, continent):
    if continent in player.continents:
        player.remove_continent(continent)
        print(f"O {player.name} perdeu o continente {continent.name}!")

def transfer_territory(attacking_player, target_territory):
    defending_player = target_territory.owner
    defending_player.remove_territory(target_territory)
    attacking_player.add_territory(target_territory)
    target_territory.owner = attacking_player

    check_player_elimination(attacking_player, defending_player)

def check_player_elimination(attacking_player, defending_player):
    if defending_player.territories == []:
        attacking_player.defeated_players.append(defending_player)
        attacking_player.cards.extend(defending_player.cards)
        print(f"O {defending_player.name} foi eliminado!")

def check_continent_conquest(player, continent):
    conquered = True
    for territory in continent.territories:
        if territory.owner != player:
            conquered = False
            break
    if conquered:
        player.add_continent(continent)
        print(f"O {player.name} conquistou o continente {continent.name}!")