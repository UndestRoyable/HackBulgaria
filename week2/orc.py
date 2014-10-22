from entity import Entity

class Orc(Entity):

    def __init__(self, name, health, berserkfactor):
        super().__init__(name, health)
        self.berserkfactor = berserkfactor

    def berserk_factor_check(self):
        if self.berserk_factor < 1:
            self.berserk_factor = 1
            return self.berserk_factor

        elif self.berserk_factor > 2:
            self.berserk_factor = 2
            return self.berserk_factor
            
        else:
            return self.berserk_factor

   