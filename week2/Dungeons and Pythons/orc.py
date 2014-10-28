from entity import Entity

class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor

    def berserk_factor_check(self):
        if self.berserk_factor < 1:
            self.berserk_factor = 1
            return self.berserk_factor

        elif self.berserk_factor > 2:
            self.berserk_factor = 2
            return self.berserk_factor
            
        else:
            return self.berserk_factor

    def attack(self):
        if self.has_weapon():
            if self.weapon.critical_hit():
                return self.berserk_factor * self.weapon.damage * 2
            else:
                return self.berserk_factor * self.weapon.damage
        else:
            return 0

   