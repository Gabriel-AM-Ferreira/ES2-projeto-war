
def get_object_by_name(name, objects):
    for obj in objects:
        if obj.name == name:
            return obj
    return None