class Raquettes:
    
    def __init__(self, direction):
        self._direction = direction
    
        

    def set_direction(self,val):
        self._direction = val

    def get_direction(self):
        return self._direction

    direction = property(get_direction, set_direction)