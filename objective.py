class Objective:
    def __init__(self, description):
        self.description = description
        self.owner = None
        self.is_complete = False

    def is_completed(self, player):
        return False
    
