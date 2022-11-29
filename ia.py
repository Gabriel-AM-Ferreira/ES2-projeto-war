
import player

import iaRandomizer as randomizer


class IA(player.Player) :

    def __init__(self, name):
        
        super().__init__(name)

    

    def add_troops(self, troops_to_add, territory_list):
        print("IA pensando......")
        while troops_to_add > 0:
            print(f"{self.name} tem {troops_to_add} tropas para distribuir.")
            terr = randomizer.territory_distribution(territory_list)
            quantity = randomizer.territory_amount_to_distribute(troops_to_add)
            terr.add_troops(quantity)
            troops_to_add -= quantity
            print(f"O {self.name} adicionou {quantity} no território {terr.name}")

    def get_viable_attackers(self):
        terr_list = []
        for terr in self.territories:
            if terr.troops > 1 and len(terr.get_hostile_neighbors()) > 0:
                terr_list.append(terr)
        
        return terr_list
    
    def get_viable_movers(self):
        terr_list = []
        for terr in self.territories:
            if terr.troops > 1 and len(terr.get_friendly_neighbors()) > 0:
                terr_list.append(terr)
        
        return terr_list

    def ask_from_territory(self):
        print("Ia pensando......")
        terr = randomizer.pick_a_territory_to_move(self.get_viable_movers())
        print(f"O {self.name} vai mover o territorio {terr.name}")
        return terr

    def ask_to_territory(self, from_territory):
        print("Ia pensando.......")
        friendly_neighbors = from_territory.get_friendly_neighbors()
        terr = randomizer.pick_where_to_move_troops(friendly_neighbors)
        print(f"O {self.name} vai mover tropas de {from_territory.name} para {terr.name}")
        return terr

    def choose_moving_troops(self, from_territory):
        print("Ia pensando.......")
        troops = randomizer.pick_amount_of_troops_to_move(from_territory.troops-1)
        print(f"O {self.name} vai mover {troops} tropas")
        return troops

    def get_attacking_territory(self):
        print("IA pensando......")
        while True:
            if self.get_viable_attackers() is None:
                return None
            terr = randomizer.territory_distribution(self.get_viable_attackers())
            print(f"O {self.name}  usar o territorio {terr.name} para atacar")
            return terr


    def get_defending_territory(self, attacking_territory):
        print("IA pensando......")
        hostile_neighbors = attacking_territory.get_hostile_neighbors()
        terr = randomizer.territory_to_attack(hostile_neighbors)
        print(f"O {self.name} vai atacar o território {terr.name}")
        return terr

    def choose_attacking_troops(self, attacking_territory):
        print("IA pensando......")
        troops = randomizer.amount_to_attack(attacking_territory.troops-1)
        print(f"O {self.name} vai usar {troops} tropas para atacar")
        return troops
    
    def move_pieces(self,total):
        print("Ia pensando.....")
        num = randomizer.amount_to_move(total)
        print(f"O {self.name} vai mover {num} tropas")
        return num

    def attack_or_pass(self):
        num = str(randomizer.attack_or_pass())
        if num == "1":
            print(f"O {self.name} escolheu atacar!")
        else:
            print(f"O {self.name} escolheu passar!")
        return num

    def move_or_pass(self):
        num = str(randomizer.move_or_pass())
        if num == "1":
            print(f"O {self.name} escolheu mover!")
        else:
            print(f"O {self.name} escolheu passar!")
        return num