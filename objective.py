class Objective:
    def __init__(self, description):
        self.description = description
        self.owner = None
        self.is_complete = False

    def is_completed(self, player):
        objective_types = {
            "Destruir": self.destroy,
        }
        objective_types[self.description.split()[0]](player)
        return self.is_complete

