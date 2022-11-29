import random

def define_ia_name(num):
    return "Player "+str(num)

def pick_random_color(colors):
    return random.choice(colors)

def territory_distribution(territory_list):
    return random.choice(territory_list)

def territory_amount_to_distribute(troops_to_add):
    return random.randint(1,troops_to_add)

def territory_to_attack(territories):
    return territory_distribution(territories)

def amount_to_attack(max):
    return random.randint(1,max)

def amount_to_move(total):
    return random.randint(1,total)

def attack_or_pass():
    return random.randint(1,2)

def move_or_pass():
    return random.randint(1,2)

def pick_a_territory_to_move(valid_movers):
    return random.choice(valid_movers)

def pick_where_to_move_troops(friendly_neighbors):
    return random.choice(friendly_neighbors)

def pick_amount_of_troops_to_move(avaiable_troops):
    return random.randint(1,avaiable_troops)


    

