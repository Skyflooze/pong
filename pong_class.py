class Raquettes:
    
    def __init__(self):
        self.bx = 4
        self.by = 4
    
    def set_direction(self,val):
        self._direction = val

    def get_direction(self):
        return self._direction

    direction = property(get_direction, set_direction)
