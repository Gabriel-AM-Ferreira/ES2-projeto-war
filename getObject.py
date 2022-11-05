
def get_object_by_name(name, objects):
    for obj in objects:
        if obj.name == name:
            return obj
    return None

def is_continent_owned_by_player(continent_name, player):
    continent = get_object_by_name(continent_name, player.continents)
    for territory in continent.territories:
        if territory.owner != player:
            return False
    return True