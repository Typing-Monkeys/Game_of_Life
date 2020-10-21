class Entity:
    def __init__(self):
        self.alive = False
        self.neighbour_alive = 0

    def set_alive(self):
        self.alive = True

    def set_death(self):
        self.alive = False

    def __repr__(self):
        result = ""

        if (self.alive is True):
            result = "x"
        else:
            result = " "
        
        return result
