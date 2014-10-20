class Orc:

    def __init__(self,name,health,berserk_factor):
        self.name = name
        self.health = health
        self.berserk_factor = berserk_factor
        #self._MAX_HEALTH = health

    def berserk_factor_check(self):
        if self.berserk_factor < 1:
            self.berserk_factor = 1
            return self.berserk_factor

        elif self.berserk_factor > 2:
            self.berserk_factor = 2
            return self.berserk_factor
            
        else:
            return self.berserk_factor

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_damage(self,damage_points):
        if damage_points > self.health:
            self.health = 0
            return self.health
        else:
            return self.health - damage_points

    def take_healing(self,healing_points):
        if self.health == 0:
            return False
        elif self.health + healing_points > 100:
            return False
        elif self.health + healing_points < 100:
            return True

        